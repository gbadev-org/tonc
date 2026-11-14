/*
 * Adapted from gbdev's Pan Docs preprocessor
 * https://github.com/gbdev/pandocs/blob/master/preproc/src/main.rs
 *
 * This Source Code Form is subject to the
 * terms of the Mozilla Public License, v.
 * 2.0. If a copy of the MPL was not
 * distributed with this file, You can
 * obtain one at
 * http://mozilla.org/MPL/2.0/.
 */

use std::io;
use std::process;

use mdbook_preprocessor::{
    book::{Book, BookItem},
    errors::Error,
    Preprocessor, PreprocessorContext,
};

mod admonitions;
mod git;
use git::Commit;

fn main() -> Result<(), Error> {
    let mut args = std::env::args();
    let _ = args.next(); // Program name.

    let preprocessor = Pandocs::new();

    if args.next().is_some_and(|arg| arg == "supports") {
        let renderer_name = args
            .next()
            .expect("Missing argument: name of renderer to check for compat");
        assert!(args.next().is_none(), "Unexpected extra args");
        handle_supports(&preprocessor, &renderer_name);
    } else {
        handle_preprocessing(&preprocessor)
    }
}

fn handle_preprocessing(pre: &dyn Preprocessor) -> Result<(), Error> {
    let (ctx, book) = mdbook_preprocessor::parse_input(io::stdin())?;

    if ctx.mdbook_version != mdbook_preprocessor::MDBOOK_VERSION {
        // We should probably use the `semver` crate to check compatibility
        // here...
        eprintln!(
            "Warning: The {} plugin was built against version {} of mdbook, \
             but we're being called from version {}",
            pre.name(),
            mdbook_preprocessor::MDBOOK_VERSION,
            ctx.mdbook_version
        );
    }

    let processed_book = pre.run(&ctx, book)?;
    serde_json::to_writer(io::stdout(), &processed_book)?;

    Ok(())
}

fn handle_supports(pre: &dyn Preprocessor, renderer: &str) -> ! {
    let supported = pre.supports_renderer(renderer);

    // Signal whether the renderer is supported by exiting with 1 or 0.
    if supported.unwrap() {
        process::exit(0);
    } else {
        process::exit(1);
    }
}

struct Pandocs;

impl Pandocs {
    fn new() -> Pandocs {
        Pandocs
    }
}

impl Preprocessor for Pandocs {
    fn name(&self) -> &str {
        "pandocs-preproc"
    }

    fn supports_renderer(&self, renderer: &str) -> Result<bool, Error> {
        Ok(renderer != "not-supported")
    }

    fn run(&self, _: &PreprocessorContext, mut book: Book) -> Result<Book, Error> {


        let mut res = Ok(());

        book.for_each_mut(|item| {
            macro_rules! abort_if_err {
                ($expr:expr) => {
                    match $expr {
                        Err(e) => {
                            res = Err(e);
                            return;
                        }
                        Ok(ret) => ret,
                    }
                };
            }

            if res.is_err() {
                return;
            }

            if let BookItem::Chapter(ref mut chapter) = item {
                abort_if_err!(self.process_admonitions(chapter));

                if chapter.name == "Foreword" {
                    let commit = abort_if_err!(Commit::rev_parse("HEAD"));
                    chapter.content.push_str(&format!(
                        "<small>This document version was produced from git commit <a href=\"https://github.com/gbadev-org/tonc/tree/{}\"> <code>{}</code> </a> ({}). </small>",
                        commit.hash(), commit.short_hash(), commit.timestamp(),
                    ));
                }
            }
        });

        res.map(|_| book)
    }
}

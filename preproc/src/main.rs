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

use clap::{App, Arg, ArgMatches, SubCommand};
use mdbook::book::Book;
use mdbook::errors::Error;
use mdbook::preprocess::{CmdPreprocessor, Preprocessor, PreprocessorContext};
use mdbook::BookItem;

mod admonitions;
mod git;
use git::Commit;

pub fn make_app() -> App<'static, 'static> {
    App::new("pandocs-preproc")
        .about("A mdbook preprocessor for Pan Docs")
        .subcommand(
            SubCommand::with_name("supports")
                .arg(Arg::with_name("renderer").required(true))
                .about("Check whether a renderer is supported by this preprocessor"),
        )
}

fn main() -> Result<(), Error> {
    let matches = make_app().get_matches();

    // Users will want to construct their own preprocessor here
    let preprocessor = Pandocs::new();

    if let Some(sub_args) = matches.subcommand_matches("supports") {
        handle_supports(&preprocessor, sub_args);
    } else {
        handle_preprocessing(&preprocessor)
    }
}

fn handle_preprocessing(pre: &dyn Preprocessor) -> Result<(), Error> {
    let (ctx, book) = CmdPreprocessor::parse_input(io::stdin())?;

    if ctx.mdbook_version != mdbook::MDBOOK_VERSION {
        // We should probably use the `semver` crate to check compatibility
        // here...
        eprintln!(
            "Warning: The {} plugin was built against version {} of mdbook, \
             but we're being called from version {}",
            pre.name(),
            mdbook::MDBOOK_VERSION,
            ctx.mdbook_version
        );
    }

    let processed_book = pre.run(&ctx, book)?;
    serde_json::to_writer(io::stdout(), &processed_book)?;

    Ok(())
}

fn handle_supports(pre: &dyn Preprocessor, sub_args: &ArgMatches) -> ! {
    let renderer = sub_args.value_of("renderer").expect("Required argument");
    let supported = pre.supports_renderer(renderer);

    // Signal whether the renderer is supported by exiting with 1 or 0.
    if supported {
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

    fn supports_renderer(&self, renderer: &str) -> bool {
        renderer != "not-supported"
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

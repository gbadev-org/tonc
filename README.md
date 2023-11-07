# Tonc (Community Edition)

This is a community-maintained version of Tonc, the GBA programming tutorial originally written by Jasper Vijn (cearn).

## Setup

You need Python, Rust and mdBook.

```sh
# clone the repo
git clone --recurse-submodules git@github.com:gbadev-org/tonc.git
cd tonc

cargo install mdbook

# run the development server
mdbook serve --open
```

## Converting pages to markdown

Conversion can be done one page at a time.

You can use `pandoc` to get you started:

### 1. Initial conversion

```sh
cd content

# rename to avoid conflicts in page generation
mv intro.htm intro-old.htm

# run through pandoc (minus some extensions to get sane output)
pandoc --from=html --to=markdown-fenced_divs-bracketed_spans-escaped_line_breaks-smart --wrap=none -o intro.md intro-old.htm
```

Then, add metadata and replace the table of contents with a `<!-- toc -->` marker:

```md
Title: Introduction to Tonc
Date: 2003-09-01
Modified: 2023-08-13
Authors: Cearn

# ii. Introduction to Tonc

<!-- toc -->
```

### 2. Cleanup

Next, go through the page and fix anything that's broken.

For example:

*   `<span class="dfn">` should be changed back to `<dfn>` (for some reason pandoc messes this up). Same goes for `<kbd>` and some other tags.

    ```
    sed -i -E 's,<span class="dfn">([^<]+)</span>,<dfn>\1</dfn>,g' pagename.md
    ```

*   Section numbers should be removed from headings (but the number in the page title should stay, e.g. `# 3. My first GBA demo`)

    ```
    sed -i -E 's,^(##+) [0-9]+\.[0-9.]+,\1,g' pagename.md
    ```

*   Tables and Figures should be replaced with the raw HTML from the `-old.htm` file.

*   Equations are coded in MathML, which displays in all browsers since 2023 according to [Can I use](https://caniuse.com/mathml).
    It's recommended to write equations in LaTeX first, using a live preview tool such as [Online LaTeX Equation Editor](https://latexeditor.lagrida.com/).
    Right-click the preview and choose Copy to Clipboard > MathML Code.

*   Code blocks should have the correct language set on them (`c`, `asm`, `sh`, `makefile`)

*   Use backticks (`` ` ``) around code keywords and italics (`*`) around file names in the text.

*   Container tags need empty lines after them, otherwise the Markdown within won't be rendered properly. For example:

    ```html
    <div class="note">

    ...
    </div>

    <div style="margin-left:1.2cm;">

    ...
    </div>
    ```

*   The `target` attribute should be removed from links:

    ```
    sed -i 's/{target="_blank"}//g' pagename.md
    ```

*  Image links with a `{#id}` attribute need to be converted to `<img>` tags:

    (vim substitute command)
    ```
    %s$!\[\(.\{-}\)\](\(.\{-}\)){\s*#\(.\{-}\)\s*}\s*$<img alt="\1" src="\2" id="\3">$g
    ```

Once it's in good shape, you can delete the original .htm file.

### 3. Figures, tables, equations

For autonumbering and cross-referencing of figures, tables and equations, we use a syntax based on [pandoc-xnos](https://github.com/tomduck/pandoc-xnos).


* The `id` attribute is used to define a figure, e.g. `id="fig:foobar"` or `{#fig:foobar}`.

* Possible ID kinds are `fig:`, `tbl:` and `eq:` to define figures, tables, and equations respectively.

* Use `@fig:foobar` to refer to a figure.

* Use `*@fig:foobar` when the first letter should be capitalised.

* Use `!@fig:foobar` to print only the number (without the word 'fig').

* Use `{@fig:foobar}` to avoid clashing with surrounding syntax.

* The figure/table/equation prefix is defined by the page title.


For example, on the page *'ii. Introduction to Tonc'*, the following Markdown:

```html
<img src="img/toncdirs.png" id="fig:toncdirs" alt="Tonc directory structure">
**{*@fig:toncdirs}**: directories.
```

Will be rendered as:

<table>
 <tr>
  <td>
   <p>
   <img alt="Tonc directory structure" id="fig:toncdirs" src="content/img/toncdirs.png"><br>
    <strong>Fig ii.1</strong>: directories.
    </p>
  </td>
 </tr>
</table>

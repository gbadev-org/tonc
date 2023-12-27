# Tonc (Community Edition)

This repository hosts the source of the community-maintained version of Tonc, the GBA programming tutorial originally written by Jasper Vijn (cearn).

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

The book will be live at http://localhost:3000
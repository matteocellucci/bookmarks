# Bookmarks

[![License GPLV3](https://www.gnu.org/graphics/gplv3-88x31.png "License GPLv3")
](https://github.com/matteocellucci/nit/blob/master/LICENSE)

A dumb resource bookmarks CLI system heavly based on search rather then organize.

## Usage

```
Usage: bookmarks [OPTIONS] COMMAND [ARGS]...

  A dumb bookmarks system.

Options:
  --help  Show this message and exit.

Commands:
  find   Find a bookmark.
  ls     List all bookmarks.
  rm     Remove target bookmark.
  touch  Create or update a bookmark.
```

## Installation

Maybe you will find one of these tips handy:

### Th' linux way

1. Make sure `~/.local/bin` is in your `$PATH`;
2. `git clone https://github.com/matteocellucci/bookmarks.git`;
3. `ln -s $(pwd)/bookmarks/bookmarks.py ~/.local/bin/bookmarks`;
4. Enjoy `bookmarks` from anywhere.

### Th' python-ish way

1. `git clone https://github.com/matteocellucci/bookmarks.git`;
2. `cd bookmarks`
3. `pip install -e .`
4. Enjoy `bookmarks` from anywhere.

# Bookmarks

[![License GPLV3](https://www.gnu.org/graphics/gplv3-88x31.png "License GPLv3")
](https://github.com/matteocellucci/nit/blob/master/LICENSE)

A dumb resource bookmarks CLI

## Usage

```
Usage: bookmark [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  find    Search for a resource. Use doublequotes for exact phrase.
  ls      List all resources.
  rm      Remove a resource. WARNING: Indexes change every delete.
  touch   Create or update a resource.
```

## Installation tip

Maybe you will find this tip handy(ish):

1. Make sure `~/.local/bin` is in your `$PATH`;
2. `git clone https://github.com/matteocellucci/bookmarks.git`;
3. `ln -s $(pwd)/bookmarks/bookmarks.py ~/.local/bin/bookmarks`;
4. Enjoy `bookmarks` from anywhere.

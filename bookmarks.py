#!/usr/bin/env python

import os
import json
import click

@click.group()
def cli():
    """A dumb resources bookmarks system"""
    pass

@cli.command()
def ls():
    for i, bookmark in enumerate(_load_data()):
        click.echo(f"{i}# {bookmark}")

@cli.command()
@click.option("--title", default="", help="Resource title")
@click.option("--tags", default="", help="Comma separted words")
@click.argument("url")
def touch(title, tags, url):
    bookmarks = _load_data()
    generator = (bookmark for bookmark in bookmarks if bookmark["url"] == url)
    bookmark = next(generator, { "url": url })
    bookmark.update({ "title": title, "tags": _clean_tags(tags) })
    if bookmark not in bookmarks:
        bookmarks.append(bookmark)
    _save_data(bookmarks)
    click.echo("Saved.")

@cli.command()
@click.argument("index")
def rm(index):
    bookmarks = _load_data()
    try:
        bookmarks.pop(int(index))
        _save_data(bookmarks)
        click.echo("Removed.")
    except IndexError:
        raise click.ClickException("Bookmark not found")

@cli.command()
@click.argument("terms", nargs=-1)
def find(terms):
    for i, bookmark in enumerate(_load_data()):
        for term in terms:
            if _match_bookmark(term, bookmark):
                click.echo(f"{i}# {bookmark}")

def _base_path():
    return os.environ.get("XDG_DATA_HOME", f"{os.environ['HOME']}/.local/share")

def _data_path():
    path = f"{_base_path()}/bookmarks"
    if not os.path.exists(path):
        os.makedirs(path)
    return f"{path}/data.json"

def _load_data():
    try:
        with open(_data_path(), "r+") as f:
            return json.load(f)
    except:
        return []

def _save_data(data):
    with open(_data_path(), "w") as f:
        json.dump(sorted(data, key = lambda k: k["url"]), f)

def _match_bookmark(query, bookmark):
    return query.lower() in bookmark["title"].lower() or \
            query.lower() in map(lambda t: t.lower(), bookmark["tags"]) or \
            query.lower() in bookmark["url"].lower()

def _clean_tags(tags):
    tags = tags.split(",")
    if "" in tags:
        tags.remove("")
    return sorted(tags)

if __name__ == '__main__':
    cli()


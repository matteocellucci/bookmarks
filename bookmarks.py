import os
import json
import click
import hashlib

from datetime import datetime

@click.group()
def cli():
    """A dumb bookmarks system."""
    pass

@cli.command()
def ls():
    """List all bookmarks."""
    for i, bookmark in enumerate(_load_data()):
        click.echo(f'{i}# {bookmark}')

@cli.command()
@click.option('--title', default='', help='Resource title.')
@click.option('--tags', default='', help='Comma separted words.')
@click.argument('url')
def touch(title, tags, url):
    """Create or update a bookmark. Bookmarks are identified by their url."""
    bookmarks = _load_data()
    generator = (bookmark for bookmark in bookmarks if bookmark['url'] == url)
    bookmark = next(generator, { 'url': url })
    bookmark.update({ 'title': title, 'tags': _clean_tags(tags), 'updated_at': _now() })
    if bookmark not in bookmarks:
        bookmark.update({ 'created_at': _now() })
        bookmarks.append(bookmark)
    _save_data(bookmarks)
    click.echo('Saved.')

@cli.command()
@click.argument('url')
@click.argument('editor', envvar='EDITOR', default='vim', required=False)
def editor(url, editor):
    """
    Open default editor to write notes about a bookmark. If $EDITOR is not
    set an editor's name should be passed.
    """
    _open_editor(url, editor)

@cli.command()
@click.argument('target', type=int)
def rm(target):
    """Remove target bookmark. Indexes are update after each deletion."""
    bookmarks = _load_data()
    try:
        bookmarks.pop(target)
        _save_data(bookmarks)
        click.echo('Removed.')
    except IndexError:
        raise click.ClickException('Bookmark not found')

@cli.command()
@click.option('--url-only', is_flag=True, help='Print only the bookmark\'s url.')
@click.option('--edit', is_flag=True, help='Open editor related to first foundbookmark. It is not possibile to specify an editor as argument.')
@click.argument('terms', nargs=-1)
def find(url_only, edit, terms):
    """Find a bookmark. Use doublequotes to search an exact match."""
    for i, bookmark in enumerate(_load_data()):
        for term in terms:
            if _match_bookmark(term, bookmark):
                if edit:
                   _open_editor(bookmark['url'], os.environ.get('EDITOR', 'vim'))
                   return
                if url_only:
                    click.echo(bookmark['url'])
                else:
                    click.echo(f'{i}# {bookmark}')

def _base_path():
    return os.environ.get('XDG_DATA_HOME', f'{os.environ["HOME"]}/.local/share')

def _data_path():
    path = f'{_base_path()}/bookmarks'
    if not os.path.exists(path):
        os.makedirs(path)
    return f'{path}/data.json'

def _load_data():
    try:
        with open(_data_path(), 'r+') as f:
            return json.load(f)
    except:
        return []

def _save_data(data):
    with open(_data_path(), 'w') as f:
        json.dump(sorted(data, key = lambda k: k['url']), f)

def _match_bookmark(query, bookmark):
    return query.lower() in bookmark['title'].lower() or \
            query.lower() in map(lambda t: t.lower(), bookmark['tags']) or \
            query.lower() in bookmark['url'].lower()

def _clean_tags(tags):
    tags = tags.split(',')
    if '' in tags:
        tags.remove('')
    return sorted(tags)

def _now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def _open_editor(url, editor):
    path = f'{_base_path()}/bookmarks'
    if not os.path.exists(path):
        os.makedirs(path)
    digested_url = hashlib.sha1(url.encode()).hexdigest()
    os.system(f'{editor} {path}/{digested_url}.md')

if __name__ == '__main__':
    cli()


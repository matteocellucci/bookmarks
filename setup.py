from setuptools import setup

setup(
    name='Bookmarks',
    version='1.0',
    py_modules=['bookmarks'],
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        bookmarks=bookmarks:cli
    '''
)

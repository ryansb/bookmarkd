# bookmarkd

A tool to convert IPython Notebooks to markdown and back.

    ## markdown -> notebook
    $ bookmarkd convert foo.md foo.ipynb
    ## notebook -> markdown, not done yet
    $ bookmarkd convert foo.ipynb foo.md

    # receive markdown via stdin
    $ bookmarkd convert - foo.ipynb
    # output notebook on stdout
    $ bookmarkd convert foo.md -

The conversion process isn't lossless. For example, the notebook cell numbers
and stored results aren't preserved.

# License

Bookmarkd is made available under the GNU Affero General Public License, see
LICENSE.txt for details.

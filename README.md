# bookmarkd

A tool to convert IPython Notebooks to markdown and back.

    ## notebook -> markdown
    $ bookmarkd md --output bar.md foo.ipynb
    ## markdown -> notebook
    $ bookmarkd ipynb --output baz.ipynb bar.md

The conversion process isn't lossless. For example, the notebook cell numbers
and stored results aren't preserved.

# License

Bookmarkd is made available under the GNU Affero General Public License, see
LICENSE.txt for details.

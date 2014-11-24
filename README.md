# bookmarkd

A tool to convert IPython Notebooks to markdown and back.

    ## markdown -> notebook
    $ bookmarkd convert foo.md foo.ipynb
    ## notebook -> markdown, not done yet
    $ bookmarkd convert foo.ipynb foo.md
    ## notebook -> markdown using nbconvert
    $ ipython nbconvert --to markdown foo.ipynb

    # receive markdown via stdin
    $ bookmarkd convert - foo.ipynb
    # output notebook on stdout
    $ bookmarkd convert foo.md -

The conversion process isn't lossless. For example, the notebook cell numbers
and stored results aren't preserved.

# Contributing

Please see the [Code of Conduct for contributors][CoC]. Pull requests are
welcome, but please include some docs, either in the README or in a --help
flag.


# License

Bookmarkd is made available under the [GNU Affero General Public
License][agpl], see [LICENSE.txt][license] for details.

[CoC]: https://github.com/ryansb/bookmarkd/blob/master/CONTRIBUTOR_CONDUCT.md
[agpl]: http://www.gnu.org/licenses/agpl.html
[license]: https://github.com/ryansb/bookmarkd/blob/master/LICENSE.txt

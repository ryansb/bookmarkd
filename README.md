# (note)book markd(own)

## Write markdown, use notebooks

With `bookmarkd` you can use any text editor you like to write markdown with
Python code blocks and render them as an IPython notebook.

This README can be converted to a notebook using the command
`bookmarkd convert README.md README.ipynb`

## Usage

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


Code blocks are converted to IPython notebook cells, and each markdown section between code blocks is made into a markdown cell in the notebook. To manually separate markdown into cells, separate blocks with horizontal rules (`---`).

The `--no-join-blocks` option will force each markdown block to become its own cell in the notebook.

---

Let's see some Python now!

    print "Hello World"

This is how blocks separated by `---` are rendered

---

They become separate markdown cells instead of being merged together.

Now let's see some more Python.

    print "Hello" + " " + "World"

# Contributing

Please see the [Code of Conduct for contributors][CoC]. Pull requests are
welcome, but please include some docs for your change. You can do this either
in the README or in `bookmarkd --help`.

[CoC]: https://github.com/ryansb/bookmarkd/blob/master/CONTRIBUTOR_CONDUCT.md

---

# License

Bookmarkd is made available under the [GNU Affero General Public
License][agpl], see [LICENSE.txt][license] for details.

[agpl]: http://www.gnu.org/licenses/agpl.html
[license]: https://github.com/ryansb/bookmarkd/blob/master/LICENSE.txt

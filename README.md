# (note)book markd(own)

## Write markdown, use notebooks

With `bookmarkd` you can use any text editor you like to write markdown with
Python code blocks and render them as an IPython notebook.

This README can be converted to a notebook using the command
`bookmarkd convert --join-blocks README.md README.ipynb`

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

There's also a `--join-blocks` option that will merge adjacent markdown blocks
if they aren't separated by a line with a horizontal rule (`---`).

Let's see some Python now!

    print "Hello World"

When you write multiple markdown blocks and separate them with a 
`---`

They will be rendered as separate markdown cells, but blocks that aren't
separated will just be merged nto the same cell.

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

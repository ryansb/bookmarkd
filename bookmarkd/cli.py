# -*- coding: utf8 -*-
"""
Copyright 2014 Ryan Brown <sb@ryansb.com>

This file is part of bookmarkd.

bookmarkd is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

bookmarkd is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with bookmarkd.  If not, see <http://www.gnu.org/licenses/>.
"""

from subprocess import Popen
from tempfile import NamedTemporaryFile

import click

from bookmarkd.version import __version__
from bookmarkd.to_notebook import to_notebook as md_to_nb


@click.group()
def cli():
    pass


@cli.command()
def version():
    click.echo("You are using bookmarkd version {}".format(__version__))
    click.echo("Get more information at "
               "https://github.com/ryansb/bookmarkd")


@cli.command(short_help="Do the conversion")
@click.option("--no-join-blocks", default=False, is_flag=True,
              help="join adjacent markdown blocks together instead of giving "
              "each their own cell. Blocks can be manually separated with "
              "horizontal rules (---)")
@click.argument("infile", type=click.File('rb'))
@click.argument("outfile", type=click.File('wb'))
def convert(no_join_blocks, infile, outfile):
    if infile.name.endswith('.md') or outfile.name.endswith('.ipynb'):
        pynb = md_to_nb(infile, hr_separated=(not no_join_blocks))
        outfile.write(pynb)
    elif infile.name.endswith('.ipynb') or outfile.name.endswith('.md'):
        args = ['ipython', 'nbconvert', '--to', 'markdown']
        if infile.name == '<stdin>':
            with NamedTemporaryFile('w', suffix='.ipynb', delete=False) as temp:
                args.append(temp.name)
                temp.write(infile.read())
        else:
            args.append(infile.name)
        if outfile.name == '<stdout>':
            args.append('--stdout')
        else:
            args.append('--output="{}"'.format(outfile.name.replace('.md', '')))

        p = Popen(args)
        p.wait()
    else:
        click.echo("One of the files (either in- or out-) "
                   "needs to have a .md or .ipynb suffix "
                   "so we know which way to convert.")

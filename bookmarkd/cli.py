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
@click.option("--joinblocks", default=False, is_flag=True)
@click.argument("infile", type=click.File('rb'))
@click.argument("outfile", type=click.File('wb'))
def convert(joinblocks, infile, outfile):
    if infile.name.endswith('.md') or outfile.name.endswith('.ipynb'):
        pynb = md_to_nb(infile, hr_separated=joinblocks)
        outfile.write(pynb)
    else:
        click.echo("Only markdown -> notebook conversion is "
                   "currently supported")

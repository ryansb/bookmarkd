# -*- coding: utf8 -*-
"""
Copyright 2015 Ryan Brown <sb@ryansb.com>

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

from StringIO import StringIO
from IPython.nbformat import current

from bookmarkd.to_notebook import tidy_notebook, to_notebook


def tidy_notebook_test():
    cells = [
        current.new_text_cell('markdown', ''),
        current.new_text_cell('code', '2 + 2'),
        current.new_text_cell('markdown', 'Hiya'),
        current.new_text_cell('markdown', ''),
        current.new_text_cell('code', '4 + 4'),
    ]
    assert len(cells) == 5
    new_cells = tidy_notebook(cells)
    assert len(new_cells) == 3


markdown_basic = """
# Hello there

This is a single-cell markdown notebook
"""


def markdown_basic_notebook_test():
    io = StringIO(markdown_basic)
    io.name = "fake.md"
    nb = to_notebook(io)
    print nb
    assert 3 == 4

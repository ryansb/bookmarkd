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

import json
from os.path import basename

import CommonMark as markdown
from IPython.nbformat import current


def to_notebook(infile):
    """Given markdown, returns an ipynb compliant JSON string"""

    parser = markdown.DocParser()
    ast = json.loads(markdown.ASTtoJSON(
        parser.parse(infile.read())))

    cells = []

    for block in ast.get('children', []):
        if block['t'] in ["IndentedCode", "FencedCode"]:
            cells.append(current.new_code_cell(block['string_content']))
        elif block['t'] in ['SetextHeader', 'ATXHeader']:
            cells.append(current.new_text_cell(
                'markdown',
                '#' * block.get('level', 1) + ' ' + ''.join(block['strings']))
            )
        elif block['t'] in ['HorizontalRule']:
            # We don't render horizontal rules
            pass
        else:
            cells.append(current.new_text_cell(
                'markdown',
                '\n'.join(block['strings']))
            )

    worksheet = current.new_worksheet(cells=cells)

    nb = current.new_notebook(
        basename(infile.name).split('.')[:-1],
        worksheets=[worksheet]
    )

    # using the indent option leaves a bunch of trailing whitespace. No thanks!
    return json.dumps(nb, indent=2).replace(' \n', '\n')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

__copyright__="""
    pySART - Simplified AUTOSAR-Toolkit for Python.

   (C) 2021 by Christoph Schueler <github.com/Christoph2,
                                        cpu12.gems@googlemail.com>

   All Rights Reserved

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

import argparse
from pathlib import Path
import pathlib
import sys

from pya2l import DB

def main():
    parser = argparse.ArgumentParser(description = 'Import/export from/to a2l(db) files.')
#    parser.add_argument("a2ldb_file", help = "File to import/export.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-i", "--import", help = "A2L file to import", dest = "ifn", type = str, metavar = "A2L_file")
    group.add_argument("-e", "--export", help = "A2LDB file to export", dest = "efn", type = str, metavar = "DB_file")

    parser.add_argument("-k", dest = 'keepDirectory', action = "store_true", default = False,
        help = "keep directory; otherwise create db in current directory")
    parser.add_argument("-l", help = "loglevel [warn | info | error | debug]", dest = "loglevel", type = str, default = "info")
    parser.add_argument("-f", "--force-overwrite", help = "Force overwrite of existing file", default = False, action = "store_true")

    args = parser.parse_args()
    #print(args)
    if not (args.ifn or args.efn):
       print("Either -i or -e option is required.")
       sys.exit(2)
    db = DB()

    if args.efn:
        efn = Path(args.efn)
        session = db
        session = db.open_existing(efn)
        db.export_a2l(sys.stdout)
    else:
        ifn = Path(args.ifn)
        session = db.import_a2l(ifn)

#    if not a2ldb_file.exists():
#        raise RuntimeError("file '{}' does not exist.".format(a2ldb_file))


if __name__ == '__main__':
    main()

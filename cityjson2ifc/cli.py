"""Command Line Interface (cli.py)
Copyright 2023 3DGI <info@3dgi.nl>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import sys
import warnings
import gc

import click
from cjio import errors, cityjson, cjio

from cityjson2ifc import convert

cityjson.CITYJSON_VERSIONS_SUPPORTED = ['1.1',]


def main(infile, outfile, ignore_duplicate_keys):
    click.echo("Parsing %s" % infile.name)
    if infile.name == "<stdin>":
        cm = cityjson.read_stdin()
    else:
        try:
            cm = cityjson.reader(file=infile, ignore_duplicate_keys=ignore_duplicate_keys)
        except ValueError as e:
            raise click.ClickException('%s: "%s".' % (e, infile))
        except IOError as e:
            raise click.ClickException('Invalid file: "%s".\n%s' % (infile, e))

    try:
        with warnings.catch_warnings(record=True) as w:
            cm.check_version()
            cjio._print_cmd(w)
    except errors.CJInvalidVersion as e:
        raise click.ClickException(e.msg)

    # Dereference the CityJSON geometry boundaries so that they store the
    # coordinates instead of vertex indices
    cm.load_from_j()
    # TODO: Remove duplicate data from the citymodel (need to be fixed in cjio)
    cm.j["CityObjects"] = {}
    gc.collect()

    click.echo("Converting to IFC")
    collection = None
    click.echo("Writing to %s" % outfile.name)
    outfile.write("")


@click.command(name="main")
@click.version_option()
@click.argument("infile", type=click.File("r"), default=sys.stdin)
@click.argument("outfile", type=click.File("w", lazy=True))
@click.option('--ignore_duplicate_keys', is_flag=True, help='Load a CityJSON file even if some City Objects have the same IDs (technically invalid file).')
def main_cmd(infile, outfile, ignore_duplicate_keys):
    """A command line tool for converting CityJSON files to IFC format.

        INFILE – Path to a CityJSON file\n
        OUTFILE – Path to the IFC file to write
    """
    main(infile, outfile, ignore_duplicate_keys)

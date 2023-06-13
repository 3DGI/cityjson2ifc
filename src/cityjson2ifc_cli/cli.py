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

from cityjson2ifc_cli import convert


def load_cityjson(infile, ignore_duplicate_keys):
    if infile.name == "<stdin>":
        cm = cityjson.read_stdin()
    else:
        try:
            cm = cityjson.reader(file=infile,
                                 ignore_duplicate_keys=ignore_duplicate_keys)
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
    if cm.get_version() != "1.1":
        click.echo("Upgrading CityJSON to v1.1")
        re, reasons = cm.upgrade_version("1.1", digit=4)
        if (re == False):
            click.echo("WARNING: %s" % (reasons))
    # Dereference the CityJSON geometry boundaries so that they store the
    # coordinates instead of vertex indices
    cm.cityobjects = dict()
    cm.load_from_j(transform=False)
    # Remove duplicate data from the citymodel (need to be fixed in cjio)
    cm.j["CityObjects"] = {}
    gc.collect()
    return cm


def main(infile, outfile, ignore_duplicate_keys=None,
         lod_split=None, lod_select=None,
         name_entity=None, name_project=None, name_site=None,
         name_person_family=None, name_person_given=None
         ):
    click.echo("Parsing %s" % infile.name)
    cm = load_cityjson(infile, ignore_duplicate_keys)

    click.echo("Converting to IFC")
    convert.cityjson2ifc(cm=cm, file_destination=str(outfile), lod_split=lod_split,
                         lod_select=lod_select, name_entity=name_entity,
                         name_project=name_project, name_site=name_site,
                         name_person_family=name_person_family,
                         name_person_given=name_person_given)
    click.echo("Written file to %s" % outfile.name)


@click.command(name="main")
@click.version_option()
@click.argument("infile", type=click.File("r"), default=sys.stdin)
@click.argument("outfile", type=click.File("w", lazy=True))
@click.option('--ignore_duplicate_keys', is_flag=True,
              help='Load a CityJSON file even if some City Objects have the same IDs (technically invalid file).')
@click.option('--lod-split', is_flag=True,
              help='Split the CityJSON file per LoD, writing a separate IFC file for each LoD.')
@click.option('--lod-select', type=str,
              help='Select the LoD that should be converted to IFC.')
@click.option('--name-entity', type=str,
              help='The CityObject attribute that should be used for the entity name.')
@click.option('--name-project', type=str, help='Set the IfcProject name.')
@click.option('--name-site', type=str, help='Set the IfcSite name.')
@click.option('--name-person-family', type=str, help='Set the IfcPerson family name.')
@click.option('--name-person-given', type=str, help='Set the IfcPerson given name.')
def main_cmd(infile, outfile, ignore_duplicate_keys, lod_split, lod_select,
             name_entity, name_project, name_site, name_person_family,
             name_person_given):
    """A command line tool for converting CityJSON files to IFC format.

        INFILE – Path to a CityJSON file\n
        OUTFILE – Path to the IFC file to write
    """
    main(infile, outfile, ignore_duplicate_keys=ignore_duplicate_keys,
         lod_split=lod_split, lod_select=lod_select, name_entity=name_entity,
         name_project=name_project, name_site=name_site,
         name_person_family=name_person_family, name_person_given=name_person_given
         )

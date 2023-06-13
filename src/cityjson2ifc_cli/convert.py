# cityjson2ifc - Python CityJSON to IFC converter
# Copyright (C) 2023 3DGI <info@3dgi.nl>
#
# This file is part of cityjson2ifc.
#
# cityjson2ifc is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cityjson2ifc is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with cityjson2ifc.  If not, see <http://www.gnu.org/licenses/>.

from ifccityjson.cityjson2ifc import Cityjson2ifc


def cityjson2ifc(cm, file_destination, name_entity=None,
                 lod_split=None, lod_select=None, name_project=None, name_site=None,
                 name_person_family=None, name_person_given=None):
    converter = Cityjson2ifc()
    converter.configuration(file_destination=file_destination, split=lod_split,
                            lod=lod_select,
                            name_attribute=name_entity,
                            name_project=name_project,
                            name_site=name_site,
                            name_person_family=name_person_family,
                            name_person_given=name_person_given)
    converter.convert(city_model=cm)

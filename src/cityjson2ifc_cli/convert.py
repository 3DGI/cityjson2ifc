"""Converter module (convert.py)
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

from ifccityjson.cityjson2ifc.cityjson2ifc import Cityjson2ifc

def convert(data, city_model):

    converter = Cityjson2ifc()
    converter.configuration(**data)
    converter.convert(city_model)
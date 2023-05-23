# CityJSON to IFC

*A command line tool for converting CityJSON files to IFC format.*



## Installation

Required python: >= 3.8

Additionally, you need a relatively new version of `pip` and `setuptools` that supports building from `pyproject.toml` files.

You can install *cityjson2ifc* with pip.

```shell
pip install cityjson2ifc
```

## Usage

Convert a single CityJSON file to IFC.

```shell
cityjson2ifc <input.city.json> <output.ifc>
```

See the help menu and the tool version

```shell
cityjson2ifc --help
cityjson2ifc --version
```

### Pipe from cjio

[cjio]() is a CLI tool for manipulating 3D city models that are stored in CityJSON files.
You can pipe cjio's output directly into *cityjson2ifc* without saving an intermedate file.
This is particularly useful if you want to modify the citymodel before the conversion.
For instance, upgrade the CityJSON file to v1.1 and then convert it to IFC.

```shell
cjio --suppress_msg <input.city.json> upgrade save stdout | cityjson2ifc - <output.ifc>
```

## Limitations



## Converted data



## CityJSON --> IFC conversion table


## Communication

All work takes place in the current GitHub repository.
The primary channel for communication is the [GitHub Discussions](https://github.com/3DGI/cityjson2ifc/discussions).
Feel free to ask questions you’re wondering about, share ideas and engage with other community members.

## Contributing

Contributions to the project are very welcome!
You could help with testing, documentation, bug reports, bug fixes, implementing new features and more.
Please read the [CONTRIBUTING.md](https://github.com/3DGI/cityjson2jsonfg/blob/master/CONTRIBUTING.md) on how to get started.

## Funding

Version 1.0 was funded by the [Dutch Kadaster](https://www.kadaster.nl/).
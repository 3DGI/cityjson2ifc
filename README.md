# CityJSON to IFC

*A command line tool for converting CityJSON files to IFC format.*

Supported versions:

- CityJSON v1.1
- IFC 4

## Installation

Download and install the executable for your platform from one of the [releases](https://github.com/3DGI/cityjson2ifc/releases).

Alternatively, you can install with pip.

### Install with pip

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

- CityJSON extensions are not supported (except the *GenericCityObject*)
- The following CityJSON geometry types are not supported, `Solid: interior shell`, `GeometryInstance`.

## CityJSON --> IFC conversion table

| **CityJSON**                | **IFC**                 | **IFC attributes**                                                |
|:----------------------------|:------------------------|:------------------------------------------------------------------|
| Building                    | IfcBuilding             |                                                                   |
| BuildingPart                | IfcBuilding             | CompositionType: PARTIAL                                          |
| BuildingInstallation        | IfcBuildingElementProxy |                                                                   |
| BuildingConstructiveElement | IfcBuildingElementProxy |                                                                   |
| BuildingFurniture           | IfcFurniture            |                                                                   |
| BuildingStorey              | IfcBuildingStorey       | CompositionType: PARTIAL                                          |
| BuildingRoom                | IfcSpace                | CompositionType: ELEMENT                                          |
| BuildingUnit                | IfcSpace                | CompositionType: ELEMENT                                          |
| Road                        | IfcCivilElement         |                                                                   |
| Railway                     | IfcCivilElement         |                                                                   |
| TransportationSquare        | IfcCivilElement         |                                                                   |
| TINRelief                   | IfcGeographicElement    | PredefinedType: TERRAIN                                           |
| WaterBody                   | IfcGeographicElement    | PredefinedType: USERDEFINED, ObjectType: WaterBody                |
| LandUse                     | IfcGeographicElement    | PredefinedType: USERDEFINED, ObjectType: LandUse                  |
| PlantCover                  | IfcGeographicElement    | PredefinedType: USERDEFINED, ObjectType: Plantcover               |
| SolitaryVegetationObject    | IfcGeographicElement    | PredefinedType: USERDEFINED, ObjectType: SolitaryVegetationObject |
| CityFurniture               | IfcFurnishingElement    |                                                                   |
| OtherConstruction           | IfcCivilElement         |                                                                   |
| +GenericCityObject          | IfcCivilElement         |                                                                   |
| Bridge                      | IfcCivilElement         |                                                                   |
| BridgePart                  | IfcCivilElement         |                                                                   |
| BridgeInstallation          | IfcCivilElement         |                                                                   |
| BridgeConstructiveElement   | IfcCivilElement         |                                                                   |
| BridgeRoom                  | IfcCivilElement         |                                                                   |
| BridgeFurniture             | IfcCivilElement         |                                                                   |
| Tunnel                      | IfcCivilElement         |                                                                   |
| TunnelPart                  | IfcCivilElement         |                                                                   |
| TunnelInstallation          | IfcCivilElement         |                                                                   |
| TunnelConstructiveElement   | IfcCivilElement         |                                                                   |
| TunnelHollowSpace           | IfcCivilElement         |                                                                   |
| TunnelFurniture             | IfcCivilElement         |                                                                   |
| CityObjectGroup             | IfcBuilding             |                                                                   |
| GroundSurface               | IfcSlab                 | PredefinedType: BASESLAB                                          |
| RoofSurface                 | IfcRoof                 |                                                                   |
| WallSurface                 | IfcWall                 |                                                                   |
| ClosureSurface              | IfcSpace                |                                                                   |
| OuterCeilingSurface         | IfcCovering             | PredefinedType: CEILING                                           |
| OuterFloorSurface           | IfcSlab                 | PredefinedType: FLOOR                                             |
| Window                      | IfcWindow               |                                                                   |
| Door                        | IfcDoor                 |                                                                   |
| InteriorWallSurface         | IfcWall                 |                                                                   |
| CeilingSurface              | IfcCovering             | PredefinedType: CEILING                                           |
| FloorSurface                | IfcSlab                 | PredefinedType: FLOOR                                             |
| WaterSurface                | IfcGeographicElement    | PredefinedType: USERDEFINED, ObjectType: WaterSurface             |
| WaterGroundSurface          | IfcGeographicElement    | PredefinedType: USERDEFINED, ObjectType: WaterGroundSurface       |
| WaterClosureSurface         | IfcGeographicElement    | PredefinedType: USERDEFINED, ObjectType: WaterClosureSurface      |
| TrafficArea                 | IfcCivilElement         |                                                                   |
| AuxiliaryTrafficArea        | IfcCivilElement         |                                                                   |
| TransportationMarking       | IfcCivilElement         |                                                                   |
| TransportationHole          | IfcCivilElement         |                                                                   |


## Communication

All work takes place in the current GitHub repository.
The primary channel for communication is the [GitHub Discussions](https://github.com/3DGI/cityjson2ifc/discussions).
Feel free to ask questions you’re wondering about, share ideas and engage with other community members.

## Contributing

Contributions to the project are very welcome!
You could help with testing, documentation, bug reports, bug fixes, implementing new features and more.
Please read the [CONTRIBUTING.md](https://github.com/3DGI/cityjson2jsonfg/blob/master/CONTRIBUTING.md) on how to get started.

## Credits

*cityjson2ifc* is a CLI that wraps the code that was developed by Laurens Oostwegel in 2021, [as part of IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.7.0/src/ifccityjson).

## Funding

Version 1.0 was funded by the [Dutch Kadaster](https://www.kadaster.nl/).
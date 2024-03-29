# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/attribuutit/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([1da0d3fe ...](https://git.sr.ht/~sthagen/attribuutit/blob/default/etc/sbom/cdx.json.sha256 "sha256:1da0d3fe4dd28c9dfab886e618ff0dbdc2c68cc92945f1a90542e35ca1c987e8")).
<!--[[[end]]] (checksum: 74050bac6454d95e9e04c7d1faeefdd3)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                          | Version                                            | License                                                 | Author            | Description (from packaging data)                                  |
|:--------------------------------------------------------------|:---------------------------------------------------|:--------------------------------------------------------|:------------------|:-------------------------------------------------------------------|
| [geotiff](https://github.com/Open-Source-Agriculture/geotiff) | [0.2.10](https://pypi.org/project/geotiff/0.2.10/) | GNU Lesser General Public License v2 or later (LGPLv2+) | Kipling Crossing  | A noGDAL tool for reading and writing geotiff files                |
| [pyshp](https://github.com/GeospatialPython/pyshp)            | [2.3.1](https://pypi.org/project/pyshp/2.3.1/)     | MIT                                                     | Joel Lawhead      | Pure Python read/write support for ESRI Shapefile format           |
| [typer](https://github.com/tiangolo/typer)                    | [0.9.0](https://pypi.org/project/typer/0.9.0/)     | MIT License                                             | Sebastián Ramírez | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 19e8f6379fe37dfee5d4286900cf1d0c)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                      | Version                                                   | License                              | Author                                      | Description (from packaging data)                                                          |
|:----------------------------------------------------------|:----------------------------------------------------------|:-------------------------------------|:--------------------------------------------|:-------------------------------------------------------------------------------------------|
| [asciitree](http://github.com/mbr/asciitree)              | [0.3.3](https://pypi.org/project/asciitree/0.3.3/)        | MIT                                  | Marc Brinkmann                              | Draws ASCII trees.                                                                         |
| [certifi](https://github.com/certifi/python-certifi)      | [2023.5.7](https://pypi.org/project/certifi/2023.5.7/)    | Mozilla Public License 2.0 (MPL 2.0) | Kenneth Reitz                               | Python package for providing Mozilla's CA Bundle.                                          |
| [click](https://palletsprojects.com/p/click/)             | [8.1.5](https://pypi.org/project/click/8.1.5/)            | BSD License                          | Pallets <contact@palletsprojects.com>       | Composable command line interface toolkit                                                  |
| [entrypoints](https://github.com/takluyver/entrypoints)   | [0.4](https://pypi.org/project/entrypoints/0.4/)          | MIT License                          | Thomas Kluyver                              | Discover and load entry points from installed packages.                                    |
| [fasteners](https://github.com/harlowja/fasteners)        | [0.18](https://pypi.org/project/fasteners/0.18/)          | Apache Software License              | Joshua Harlow                               | A python package that provides useful locks                                                |
| [numcodecs](https://github.com/zarr-developers/numcodecs) | [0.11.0](https://pypi.org/project/numcodecs/0.11.0/)      | MIT License                          | Alistair Miles                              | A Python package providing buffer compression and transformation codecs for use            |
| [numpy](https://www.numpy.org)                            | [1.25.1](https://pypi.org/project/numpy/1.25.1/)          | BSD License                          | Travis E. Oliphant et al.                   | Fundamental package for array computing in Python                                          |
| [pyproj](https://github.com/pyproj4/pyproj)               | [3.6.0](https://pypi.org/project/pyproj/3.6.0/)           | MIT License                          | Jeff Whitaker <jeffrey.s.whitaker@noaa.gov> | Python interface to PROJ (cartographic projections and coordinate transformations library) |
| [tifffile](https://www.lfd.uci.edu/~gohlke/)              | [2022.4.26](https://pypi.org/project/tifffile/2022.4.26/) | BSD License                          | Christoph Gohlke                            | Read and write TIFF files                                                                  |
| [zarr](https://github.com/zarr-developers/zarr-python)    | [2.12.0](https://pypi.org/project/zarr/2.12.0/)           | MIT License                          | Alistair Miles                              | An implementation of chunked, compressed, N-dimensional arrays for Python.                 |
<!--[[[end]]] (checksum: 17d0f203c1eb222cc0c0bbab5075481a)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
geotiff==0.2.10
├── numpy [required: Any, installed: 1.25.1]
├── pyproj [required: Any, installed: 3.6.0]
│   └── certifi [required: Any, installed: 2023.5.7]
├── tifffile [required: >=2021.7.4,!=2022.4.28, installed: 2022.4.26]
│   └── numpy [required: >=1.19.2, installed: 1.25.1]
└── zarr [required: >=2.12.0,<2.13, installed: 2.12.0]
    ├── asciitree [required: Any, installed: 0.3.3]
    ├── fasteners [required: Any, installed: 0.18]
    ├── numcodecs [required: >=0.6.4, installed: 0.11.0]
    │   ├── entrypoints [required: Any, installed: 0.4]
    │   └── numpy [required: >=1.7, installed: 1.25.1]
    └── numpy [required: >=1.7, installed: 1.25.1]
pyshp==2.3.1
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.5]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: d18b5c1ba3a14447e3820ec1a8f91612)-->

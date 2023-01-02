# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/attribuutit/blob/default/sbom.json) with SHA256 checksum ([e4dc8714 ...](https://git.sr.ht/~sthagen/attribuutit/blob/default/sbom.json.sha256 "sha256:e4dc87147271ebc10df679dfded5165e53ab9ac11b6aa902472a38479fa8f13c")).
<!--[[[end]]] (checksum: a166952f221dc70b437efc7d66c37572)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                          | Version                                          | License                                                 | Author            | Description (from packaging data)                                  |
|:--------------------------------------------------------------|:-------------------------------------------------|:--------------------------------------------------------|:------------------|:-------------------------------------------------------------------|
| [geotiff](https://github.com/Open-Source-Agriculture/geotiff) | [0.2.7](https://pypi.org/project/geotiff/0.2.7/) | GNU Lesser General Public License v2 or later (LGPLv2+) | Kipling Crossing  | A noGDAL tool for reading and writing geotiff files                |
| [pyshp](https://github.com/GeospatialPython/pyshp)            | [2.3.1](https://pypi.org/project/pyshp/2.3.1/)   | MIT                                                     | Joel Lawhead      | Pure Python read/write support for ESRI Shapefile format           |
| [typer](https://github.com/tiangolo/typer)                    | [0.7.0](https://pypi.org/project/typer/0.7.0/)   | MIT License                                             | Sebastián Ramírez | Typer, build great CLIs. Easy to code. Based on Python type hints. |
<!--[[[end]]] (checksum: 53e0bff08dc8a28dfb2c7073b72bb8d9)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                           | Version                                                   | License                              | Author                    | Description (from packaging data)                                                          |
|:-------------------------------------------------------------------------------|:----------------------------------------------------------|:-------------------------------------|:--------------------------|:-------------------------------------------------------------------------------------------|
| [asciitree](http://github.com/mbr/asciitree)                                   | [0.3.3](https://pypi.org/project/asciitree/0.3.3/)        | MIT                                  | Marc Brinkmann            | Draws ASCII trees.                                                                         |
| [certifi](https://github.com/certifi/python-certifi)                           | [2022.12.7](https://pypi.org/project/certifi/2022.12.7/)  | Mozilla Public License 2.0 (MPL 2.0) | Kenneth Reitz             | Python package for providing Mozilla's CA Bundle.                                          |
| [click](https://palletsprojects.com/p/click/)                                  | [8.1.3](https://pypi.org/project/click/8.1.3/)            | BSD License                          | Armin Ronacher            | Composable command line interface toolkit                                                  |
| [entrypoints](https://github.com/takluyver/entrypoints)                        | [0.4](https://pypi.org/project/entrypoints/0.4/)          | MIT License                          | Thomas Kluyver            | Discover and load entry points from installed packages.                                    |
| [fasteners](https://github.com/harlowja/fasteners)                             | [0.18](https://pypi.org/project/fasteners/0.18/)          | Apache Software License              | Joshua Harlow             | A python package that provides useful locks                                                |
| [numcodecs](https://github.com/zarr-developers/numcodecs/blob/main/README.rst) | [0.11.0](https://pypi.org/project/numcodecs/0.11.0/)      | MIT License                          | Alistair Miles            | A Python package providing buffer compression and transformation codecs for use            |
| [numpy](https://www.numpy.org)                                                 | [1.24.0](https://pypi.org/project/numpy/1.24.0/)          | BSD License                          | Travis E. Oliphant et al. | Fundamental package for array computing in Python                                          |
| [pyproj](https://github.com/pyproj4/pyproj)                                    | [3.4.1](https://pypi.org/project/pyproj/3.4.1/)           | MIT License                          | Jeff Whitaker             | Python interface to PROJ (cartographic projections and coordinate transformations library) |
| [tifffile](https://www.lfd.uci.edu/~gohlke/)                                   | [2022.4.26](https://pypi.org/project/tifffile/2022.4.26/) | BSD License                          | Christoph Gohlke          | Read and write TIFF files                                                                  |
| [zarr](https://github.com/zarr-developers/zarr-python)                         | [2.13.3](https://pypi.org/project/zarr/2.13.3/)           | MIT License                          | Alistair Miles            | An implementation of chunked, compressed, N-dimensional arrays for Python.                 |
<!--[[[end]]] (checksum: 74195b025093f70731c3aa4c7828f577)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
geotiff==0.2.7
  - numpy [required: Any, installed: 1.24.0]
  - pyproj [required: Any, installed: 3.4.1]
    - certifi [required: Any, installed: 2022.12.7]
  - tifffile [required: >=2021.7.2,<2022.4.28, installed: 2022.4.26]
    - numpy [required: >=1.19.2, installed: 1.24.0]
  - zarr [required: >=2.10.*, installed: 2.13.3]
    - asciitree [required: Any, installed: 0.3.3]
    - fasteners [required: Any, installed: 0.18]
    - numcodecs [required: >=0.10.0, installed: 0.11.0]
      - entrypoints [required: Any, installed: 0.4]
      - numpy [required: >=1.7, installed: 1.24.0]
    - numpy [required: >=1.7, installed: 1.24.0]
pyshp==2.3.1
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 5a2d73d80a8c1c37f241f1f4cd4cd5b1)-->

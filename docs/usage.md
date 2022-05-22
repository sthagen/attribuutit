# Usage

## Example 

### Help

```console
❯ attribuutit --help
Usage: attribuutit [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  eject    Eject an example configuration in JSON format with stem equal...
  inspect  Inspect the file at path and persist the report eventually.
  scan     Scan the file system based on the configuration given in...
```

### Inspect GeoTIFF

```console
❯ attribuutit inspect GRAY_50M_SR_OB.tif
Real run inspecting file at GRAY_50M_SR_OB.tif
crs_name: WGS_84 (code 4326)
bbox: ((-179.99999999999997, 90.0), (179.99999999996405, -89.99999999998201))
```

### Inspect Shape File

```console
❯ attribuutit inspect ne_110m_admin_0_tiny_countries.shp
Real run inspecting file at ne_110m_admin_0_tiny_countries.shp
upstream: POINT =?= POINT :downstream
#features: 37
bbox: [-175.23533295466754, -54.274478863695265, 179.20397422623353, 71.02824880643254]
geojson: {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'properties': {'scalerank': 1, ...
# - - - 8< - - -
'geometry': {'type': 'Point', 'coordinates': (-36.792143407672654, -54.274478863695265)}}], 
'bbox': [-175.23533295466754, -54.274478863695265, 179.20397422623353, 71.02824880643254]}
shapefile Reader
    37 shapes (type 'POINT')
    37 records (171 fields)
```

### Inspect VPF File

```console
❯ attribuutit inspect lat
Real run inspecting file at lat
{
  "error": false,
  "error_detail": "",
  "byte_order": "little",
  "byte_order_explicit": true,
  "header_length": 268,
  "header_byte_offset": 5,
  "table_description": "Library Attribute (Extent) Table",
  "narrative_table_name": "-",
  "columns": {
    "id": {
      "column_rank": 1,
      "column_name": "id",
      "field_type": "I",
      "field_length": 1,
      "key_type": "P",
      "column_textual_description": "Row Identifier",
      "optional_value_description_table_name": "-",
      "optional_thematic_index_name": "-",
      "optional_column_narrative_table_name": "-"
    },
# - - - 8< - - -
    "ymax": {
      "column_rank": 6,
      "column_name": "ymax",
      "field_type": "F",
      "field_length": 1,
      "key_type": "N",
      "column_textual_description": "Northernmost latitude",
      "optional_value_description_table_name": "-",
      "optional_thematic_index_name": "-",
      "optional_column_narrative_table_name": "-"
    }
  }
}
```

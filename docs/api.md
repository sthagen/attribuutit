# API

## Module

Example use of the vpf module to read the table description from a Vector Product Format (VPF) table:

```python
import attribuutit.vpf as vpf

artifact = vpf.Table('path/to/vpf-table')
print(artifact.table['table_description'])
```

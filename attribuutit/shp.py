import pathlib
from typing import no_type_check

import shapefile  # type: ignore


@no_type_check
def shape_type(code: int) -> str:
    """Look up the name (code) from the integer code reported by shapefile or UNKNOWN"""
    shape_type_map = {
        -1: 'UNKNOWN',
        0: 'NULL',
        1: 'POINT',
        3: 'POLYLINE',
        5: 'POLYGON',
        8: 'MULTIPOINT',
        11: 'POINTZ',
        13: 'POLYLINEZ',
        15: 'POLYGONZ',
        18: 'MULTIPOINTZ',
        21: 'POINTM',
        23: 'POLYLINEM',
        25: 'POLYGONM',
        28: 'MULTIPOINTM',
        31: 'MULTIPATCH',
    }
    name = shape_type_map.get(code)
    return name if name else shape_type_map[-1]


@no_type_check
def load(path: pathlib.Path):
    """Load the shape file at path."""
    error = ''
    with shapefile.Reader(path) as shape:
        shape_type_name = shape_type(shape.shapeType)
        upstream_name = shape.shapeTypeName
        feature_count = len(shape)
        bounding_box = shape.bbox
        try:
            geo_json = shape.__geo_interface__
        except shapefile.ShapefileException as err:
            geo_json = None
            error = f'problem reading database of shape for {path} with {err}'

    return error, {
        'folder_path': str(path.parent),
        'file_name': path.name,
        'file_suffixes': path.suffixes,
        'shape_type_name': shape_type_name,
        'feature_count': feature_count,
        'bounding_box': bounding_box,
        'has_geo_json': bool(geo_json),
        'geo_json_type': geo_json.get('type', None) if geo_json else None,
    }


@no_type_check
def summary(shp_model, full_path=False):
    """Summarize the shapefile model as single line string."""
    path_shown = pathlib.Path(shp_model['folder_path']) / shp_model['file_name'] if full_path else shp_model['file_name']
    return (
        f"{path_shown} ->"
        f" {shp_model['geo_json_type'] if shp_model['has_geo_json'] else shp_model['shape_type_name']}"
        f"/{shp_model['feature_count']} within {shp_model['bounding_box']}"
    )

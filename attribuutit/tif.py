import pathlib
from typing import no_type_check

from geotiff import GeoTiff  # type: ignore


@no_type_check
def load(path: pathlib.Path):
    """Load the GeoTIFF file at path."""
    error = ''
    try:
        geo_tiff = GeoTiff(str(path))  # Consider contributing upstream as neither pathlib nor context manager support there
        crs_code = geo_tiff.crs_code.value
        crs_name = geo_tiff.crs_code.name
        bounding_box = geo_tiff.tif_bBox
    except BaseException as err:
        error = f'problem reading GeoTIFF from {path} with {err}'

    return error, {
        'folder_path': str(path.parent),
        'file_name': path.name,
        'file_suffixes': path.suffixes,
        'crs_name': crs_name,
        'crs_code': crs_code,
        'bounding_box': [coord for point in bounding_box for coord in point],
    }


@no_type_check
def summary(tif_model, full_path=False):
    """Summarize the TIFF file model as single line string."""
    path_disp = pathlib.Path(tif_model['folder_path']) / tif_model['file_name'] if full_path else tif_model['file_name']
    return (
        f'{path_disp} ->'
        f" CRS {tif_model['crs_name']} ({tif_model['crs_code']})"
        f" within {tif_model['bounding_box']}"
    )

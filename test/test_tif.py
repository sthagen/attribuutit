import pathlib

import attribuutit.tif as tif

TIF_ROOT = pathlib.Path('local', 'incoming')


def test_tif_load(capsys):
    path = TIF_ROOT / 'GRAY_50M_SR_OB.tif'
    error, result = tif.load(path)
    assert not error
    assert result['crs_name'] == 'WGS_84'
    assert result['crs_code'] == 4326
    bbox = result['bounding_box']
    assert len(bbox) == 4
    assert bbox[0] <= bbox[2]
    assert bbox[1] >= bbox[3]
    assert -180 <= bbox[0] <= 180
    assert -180 <= bbox[2] <= 180
    assert -90 <= bbox[1] <= 90
    assert -90 <= bbox[3] <= 90
    out, err = capsys.readouterr()
    assert not out
    assert not err

import pathlib

import attribuutit.shp as shp

SHP_ROOT = pathlib.Path('local', 'incoming')


def test_shp_load(capsys):
    path = SHP_ROOT / 'ne_110m_admin_0_tiny_countries.shp'
    error, result = shp.load(path)
    assert not error
    assert result['feature_count'] == 37
    assert result['geo_json_type'] == 'FeatureCollection'
    bbox = result['bounding_box']
    assert len(bbox) == 4
    assert bbox[0] <= bbox[2]
    assert bbox[1] <= bbox[3]
    assert -180 <= bbox[0] <= 180
    assert -180 <= bbox[2] <= 180
    assert -90 <= bbox[1] <= 90
    assert -90 <= bbox[3] <= 90
    out, err = capsys.readouterr()
    assert not out
    assert not err

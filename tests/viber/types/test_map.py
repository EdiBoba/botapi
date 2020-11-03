def test_map_serialize(map_obj):
    expected = {
        'Latitude': '37.7898',
        'Longitude': '-122.3942',
        'min_api_version': 6
    }
    assert map_obj.serialize(add_min_api_ver=True) == expected

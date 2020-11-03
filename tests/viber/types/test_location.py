def test_to_dict(location_obj):
    expected = {
        'lat': '37.7898',
        'lon': '-122.3942'
    }
    assert location_obj.serialize() == expected

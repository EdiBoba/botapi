from botapi.viber.types import LocationMessage


def test_to_dict(location_obj):
    obj = LocationMessage(location_obj, 'tracking data')
    expected = {
        'type': 'location',
        'min_api_version': 1,
        'tracking_data': 'tracking data',
        'location': {
            'lat': '37.7898',
            'lon': '-122.3942'
        }
    }
    assert obj.serialize(add_min_api_ver=True) == expected

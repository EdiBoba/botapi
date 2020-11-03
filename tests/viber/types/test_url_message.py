from botapi.viber.types import UrlMessage


def test_url_message_serialize():
    obj = UrlMessage('http://www.website.com/go_here', 'tracking data')
    expected = {
        'type': 'url',
        'min_api_version': 1,
        'tracking_data': 'tracking data',
        'media': 'http://www.website.com/go_here'
    }
    assert obj.serialize(add_min_api_ver=True) == expected

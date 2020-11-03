from botapi.viber.types import TextMessage


def test_text_message_serialize():
    obj = TextMessage('Hello world!', 'tracking data')
    expected = {
        'min_api_version': 1,
        'tracking_data': 'tracking data',
        'type': 'text',
        'text': 'Hello world!'
    }
    assert obj.serialize(add_min_api_ver=True) == expected

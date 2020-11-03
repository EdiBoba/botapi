from botapi.viber.types import StickerMessage


def test_sticker_message_serialize():
    obj = StickerMessage(46105, 'tracking data')
    expected = {
        'min_api_version': 1,
        'tracking_data': 'tracking data',
        'type': 'sticker',
        'sticker_id': 46105
    }
    assert obj.serialize(add_min_api_ver=True) == expected

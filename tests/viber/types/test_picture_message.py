from botapi.viber.types import PictureMessage


def test_pic_message_serialize():
    obj = PictureMessage(
        text='Photo description',
        media='http://www.images.com/img.jpg',
        thumbnail='http://www.images.com/thumb.jpg',
        tracking_data='tracking data'
    )
    expected = {
        'min_api_version': 1,
        'tracking_data': 'tracking data',
        'type': 'picture',
        'text': 'Photo description',
        'media': 'http://www.images.com/img.jpg',
        'thumbnail': 'http://www.images.com/thumb.jpg'
    }
    assert obj.serialize(add_min_api_ver=True) == expected

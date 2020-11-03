from botapi.viber.types import FileMessage


def test_file_message_serialize():
    obj = FileMessage(
        media='http://www.images.com/file.doc',
        size=10000,
        file_name='name_of_file.doc',
        tracking_data='tracking data'
    )
    expected = {
        'min_api_version': 1,
        'tracking_data': 'tracking data',
        'type': 'file',
        'media': 'http://www.images.com/file.doc',
        'size': 10000,
        'file_name': 'name_of_file.doc'
    }
    assert obj.serialize(add_min_api_ver=True) == expected

from botapi.viber.types import RichMediaMessage


def test_rich_media_message_serialize(rich_media_obj):
    obj = RichMediaMessage(
        rich_media=rich_media_obj,
        alt_text='alt text',
        tracking_data='tracking data'
    )
    expected = {
        'min_api_version': 7,
        'type': 'rich_media',
        'rich_media': rich_media_obj.serialize(),
        'alt_text': 'alt text',
        'tracking_data': 'tracking data'
    }
    assert obj.serialize(add_min_api_ver=True) == expected

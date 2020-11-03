def test_serialize_button(
    button_obj,
    internal_browser_obj,
    map_obj,
    frame_obj,
    media_player_obj
):
    expected = {
        'ActionBody': 'action body',
        'Columns': 6,
        'Rows': 1,
        'BgColor': '#000000',
        'Silent': True,
        'BgMediaType': 'picture',
        'BgMedia': 'some_url',
        'BgMediaScaleType': 'crop',
        'ImageScaleType': 'crop',
        'BgLoop': True,
        'ActionType': 'reply',
        'Image': 'some_url',
        'Text': 'text',
        'TextVAlign': 'middle',
        'TextHAlign': 'center',
        'TextPaddings': [12, 12, 12, 12],
        'TextOpacity': 100,
        'TextSize': 'regular',
        'OpenURLType': 'internal',
        'OpenURLMediaType': 'not-media',
        'TextBgGradientColor': '#000000',
        'TextShouldFit': False,
        'InternalBrowser': internal_browser_obj.serialize(),
        'Map': map_obj.serialize(),
        'Frame': frame_obj.serialize(),
        'MediaPlayer': media_player_obj.serialize()
    }
    assert button_obj.serialize() == expected

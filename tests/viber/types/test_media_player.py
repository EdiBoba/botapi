def test_media_player_serialize(media_player_obj):
    expected = {
        'Title': 'title',
        'Subtitle': 'subtitle',
        'ThumbnailURL': 'some_url',
        'Loop': False,
        'min_api_version': 6
    }
    assert media_player_obj.serialize(add_min_api_ver=True) == expected

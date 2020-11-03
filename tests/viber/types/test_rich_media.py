def test_rich_media_serialize(rich_media_obj, button_obj, favorites_metadata_obj):
    expected = {
        'Buttons': [button_obj.serialize()],
        'ButtonsGroupColumns': 6,
        'ButtonsGroupRows': 7,
        'BgColor': '#000000',
        'Type': 'rich_media',
        'FavoritesMetadata': favorites_metadata_obj.serialize()
    }
    assert rich_media_obj.serialize() == expected


def test_rich_media_add_button(rich_media_obj, button_obj, favorites_metadata_obj):
    rich_media_obj.add_button(button_obj)
    expected = {
        'Buttons': [button_obj.serialize(), button_obj.serialize()],
        'ButtonsGroupColumns': 6,
        'ButtonsGroupRows': 7,
        'BgColor': '#000000',
        'Type': 'rich_media',
        'FavoritesMetadata': favorites_metadata_obj.serialize()
    }
    assert rich_media_obj.serialize() == expected

def test_ib_serialize(internal_browser_obj):
    expected = {
        'ActionButton': 'forward',
        'ActionPredefinedURL': 'some_url',
        'TitleType': 'default',
        'CustomTitle': 'custom_title',
        'Mode': 'fullscreen',
        'FooterType': 'default',
        'ActionReplyData': 'action_reply',
        'min_api_version': 6
    }
    assert internal_browser_obj.serialize(add_min_api_ver=True) == expected

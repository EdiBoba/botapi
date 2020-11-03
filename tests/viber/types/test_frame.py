def test_frame_serialize(frame_obj):
    expected = {
        'BorderWidth': 1,
        'BorderColor': '#000000',
        'CornerRadius': 0,
        'min_api_version': 6
    }
    assert frame_obj.serialize(add_min_api_ver=True) == expected

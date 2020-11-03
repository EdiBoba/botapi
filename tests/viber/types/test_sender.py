def test_sender_serialize(sender_obj):
    expected = {
        'name': 'John McClane',
        'avatar': 'http://avatar.example.com'
    }
    assert sender_obj.serialize() == expected

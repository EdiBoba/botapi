def test_contact_serialize(contact_obj):
    expected = {
        'name': 'Itamar',
        'phone_number': '+972511123123'
    }
    assert contact_obj.serialize() == expected

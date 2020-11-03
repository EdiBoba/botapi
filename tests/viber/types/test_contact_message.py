from botapi.viber.types import ContactMessage


def test_contact_message_serialize(contact_obj):
    obj = ContactMessage(contact=contact_obj, tracking_data='tracking data')
    expected = {
        'type': 'contact',
        'min_api_version': 1,
        'tracking_data': 'tracking data',
        'contact': contact_obj.serialize()
    }
    assert obj.serialize(add_min_api_ver=True) == expected

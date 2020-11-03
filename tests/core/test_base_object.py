def test_serialize_object(obj_with_fields):
    obj_with_fields.base = 1
    expected = {
        'base': 1,
        'alias_field': 'default',
        'list_field': [
            1,
            'string',
            {
                'field': 'field'
            }
        ],
        'updated_field': 1
    }
    assert obj_with_fields.serialize(data_to_update={'updated_field': 1}) == expected

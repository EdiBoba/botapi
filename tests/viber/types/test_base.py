def test_base_obj_update_data(map_obj):
    expected = {
        **map_obj.serialize(),
        'updated_field': 'new_field'
    }
    assert map_obj.serialize(data_to_update={'updated_field': 'new_field'}) == expected

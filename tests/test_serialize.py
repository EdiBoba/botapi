def test_serialize(child_model, nested_model):
    obj = child_model()
    obj.self_base = child_model()
    obj.model = nested_model()
    obj.model.field = {'a': 'b'}
    obj.int_list = [1, 2, 3]
    obj.simple_list = [nested_model(), nested_model()]

    expected = {
        'self_base': {
            'child field': 2
        },
        'child field': 2,
        'model': {
            'field': {'a': 'b'}
        },
        'int_list': [1, 2, 3],
        'simple_list': [{'field': 1}, {'field': 1}],
        'updated_value': 1
    }

    assert obj.serialize({'updated_value': 1}) == expected

    new_obj = child_model(**expected)
    assert new_obj.serialize({'updated_value': 1}) == expected

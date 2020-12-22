from botapi.types import DateTime


def test_serialize(child_model, nested_model):
    obj = child_model()
    obj.self_base = child_model()
    obj.model = nested_model()
    obj.model.field = {'a': 'b'}
    obj.int_list = [1, 2, 3]
    obj.simple_list = [nested_model(), nested_model()]
    obj.dateformat_field = DateTime(2020, 12, 12, 10, 5, 3)
    obj.datetime_field = '2020-12-12 10:05:03'

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
        'updated_value': 1,
        'dateformat_field': '10:05:03',
        'datetime_field': '2020-12-12 10:05:03'
    }

    assert obj.serialize({'updated_value': 1}) == expected

    new_obj = child_model(**expected)
    assert new_obj.serialize({'updated_value': 1}) == expected

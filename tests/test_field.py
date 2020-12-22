from datetime import datetime

import pytest

from botapi import Field
from botapi.types import DateTime


def test_fields_and_aliases(child_model):
    obj = child_model()
    assert obj._fields == {
        'self_base',
        'field',
        'model',
        'simple_list',
        'int_list',
        'model_list',
        'date_field',
        'dateformat_field',
        'datetime_field'
    }
    assert obj._aliases == {'field': 'child field'}


def test_self_base(parent_model):
    # self_base ignore base
    assert parent_model.self_base.base == parent_model

    obj = parent_model()
    # type check
    with pytest.raises(TypeError):
        obj.self_base = 'not ParentModel'

    obj.self_base = parent_model()
    # nested model field access
    assert obj.self_base.field == 1
    assert obj.self_base.self_base is None


def test_field_inheritance(parent_model, child_model):
    parent_object = parent_model()
    assert parent_object.field == 1
    assert parent_object._aliases == {'field': 'parent field'}

    child_object = child_model()

    assert child_object.field == 2
    assert child_object._aliases == {'field': 'child field'}


def test_model_field(parent_model, nested_model):
    obj = parent_model()
    obj.model = nested_model()

    # nested model field access
    assert obj.model.field == 1


def test_type_check(parent_model):
    obj = parent_model()

    with pytest.raises(TypeError):
        obj.field = 'not int'

    with pytest.raises(TypeError):
        obj.model = 'not model'

    with pytest.raises(TypeError):
        obj.self_base = 'not model'

    # raise error after set
    obj.field = 1
    with pytest.raises(TypeError):
        obj.field = 'not int'


def test_list_field(parent_model, nested_model):
    obj = parent_model()

    assert obj.simple_list is None
    with pytest.raises(TypeError):
        obj.simple_list = 1

    with pytest.raises(TypeError):
        obj.int_list = 'iterable'

    obj.model_list = []

    with pytest.raises(TypeError):
        obj.model_list.append('not model')

    obj.model_list.append(nested_model())
    assert obj.model_list[0].field == 1

    obj.simple_list = 'iterable'
    assert obj.simple_list == ['i', 't', 'e', 'r', 'a', 'b', 'l', 'e']


def test_datetime_field(parent_model):
    obj = parent_model()

    with pytest.raises(ValueError):
        obj.date_field = 'not date format'

    with pytest.raises(TypeError):
        obj.date_field = 13.5

    with pytest.raises(ValueError):
        obj.dateformat_field = 'not date format'

    with pytest.raises(ValueError):
        obj.datetime_field = 'not date format'

    with pytest.raises(TypeError):
        obj.datetime_field = 13.5

    obj.dateformat_field = datetime(2020, 12, 12, 10, 5, 3)
    obj.datetime_field = '2020-12-12 10:05:03'

    assert type(obj.dateformat_field) == DateTime
    assert str(obj.dateformat_field) == '10:05:03'
    assert obj.datetime_field.year == 2020
    assert obj.datetime_field.month == 12
    assert obj.datetime_field.day == 12
    assert obj.datetime_field.hour == 10
    assert obj.datetime_field.minute == 5
    assert obj.datetime_field.second == 3

    obj.date_field = '2020-12-12 10:05:03'
    assert type(obj.date_field) == datetime
    assert str(obj.date_field) == '2020-12-12 10:05:03'


def test_on_the_fly(parent_model):
    with pytest.raises(TypeError):
        parent_model.self_base = Field()

    obj = parent_model()
    with pytest.raises(TypeError):
        obj.self_base = Field()

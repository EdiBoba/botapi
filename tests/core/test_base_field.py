import pytest


def test_base(obj_with_fields):
    with pytest.raises(TypeError):
        obj_with_fields.base = 'not int'


def test_self_base(obj_with_fields):
    with pytest.raises(TypeError):
        obj_with_fields.self_base = 'not ClassWithFields'


def test_self_base_ignore_base(obj_with_fields):
    with pytest.raises(TypeError):
        obj_with_fields.base_self_base = 1


def test_default(obj_with_fields):
    assert obj_with_fields.default_alias == 'default'


def test_field_inheritance(small_base_class_child):
    assert small_base_class_child().field == 'child_field'

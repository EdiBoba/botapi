import pytest

from botapi.core import Field, BotObject


@pytest.fixture
def small_base_class():
    class Small(BotObject):
        field = Field(default='field')

    return Small


@pytest.fixture
def small_base_class_child(small_base_class):
    class SmallChild(small_base_class):
        field = Field(default='child_field')

    return SmallChild


@pytest.fixture
def obj_with_fields(small_base_class):
    class ClassWithFields(BotObject):
        base = Field(base=int)
        self_base = Field(self_base=True)
        base_self_base = Field(base=int, self_base=True)
        default_alias = Field(default='default', alias='alias_field')
        list_field = Field(default=[
            1,
            'string',
            small_base_class()
        ])

    return ClassWithFields()

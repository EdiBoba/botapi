import pytest

from botapi import Model, Field, ListField


@pytest.fixture(scope='function')
def nested_model():
    class NestedModel(Model):
        field = Field(default=1)

    return NestedModel


@pytest.fixture(scope='function')
def parent_model(nested_model):
    class ParentModel(Model):
        self_base = Field(base=int, self_base=True)
        field = Field(base=int, alias='parent field', default=1)
        model = Field(base=nested_model)
        int_list = ListField(item_base=int)
        model_list = ListField(item_base=nested_model)
        simple_list = ListField()

    return ParentModel


@pytest.fixture(scope='function')
def child_model(parent_model):
    class ChildModel(parent_model):
        field = Field(alias='child field', default=2)

    return ChildModel

import pytest

from botapi.viber.types import Message


def test_abstract_message():
    with pytest.raises(TypeError):
        Message()

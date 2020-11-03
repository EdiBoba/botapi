import pytest

from botapi.viber.types import Keyboard


@pytest.fixture
def keyboard_object(button_obj):
    return Keyboard(
        buttons=[button_obj],
        bg_color='#000000',
        default_height=False,
        custom_default_height=70,
        height_scale=100,
        buttons_group_columns=6,
        buttons_group_rows=2,
        input_field_state='regular'
    )


def test_keyboard_serialize(keyboard_object, button_obj):
    expected = {
        'Type': 'keyboard',
        'Buttons': [button_obj.serialize()],
        'BgColor': '#000000',
        'DefaultHeight': False,
        'CustomDefaultHeight': 70,
        'HeightScale': 100,
        'ButtonsGroupColumns': 6,
        'ButtonsGroupRows': 2,
        'InputFieldState': 'regular'
    }
    assert keyboard_object.serialize() == expected


def test_add_button(keyboard_object, button_obj):
    keyboard_object.add_button(button_obj)
    expected = {
        'Type': 'keyboard',
        'Buttons': [button_obj.serialize(), button_obj.serialize()],
        'BgColor': '#000000',
        'DefaultHeight': False,
        'CustomDefaultHeight': 70,
        'HeightScale': 100,
        'ButtonsGroupColumns': 6,
        'ButtonsGroupRows': 2,
        'InputFieldState': 'regular'
    }
    assert keyboard_object.serialize() == expected

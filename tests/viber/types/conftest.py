import pytest

from botapi.viber import types
from botapi.viber.types.sender import Sender


@pytest.fixture
def internal_browser_obj():
    return types.InternalBrowser(
        action_button='forward',
        action_predefined_url='some_url',
        title_type='default',
        custom_title='custom_title',
        mode='fullscreen',
        footer_type='default',
        action_reply_data='action_reply'
    )


@pytest.fixture
def map_obj():
    return types.Map(
        latitude='37.7898',
        longitude='-122.3942'
    )


@pytest.fixture
def frame_obj():
    return types.Frame(
        border_width=1,
        border_color='#000000',
        corner_radius=0
    )


@pytest.fixture
def media_player_obj():
    return types.MediaPlayer(
        title='title',
        subtitle='subtitle',
        thumbnail_url='some_url',
        loop=False
    )


@pytest.fixture
def button_obj(internal_browser_obj, map_obj, frame_obj, media_player_obj):
    return types.Button(
        action_body='action body',
        columns=6,
        rows=1,
        bg_color='#000000',
        silent=True,
        bg_media_type='picture',
        bg_media='some_url',
        bg_media_scale_type='crop',
        image_scale_type='crop',
        bg_loop=True,
        action_type='reply',
        image='some_url',
        text='text',
        text_v_align='middle',
        text_h_align='center',
        text_paddings=[12, 12, 12, 12],
        text_opacity=100,
        text_size='regular',
        open_url_type='internal',
        open_url_media_type='not-media',
        text_bg_gradient_color='#000000',
        text_should_fit=False,
        internal_browser=internal_browser_obj,
        open_map=map_obj,
        frame=frame_obj,
        media_player=media_player_obj
    )


@pytest.fixture
def favorites_metadata_obj():
    return types.FavoritesMetadata(
        data_type='link',
        url='https://en.wikipedia.org/wiki/Viber',
        title='Interesting article about Viber',
        thumbnail='https://www.viber.com/app/uploads/icon-purple.png',
        domain='www.wikipedia.org',
        width=480,
        height=320,
        alternative_url='https://www.viber.com/about/',
        alternative_text='About Viber'
    )


@pytest.fixture
def rich_media_obj(button_obj, favorites_metadata_obj):
    return types.RichMedia(
        buttons=[button_obj],
        buttons_group_columns=6,
        buttons_group_rows=7,
        bg_color='#000000',
        favorites_metadata=favorites_metadata_obj
    )


@pytest.fixture
def contact_obj():
    return types.Contact(name="Itamar", phone_number="+972511123123")


@pytest.fixture
def location_obj():
    return types.Location("37.7898", "-122.3942")


@pytest.fixture
def sender_obj():
    return Sender(
        name='John McClane',
        avatar='http://avatar.example.com'
    )

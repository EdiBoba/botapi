from botapi.viber.types import Webhook


def test_webhook_serialize():
    obj = Webhook(
        url='https://my.host.com',
        event_types=[
            'delivered',
            'seen',
            'failed',
            'subscribed',
            'unsubscribed',
            'conversation_started'
        ],
        send_name=True,
        send_photo=True
    )
    expected = {
        'url': 'https://my.host.com',
        'event_types': [
            'delivered',
            'seen',
            'failed',
            'subscribed',
            'unsubscribed',
            'conversation_started'
        ],
        'send_name': True,
        'send_photo': True
    }
    assert obj.serialize() == expected

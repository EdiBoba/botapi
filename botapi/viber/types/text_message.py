from botapi.viber.types.base import ViberField as Field
from botapi.viber.types.message import Message


class TextMessage(Message):
    """
    Represents a Viber text message object

    https://developers.viber.com/docs/api/rest-bot-api/#text-message
    """

    message_type = Field(default='text', alias='type')
    text = Field()

    def __init__(self, text: str, tracking_data: str = None):
        """
        :param text: The text of the message

        :param tracking_data: Allow the account to track messages and user’s replies.
            Sent tracking_data value will be passed back with user’s reply.
            max 4000 characters
        """
        self.text = text
        self.tracking_data = tracking_data

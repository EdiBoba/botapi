from botapi.viber.types.base import ViberField
from botapi.viber.types.keyboard import Keyboard
from botapi.viber.types.message import Message


class StickerMessage(Message):
    """
    Represents a Viber sticker message object

    https://developers.viber.com/docs/api/rest-bot-api/#sticker-message
    """
    message_type = ViberField(default='sticker', alias='type')
    sticker_id = ViberField()

    def __init__(
        self,
        sticker_id: int,
        tracking_data: str = None,
        keyboard: Keyboard = None
    ):
        """
        :param sticker_id: Unique Viber sticker ID.
            For examples visit the sticker IDs page:
            https://developers.viber.com/docs/tools/sticker-ids/

        :param tracking_data: Allow the account to track messages and user’s replies.
            Sent tracking_data value will be passed back with user’s reply.
            max 4000 characters
        """
        self.sticker_id = sticker_id
        self.tracking_data = tracking_data
        self.keyboard = keyboard

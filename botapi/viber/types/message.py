from abc import abstractmethod

from botapi.viber.types import ViberObject, ViberField
from botapi.viber.types.keyboard import Keyboard


class Message(ViberObject):
    """
    Represents a Viber message object with general message parameters

    https://developers.viber.com/docs/api/rest-bot-api/#general-send-message-parameters
    """

    tracking_data = ViberField()
    keyboard = ViberField(base=Keyboard)

    @property
    @abstractmethod
    def message_type(self):
        raise NotImplementedError

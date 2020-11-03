from abc import abstractmethod

from botapi.viber.types.base import ViberObject, ViberField as Field


class Message(ViberObject):
    """
    Represents a Viber message object with general message parameters

    https://developers.viber.com/docs/api/rest-bot-api/#general-send-message-parameters
    """

    tracking_data = Field()

    @property
    @abstractmethod
    def message_type(self):
        raise NotImplementedError

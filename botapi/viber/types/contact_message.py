from botapi.viber.types.base import ViberField
from botapi.viber.types.contact import Contact
from botapi.viber.types.message import Message


class ContactMessage(Message):
    """
    Represents a Viber contact message object

    https://developers.viber.com/docs/api/rest-bot-api/#contact-message
    """

    message_type = ViberField(default='contact', alias='type')
    contact = ViberField(base=Contact)

    def __init__(
        self,
        contact: Contact,
        tracking_data: str = None
    ):
        """
        :param contact: contact to send

        :param tracking_data: Allow the account to track messages and user’s replies.
            Sent tracking_data value will be passed back with user’s reply.
            max 4000 characters
        """
        self.contact = contact
        self.tracking_data = tracking_data

"""Defines Features Request classes and related items."""

# Local source tree imports
from pyof.v0x01.common import header as of_header
from pyof.v0x01.foundation import base

__all__ = ('FeaturesRequest')

# Classes


class FeaturesRequest(base.GenericMessage):
    """Features request message.

    This message does not contain a body in addition to the OpenFlow Header.

    Args:
        xid (int): xid to be used on the message header.

    """

    header = of_header.Header(
        message_type=of_header.Type.OFPT_FEATURES_REQUEST)

    def __init__(self, xid=None):
        super().__init__()
        self.header.xid = xid

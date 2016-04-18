import unittest

from ofp.v0x01.controller2switch import barrier_reply

class TestBarrierReply(unittest.TestCase):
    def test_get_size(self):
        barrier_reply_message = barrier_reply.BarrierReply(xid=1)
        self.assertEqual(barrier_reply_message.get_size(), 8)

    def test_pack(self):
        barrier_reply_message = barrier_reply.BarrierReply(xid=1)
        barrier_reply_message.pack()

    def test_unpack(self):
        pass
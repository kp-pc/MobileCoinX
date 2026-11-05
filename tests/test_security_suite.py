"""Security-focused automated test suite for Tachoin-Coin."""

from __future__ import annotations
import json
import unittest
from mobilecoin.node import make_deterministic_node
from mobilecoin.transaction import TachoinTx
from mobilecoin.config import TRANSFER_FEE, TOKEN_DECIMALS
from mobilecoin.wallet import TachoinWallet

ONE_TACH = 10 ** TOKEN_DECIMALS

class SecurityTests(unittest.TestCase):
    def setUp(self):
        self.node, self.wallets = make_deterministic_node(4)
        self.sender = self.wallets[0]

    def test_malformed_payload_does_not_crash_node(self):
        tx = TachoinTx.build(self.sender, "transfer", b"invalid json", 0, 1)
        result = self.node.submit_transaction(tx)
        self.assertFalse(result.success)

if __name__ == '__main__':
    unittest.main()

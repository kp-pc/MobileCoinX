"""Simple mobile‑friendly Proof‑of‑Work implementation.

The difficulty is deliberately low (e.g. target = 2^240) so a modern phone can solve a block
in a few seconds. The algorithm is a straightforward incremental nonce search over the
SHA‑256 hash of the block header bytes.
"""
import hashlib

class MobilePoW:
    def __init__(self, difficulty: int = 240):
        self.difficulty = difficulty
        self.target = 1 << (256 - difficulty)

    def solve(self, header_bytes: bytes) -> str:
        """Return a hex nonce that makes ``hash(header_bytes + nonce) < target``.

        The returned string is a 16‑character zero‑padded hex for easy transport.
        """
        nonce = 0
        while True:
            candidate = header_bytes + nonce.to_bytes(8, "big")
            h = int.from_bytes(hashlib.sha256(candidate).digest(), "big")
            if h < self.target:
                return f"{nonce:016x}"
            nonce += 1

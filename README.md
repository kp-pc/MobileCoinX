# MobileCoinX 🪙

**MobileCoinX** is a lightweight, mobile‑first cryptocurrency built on the Tachyon blockchain reference implementation. It combines a **very low‑difficulty Proof‑of‑Work** (PoW) that can be solved on Android and iOS devices with a traditional **Proof‑of‑Stake** (PoS) validator set that secures the network and rewards token holders.

---

## 🌟 Goals
- **Encourage participation from smartphones** – the PoW puzzle is tuned so a modern phone can find a nonce in a few seconds, avoiding the need for ASICs or high‑end GPUs.
- **Reward both miners and stakers** – every block gives a mining reward to the miner (the PoW solver) and a portion of the reward is automatically delegated to the PoS validator set, while holders receive a share of transaction fees.
- **Keep the ecosystem simple** – the code base is a small fork of the well‑documented Tachoin project, written in pure Python, with zero external dependencies.

---

## 🚀 Quick start (desktop)
```bash
# Clone the repository
git clone https://github.com/yourusername/MobileCoinX.git
cd MobileCoinX

# Install the package (editable mode)
pip install -e .

# Run a simulation with mobile‑friendly mining
python -m mobilecoin run --blocks 10 --txs-per-block 3
```
The command will simulate 10 slots, each mined by a lightweight PoW solver.

---

## 📱 Mobile mining SDK
A minimal Python SDK is provided for Android/iOS developers (via Chaquopy or BeeWare). The SDK exposes a single function:
```python
from mobilecoin.consensus import MobilePoW

# Obtain the pending header from a node (e.g. via HTTP GET /pending_header)
header_bytes = ...
nonce = MobilePoW().solve(header_bytes)
# POST the nonce back to the node to claim the block reward
```
You can wrap this in Kotlin/Swift bindings to let users mine directly from their phone.

---

## 🛠️ Development
- **Run the test suite** – the original Tachoin tests still pass:
  ```bash
  pytest tests
  ```
- **Lint & format** – the project follows Black formatting.
- **Extending PoS rewards** – edit `mobilecoin/node.py` in the *Simple PoS reward distribution* section to change the reward split.

---

## 📚 Documentation
Full API docs are generated from the source code. See the `docs/` folder for architecture diagrams and the `README.md` for usage examples.

---

## 🤝 Contributing
Open issues or pull requests are welcome! Please follow the classic GitHub workflow:
1. Fork the repo
2. Create a feature branch
3. Submit a PR

---

## 📜 License
MIT – see the `LICENSE` file.

<p align="center">
  <a href="#">
    <img
      alt="Solathon logo"
      src="https://solathon.vercel.app/solathon.svg"
      width="140"
    />
  </a>
</p>


<p align="center">
  <a href="https://pypi.org/project/solathon_aiohttp/" target="_blank"><img src="https://badge.fury.io/py/solathon_aiohttp.svg" alt="PyPI version"></a>
  <a href="https://github.com/Vlad2030/solathon-aiohttp/blob/main/LICENSE" target="_blank"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
  <br>
</p>

<h1 align="center">Solathon-aiohttp</h1>

Solathon is a high performance, easy to use and feature-rich Solana SDK for Python.
Easy for beginners, powerful for real world applications.

Rewritten solathon that uses `aiohttp` instead `httpx`

# ✨ Getting started
## Installation
```
pip install solathon_aiohttp
```
## Client example
```python
import asyncio

from solathon_aiohttp import AsyncClient, MAINNET_ENDPOINT

async def main() -> None:
    client = AsyncClient(MAINNET_ENDPOINT)

if __name__ == "__main__":
    asyncio.run(main())

```
## Basic usage example
```python
# Basic example of fetching a public key's balance
import asyncio
from solathon_aiohttp import AsyncClient, DEVNET_ENDPOINT

public_key = "6igbZNEsbRRXvutJc3VYC19MxNg9u1zMHX39zgXpjgrn"

async def main() -> None:
    client = AsyncClient(MAINNET_ENDPOINT)
    balance = await client.get_balance(public_key)
    print(balance)

if __name__ == "__main__":
    asyncio.run(main())
```

# 🗃️ Contribution
Drop a pull request for anything which seems wrong or can be improved, could be a small typo or an entirely new feature! Checkout [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to proceed.

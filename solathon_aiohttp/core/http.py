from __future__ import annotations

import asyncio
import base64
import sys
from typing import Any

import aiohttp
import orjson

from .. import __version__
from ..publickey import PublicKey
from .types import RPCResponse


class AsyncHTTPClient:
    """Asynchronous HTTP Client to interact with Solana JSON RPC"""

    def __init__(self, endpoint: str):
        if "win" in sys.platform:
            asyncio.set_event_loop_policy(
                asyncio.WindowsSelectorEventLoopPolicy()
            )
        self.endpoint = endpoint
        version = sys.version_info
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": (
                "Solathon-aiohttp (https://github.com/Vlad2030/solathon-aiohttp "
                f"{__version__}) Python{version[0]} {version[1]}"
            ),
        }
        self.request_id = 0
        self.client = aiohttp.ClientSession(
            json_serialize=(lambda data: orjson.dumps(data).decode()),
        )

    async def send(self, data: dict[str, Any]) -> RPCResponse:
        async with self.client:
            _res = await self.client.post(
                url=self.endpoint, headers=self.headers, json=data
            )
        res = await _res.json(loads=orjson.loads)
        return RPCResponse(**res)

    def build_data(self, method: str, params: list[Any]) -> dict[str, Any]:
        self.request_id += 1
        params: list[Any] = [
            str(i) if isinstance(i, PublicKey) else i for i in params
        ]

        if isinstance(params[0], bytes):
            params[0] = base64.b64encode(params[0]).decode("utf-8")

        return {
            "jsonrpc": "2.0",
            "id": self.request_id,
            "method": method,
            "params": None if params[0] is None else params,
        }

    async def refresh(self) -> None:
        await self.client.close()
        self.request_id = 0
        self.client = aiohttp.ClientSession(
            json_serialize=(lambda data: orjson.dumps(data).decode()),
        )

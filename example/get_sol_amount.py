import asyncio

from solathon_aiohttp import AsyncClient, MAINNET_ENDPOINT
from solathon_aiohttp.utils import lamport_to_sol

public_key = "6igbZNEsbRRXvutJc3VYC19MxNg9u1zMHX39zgXpjgrn"

async def main() -> None:
    client = AsyncClient(MAINNET_ENDPOINT)

    account_info = await client.get_account_info(public_key)

    sol_amount_lamports = account_info["result"]["value"]["lamports"]
    sol_amount = lamport_to_sol(sol_amount_lamports)

    print(f"Account:\t{public_key}")
    print(f"SOL amount:\t{sol_amount} ({sol_amount_lamports})")


if __name__ == "__main__":
    asyncio.run(main())

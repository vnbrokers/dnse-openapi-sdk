"""
Market index subscription example.

Demonstrates:
- Subscribing to market index

This example shows how to receive real-time market index
"""

import asyncio
import os

from dnse import TradingClient
from datetime import datetime

from dnse.websocket.models import EstimatedMarketIndex


async def main():
    # Initialize client
    encoding = "msgpack"  # json or msgpack
    client = TradingClient(
        api_key=os.getenv("DNSE_API_KEY"),
        api_secret=os.getenv("DNSE_API_SECRET"),
        base_url="wss://ws-openapi.dnse.com.vn",
        encoding=encoding,
    )

    def handle_estimated_market_index(data: EstimatedMarketIndex):
        received_at = datetime.fromtimestamp(data.receivedAt).strftime("%H:%M:%S.%f")[:-3] if data.receivedAt else "N/A"
        print(f"[{received_at}] Estimated market index: {data}")

    # Connect to gateway
    print("Connecting to WebSocket gateway...")
    await client.connect()
    print(f"Connected! Session ID: {client._session_id}\n")

    print("Subscribing to estimated market index...")
    await client.subscribe_estimated_market_index(estimated_market_index='VN30', on_estimated_market_index=handle_estimated_market_index, encoding=encoding)

    print("\nReceiving estimated market index (will run for 1 hour)...\n")

    # Run for 8H to collect data
    # In a real application, you might run indefinitely or until a specific condition
    await asyncio.sleep(8 * 60 * 60)

    # Disconnect gracefully
    print("\n\nDisconnecting...")
    await client.disconnect()
    print("Disconnected!")


if __name__ == "__main__":
    asyncio.run(main())
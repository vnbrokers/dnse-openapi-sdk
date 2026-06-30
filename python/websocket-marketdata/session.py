"""
Demonstrates:
- Subscribing to session data

This example shows how to receive real-time session data
"""

import asyncio
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from dnse import TradingClient
from dnse.websocket.models import Session


async def main():
    # Initialize client
    encoding = "msgpack"  # json or msgpack
    client = TradingClient(
        api_key="api-key",
        api_secret="api-secret",
        base_url="wss://ws-openapi.dnse.com.vn",
        encoding=encoding,
    )

    def handle_session(session: Session):
       received_at = datetime.fromtimestamp(session.receivedAt).strftime("%H:%M:%S.%f")[:-3] if session.receivedAt else "N/A"
       print(f"[{received_at}] Session: {session}")

    # Connect to gateway
    print("Connecting to WebSocket gateway...")
    await client.connect()
    print(f"Connected! Session ID: {client._session_id}\n")

    print("Subscribing to session data...")
    await client.subscribe_session(product_group_id="STX", board_id = "G1", on_session=handle_session, encoding=encoding)

    print("\nReceiving session data (will run for 1 hour)...\n")

    # Run for 8H to collect data
    # In a real application, you might run indefinitely or until a specific condition
    await asyncio.sleep(8 * 60 * 60)

    # Disconnect gracefully
    print("\n\nDisconnecting...")
    await client.disconnect()
    print("Disconnected!")


if __name__ == "__main__":
    asyncio.run(main())

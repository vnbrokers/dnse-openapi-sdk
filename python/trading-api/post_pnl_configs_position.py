#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from dnse import DNSEClient


def main():
    client = DNSEClient(
        api_key=os.getenv("DNSE_API_KEY"),
        api_secret=os.getenv("DNSE_API_SECRET"),
        base_url="https://openapi.dnse.com.vn",
    )

    payload = {
        "takeProfit": {
            "enabled": False,
            "strategy": "DELTA_PRICE",
            "rate": 0.52,
            "deltaPrice": 162.8,
            "orderMethod": "FASTEST",
            "orderDeltaPrice": 2
        },
        "stopLoss": {
            "enabled": False,
            "strategy": "PNL_RATE",
            "rate": -0.34,
            "deltaPrice": 50.3,
            "orderMethod": "DELTA_PRICE",
            "orderDeltaPrice": 10.5,
            "trailingEnabled": False
        }
    }

    status, body = client.post_pnl_configs_position(
        market_type="DERIVATIVE",
        payload=payload,
        trading_token=os.getenv("DNSE_TRADING_TOKEN"),
        order_category="NORMAL",
        dry_run=False,
    )
    print(status, body)


if __name__ == "__main__":
    main()

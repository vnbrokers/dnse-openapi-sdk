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

    status, body = client.get_order_detail(
        account_no="0001000115",
        order_id="801",
        market_type="STOCK",
        order_category="NORMAL",
        dry_run=False,
    )
    print(status, body)


if __name__ == "__main__":
    main()

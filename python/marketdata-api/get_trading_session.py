#!/usr/bin/env python3
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from dnse import DNSEClient


def main():
    client = DNSEClient(
        api_key=os.getenv("DNSE_API_KEY"),
        api_secret=os.getenv("DNSE_API_SECRET"),
        base_url="https://openapi.dnse.com.vn",
    )

    status, body = client.get_trading_session(tsc_prod_grp_id="FBX", board_id="", dry_run=False)
    print(status, body)


if __name__ == "__main__":
    main()

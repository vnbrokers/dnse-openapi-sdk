#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from dnse import DNSEClient

def main():
    client = DNSEClient(
        api_key="replace-with-api-key",
        api_secret="replace-with-api-secret",
        base_url="https://openapi.dnse.com.vn",
    )

    status, body = client.get_corporate_action_history(
        account_no="0001000115",
        symbol="SSI",
        ca_type="all",
        ca_status="pending",
        page_index=0,
        page_size=20,
        dry_run=False,
    )
    print(status, body)


if __name__ == "__main__":
    main()

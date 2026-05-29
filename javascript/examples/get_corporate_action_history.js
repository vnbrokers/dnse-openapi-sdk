'use strict';

const { DNSEClient } = require('../dnse');

async function main() {
  const client = new DNSEClient({
    apiKey: process.env.DNSE_API_KEY || 'replace-with-api-key',
    apiSecret: process.env.DNSE_API_SECRET || 'replace-with-api-secret',
    baseUrl: process.env.DNSE_BASE_URL || 'https://openapi.dnse.com.vn',
  });

  const { status, body } = await client.getCorporateActionHistory('0001234567', {
    fromDate: '2026-01-01',
    toDate: '2026-01-31',
    dryRun: false,
  });

  console.log(status, body);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

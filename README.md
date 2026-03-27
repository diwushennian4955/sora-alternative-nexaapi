# 🎬 Sora Alternative — NexaAPI Video Generation

[![Free Tier Available](https://img.shields.io/badge/Free%20Tier-Available-green)](https://nexa-api.com)
[![PyPI](https://img.shields.io/badge/pip-nexaapi-blue)](https://pypi.org/project/nexaapi/)
[![npm](https://img.shields.io/badge/npm-nexaapi-red)](https://www.npmjs.com/package/nexaapi)

**OpenAI Sora shut down on March 24, 2026.** This repo provides drop-in replacement code using [NexaAPI](https://nexa-api.com) — access Kling 3.0, Veo 3, Sora 2, and more at 3x lower cost.

## Quick Start

```bash
pip install nexaapi
```

```python
from nexaapi import NexaAPI
client = NexaAPI(api_key='YOUR_FREE_API_KEY')  # Get free key at nexa-api.com

response = client.video.generate(
    model='kling-3.0-pro',
    prompt='Cinematic mountain landscape at sunset',
    duration=5
)
print(response.video_url)
```

## Files

- `migrate_from_sora.py` — Python migration guide
- `migrate_from_sora.js` — JavaScript migration guide

## Pricing Comparison

| Model | NexaAPI | Direct | Savings |
|-------|---------|--------|---------|
| Kling 3.0 Pro | $0.0333/sec | ~$0.10/sec | 3x cheaper |
| Sora 2 | $0.07/sec | $0.20/sec | 2.9x cheaper |
| Veo 3 | $0.15/sec | $0.40/sec | 2.7x cheaper |

## Links

- 🌐 [nexa-api.com](https://nexa-api.com)
- 🚀 [RapidAPI](https://rapidapi.com/user/nexaquency)
- 🐍 [PyPI](https://pypi.org/project/nexaapi/)
- 📦 [npm](https://www.npmjs.com/package/nexaapi)

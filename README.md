# Process Synchronisation: Food Delivery Order Acceptance

OS course project. Problem: several delivery partners try to accept the same order at the same time.

| File | What it shows |
|---|---|
| `unsafe_version.py` | No lock -> race condition, one order accepted by many partners |
| `safe_version.py` | Mutex lock per order -> each order accepted by exactly one partner |
| `screenshots/` | Output screenshots of both versions |

## How to run
```
python unsafe_version.py
python safe_version.py
```
Requires Python 3 only.

## Team
- Person 1: repo + unsafe version
- Person 2: safe version + semaphores
- Person 3: comparison + report

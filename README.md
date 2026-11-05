# Process Synchronisation: Food Delivery Order Acceptance

OS course project. Problem: several delivery partners try to accept the same order at the same time.

| File | What it shows |
|---|---|
| `unsafe_version.py` | No lock -> race condition, one order accepted by many partners |
| `safe_version.py` | Mutex lock per order -> each order accepted by exactly one partner |
| `unsafe_version1.png` to `unsafe_version3.png`, `safe_version.png` | Output screenshots of both versions |

## How it works
In the unsafe version, a partner checks whether an order is free and then assigns it to themselves in two separate steps. Another partner can slip in between, so one order is accepted by many partners (a race condition). In the safe version, each order has a mutex lock, so the check and the assignment happen as one unit and only one partner can accept an order.

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

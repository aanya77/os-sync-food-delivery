"""
SAFE VERSION - Food Delivery Order Acceptance (fixed with a mutex lock)

Fix: each order has its own Lock. The check and the assignment happen inside
`with order.lock:`, so only ONE partner at a time can run them (mutual exclusion).

Run: python safe_version.py
"""
import threading
import time
import random

NUM_PARTNERS = 15
NUM_ORDERS = 5


class Order:
    def __init__(self, order_id):
        self.id = order_id
        self.partner = None
        self.accepted_by = []
        self.lock = threading.Lock()               # NEW: one mutex per order


def accept_order(order, partner):
    with order.lock:                               # NEW: entry section
        if order.partner is None:                  # critical section starts
            time.sleep(random.uniform(0, 0.002))
            order.partner = partner
            order.accepted_by.append(partner)
                                                   # lock released here (exit section)


def partner_task(partner_id, orders):
    for order in orders:
        accept_order(order, f"Partner{partner_id}")


if __name__ == "__main__":
    orders = [Order(i) for i in range(1, NUM_ORDERS + 1)]
    threads = [threading.Thread(target=partner_task, args=(i, orders))
               for i in range(NUM_PARTNERS)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(f"=== SAFE VERSION: {NUM_PARTNERS} partners, {NUM_ORDERS} orders ===")
    conflicts = 0
    for o in orders:
        if len(o.accepted_by) > 1:
            conflicts += 1
            print(f"Order {o.id}: accepted by {len(o.accepted_by)} partners {o.accepted_by}  <-- BUG")
        else:
            print(f"Order {o.id}: accepted by {o.accepted_by}")
    print(f"\nOrders accepted by MORE than one partner: {conflicts} / {NUM_ORDERS}")

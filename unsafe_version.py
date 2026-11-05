"""
UNSAFE VERSION - Food Delivery Order Acceptance (has a race condition)

Problem: Many delivery partners (threads) press "Accept" on the same orders.
There is NO lock, so the check ("is the order free?") and the action
("assign it to me") can be interleaved -> one order gets accepted by
several partners.

Run: python unsafe_version.py
"""
import threading
import time
import random

NUM_PARTNERS = 15
NUM_ORDERS = 5


class Order:
    def __init__(self, order_id):
        self.id = order_id
        self.partner = None        # None = not yet accepted
        self.accepted_by = []      # every partner who saw "Order accepted!"


def accept_order(order, partner):
    if order.partner is None:                      # CHECK: is it free?
        time.sleep(random.uniform(0, 0.002))       # network delay -> context switch here
        order.partner = partner                    # ACT: assign (NOT atomic with the check)
        order.accepted_by.append(partner)


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

    print(f"=== UNSAFE VERSION: {NUM_PARTNERS} partners, {NUM_ORDERS} orders ===")
    conflicts = 0
    for o in orders:
        if len(o.accepted_by) > 1:
            conflicts += 1
            print(f"Order {o.id}: accepted by {len(o.accepted_by)} partners {o.accepted_by}  <-- BUG")
        else:
            print(f"Order {o.id}: accepted by {o.accepted_by}")
    print(f"\nOrders accepted by MORE than one partner: {conflicts} / {NUM_ORDERS}")

#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            self.total *= (1 - self.discount / 100)

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.total - (self.total - self.items[-1])
            self.total -= last_item_price
            self.items.pop()


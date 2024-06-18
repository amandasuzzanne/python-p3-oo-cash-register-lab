#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0) -> None:
      self.total = 0
      self.items = []
      self.discount = discount
      self.transactions = []
  
  def add_item(self, title, price, quantity=1) -> None:
      self.price = price
      for i in range(quantity):
        self.items.append(title)
        self.total += price
      self.transactions.append({"title": title, "price": price, "quantity": quantity})
  
  def apply_discount(self) -> None:
      if self.discount == 0:
        print("There is no discount to apply.")
      else:
        self.total -= (self.total * (self.discount / 100))
        print(f"After the discount, the total comes to ${int(self.total)}.")
  
  def void_last_transaction(self) -> None:
      if self.transactions == []:
        print("There are no transactions to void.")
      else:
         self.total -= (self.transactions[-1]["price"] * self.transactions[-1]["quantity"])
         for _ in range(self.transactions[-1]["quantity"]):
            self.items.pop()
            self.transactions.pop()
  

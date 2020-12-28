class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.money = 0

    def can_add(self, v):
        return self.money + v <= self.capacity

    def add(self, v):
        self.money += v
from typing import Any, SupportsIndex
from src.calculate_payment import calculate_payment

class Employee():

    def __init__(self, name: str, family: str, 
                 age: int, payment: float, emp_id: int):
        
        self.id = emp_id
        self.name = name
        self.family = family
        self.age = age
        self.payment = payment


    def __repr__(self) -> str:
        return f"{self.name}, {self.family}, {self.age}"
    
        
    def receive_payment(self, amount):
        self.payment = calculate_payment(payment=self.payment, amount=amount)
        return f"the {self.name} {self.family} receives, {self.payment}$ which {amount} is additional"
    
    def entrance(self, hour):
        return f"{self.name} {self.family} arraives at {hour}"

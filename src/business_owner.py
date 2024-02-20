from typing import Any
from src.employee import Employee


class BusinessOwner(Employee):

    def __repr__(self):
        print("ok")
        return f"{self.name}"

from src.employee import Employee
from src.business_owner import BusinessOwner


def main():

    emp_1 = Employee(name='alex', family='pit', age=23, payment=200.5, emp_id=1)
    b_o = BusinessOwner(name='bob', family='russel', age=20, payment=3000.0, emp_id=2)
    
    return (emp_1, b_o)


print(main())
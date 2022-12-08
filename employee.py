"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name,contract_type,salary_amount,rate,comission_type, comission_amount,comission_rate):
        self.name = name
        self.contract_type = contract_type
        self.salary_amount =salary_amount
        self.rate = rate
        self.comission_type = comission_type
        self.comission_amount =comission_amount
        self.comission_rate = comission_rate

    def get_pay(self):
        pay = 0
        if self.contract_type == 'monthly':
            pay += self.salary_amount
        elif self.contract_type == 'hourly':
            pay += self.salary_amount * self.rate
        
        if self.comission_type == 'bonus':
            pay += self.comission_amount
        elif self.comission_type == 'contract comission':
            pay += self.comission_amount * self.comission_rate
        
        return pay
        

    def __str__(self):
        string = ''
        if self.contract_type == 'monthly':
            if self.comission_type == '':
                string = f'{self.name} works on a {self.contract_type} salary of {self.salary_amount}.  Their total pay is {Employee.get_pay(self)}.'
            elif self.comission_type == 'contract':
                string = f'{self.name} works on a {self.contract_type} salary of {self.salary_amount} and receives a commission for {self.comission_amount} contract(s) at {self.comission_rate}/contract.  Their total pay is {Employee.get_pay(self)}.'
            elif self.comission_type == 'bonus':
                string = f'{self.name} works on a {self.contract_type} salary of {self.salary_amount} and receives a bonus commission of {self.comission_amount}.  Their total pay is {Employee.get_pay(self)}.'
        elif self.contract_type == 'hourly':
            if self.comission_type == '':
                string = f'{self.name} works on a contract of {self.salary_amount} hours at {self.rate}/hour.  Their total pay is {Employee.get_pay(self)}.'
            elif self.comission_type == 'contract':
                string = f'{self.name} works on a contract of {self.salary_amount} hours at {self.rate}/hour and receives a commission for {self.comission_amount} contract(s) at {self.comission_rate}/contract.  Their total pay is {Employee.get_pay(self)}.'
            elif self.comission_type == 'bonus':
                string = f'{self.name} works on a contract of {self.salary_amount} hours at {self.rate}/hour and receives a bonus commission of {self.comission_amount}.  Their total pay is {Employee.get_pay(self)}.'
        return string

        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie','monthly',4000,0,'',0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', 100, 25, '', 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'monthly', 3000, 0, 'contract comission', 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', 150, 25, 'contract comission', 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', 2000, 0, 'bonus', 1500, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel =  Employee('Ariel', 'hourly', 120, 30, 'bonus', 600, 0)

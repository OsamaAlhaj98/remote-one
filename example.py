class Employee:
    
    def __init__(self,name="",hours_worked=0,rate_of_pay=0):
        self.__name = name
        self.__hours_worked = float(hours_worked)
        self.__rate_of_pay=float(rate_of_pay)
        
    def __str__(self):
        return(f"Name: {self.__name}\n\n"
               f"Hours: {self.__hours_worked}\n"
               f"Rate: ${self.__rate_of_pay}\n"
               f"Gross pay: {self.calc_gross_pay()}")
        
    #getters
    def get_name(self):
        return self.__name
    
    def get_hours_worked(self):
        return self.__hours_worked
    
    def get_rate_of_pay(self):
        return self.__rate_of_pay
    
    #setters
    
    def set_name(self,name):
        self__name = name
        
    def set_hours_worked(self,hours_worked):
        self.__hours_worked = float(hours_worked)
        
    def set_rate_of_pay(self, rate_of_pay):
        self.__rate_of_pay = float(rate_of_pay)
        
    #calculations
        
    def add_hours_worked(self,hours_worked):
        self.__hours_worked += float(hours_worked)
        
    def calc_gross_pay(self):
        return self.__hours_worked*self.__rate_of_pay
    
emp1 = Employee()
emp2 = Employee("Harvey", 0, 11.20)

emp1.set_name("Sara")
emp1.set_hours_worked(40)
emp1.set_rate_of_pay(15)
print("Payroll Report for", emp1.get_name())
print("Hours =", emp1.get_hours_worked())
print("Rate =", emp1.get_rate_of_pay())
print("Total Gross = $", emp1.calc_gross_pay(), sep='')
emp2.add_hours_worked(10)
emp2.add_hours_worked(5)
print("Payroll Report for " + emp2.get_name())
print(emp2)
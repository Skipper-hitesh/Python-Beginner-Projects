class Employee:
    
    language="Python" #This is a class attribute
    salary=1200000

    def getInfo(self):
        print(f"The language is {self.language},The salary is {self.salary}")


    @staticmethod
    def greet(self):
        print("Good morning")    

hitesh=Employee()
# hitesh.language="JavaScript"# This is an instance/object attribute
# print(hitesh.language,hitesh.salary) 

hitesh.getInfo()
Employee.greet(hitesh) 
# Employee.getInfo(hitesh)  #both the functions can be written 


# we have to put a 'self' in method 
 



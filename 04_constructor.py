class Employee:
    
    language="Python" 
    salary=1200000


    def __init__(self,name,salary,language): #  dunder method which is automatically called when you make an object
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")
 
    def getInfo(self):
        print(f"The language is {self.language},The salary is {self.salary}")


    @staticmethod
    def greet(self):
        print("Good morning")    

hitesh=Employee("Hitesh",130000,"Javascript")
hitesh.name="Hitesh"
print(hitesh.name,hitesh.language, hitesh.salary)

# rohan=Employee()


class student: #declares a class student which can be used to create a lot of students
    def __init__(self,name,age,grade,sex,enroll_year):
        self.name = name #name of student
        self.age = age #age of student
        self.grade = grade #grade of student
        self.sex = sex #sex of student
        self.enroll_year = enroll_year #enrollment year of student
    
    def get_descriptive(self): #this function within the class, returns a full description of our student
        full_description = f'I\'m {self.name}, age {self.age}, in {self.grade},I\'m {self.sex} I was enrolled in {self.enroll_year}'
        return full_description

student1 = student('Emmanuella Mensah','24','level 400','female','2018') #student1 is one instance of a student notice how the arguments matches that of the __init__ declaration
print(student1.get_descriptive()) #output: I'm Emmanuella Mensah, age 24, in level 400, I was enrolled in 2018

student2 = student('Ernest Apau','26','level 600','male','2017') #student2 is the 2nd instance
print(student2.get_descriptive()) #output: I'm Ernest Apau, age 26, in level 600,I'm Male I was enrolled in 2017
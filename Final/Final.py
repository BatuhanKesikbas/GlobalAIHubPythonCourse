class Employee():

    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def showInfo(self):

            print("{} is {} years old and knows {}".format(self.name, self.age, self.language))





Person1=Employee("Alican","20","Spanish, English")
Person2=Employee("Mert","20","Turkish, English")
Person3=Employee("İpek","21","Polish, English")
Person4=Employee("Eda","20","Chinese, English")
print("EMPLOYEES")
Person1.showInfo()
Person2.showInfo()
Person3.showInfo()
Person4.showInfo()
print("Languages that known by the employees are:",Person1.language,"--",Person2.language,"--",Person3.language,"--",Person4.language)


class Manager(Employee):
    pass

print("MANAGER")
BOSS= Manager("Batuhan","20","Turkish, English")
BOSS.showInfo()
print("Languages that known by the manager are:",BOSS.language)



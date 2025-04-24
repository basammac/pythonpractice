# class Car:
#     pass
# class Car():
#      model = "Audi A5"
#      color = "black"
#      year  = 2020
#      speed_limit =240
# car1 = Car()
# car2 = Car()
# print(car2)
# print(car1)
# print(car1.model)
# print(car2.speed_limit)
# print(Car.model)
# print(Car.speed_limit)
# dir(car1)

# class Car():
#      model = "Audi A5"
#      color = "black"
#      year  = 2020
#      speed_limit =240
#
#      def __init__(self):
#          print("init function called")
# car2 = Car()
# # print(car2)

# class Car():
#     def __init__(self,model,color,year,speed_limit):
#         self.model = model
#         self.color = color
#         self.year = year
#         self.speed_limit = speed_limit
# car1=Car("bench","white",2019,240)
#
# car2=Car("Telsa roadster","silver",2020,280)
#
# print(car1.model)
# print(car2.model)

class Car():
    def __init__(self,model="No info",color="No info",year=2019,speed_limit=200):
        self.model = model
        self.color = color
        self.year = year
        self.speed_limit = speed_limit

car2=Car(model="bmw")
print(car2.model)
print(car2.color)
print(car2.year)

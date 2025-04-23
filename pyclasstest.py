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

class Car():
     model = "Audi A5"
     color = "black"
     year  = 2020
     speed_limit =240

     def __init__(self):
         print("init function called")
car2 = Car()
# print(car2)

class Car():
    def __init__(self,model,color,speed_limit):
        self.model = model
        self.color = color
        self.year = year
        self.speed_limit = speed_limit




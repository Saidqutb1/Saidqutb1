#1
# def birinchi_vazifa(a):
#     s = 0
#     for i in a:
#         if a.count(i) == 1:
#             s = i
#             break
#     return s
#
# # a = [1, 2, 3, 4, 3, 2, 1]
# # print(birinchi_vazifa(a))
#
# #2
# def ikkinchi_vazifa(a):
#     s = (a % 400 == 0) or ((a % 4 == 0) and (a % 100 != 0))
#     d = 255
#
#     if s and d > 255:
#         d += 1
#
#     v = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if s:
#         v[1] = 29
#
#     oy = 0
#     while d > v[oy]:
#         d -= v[oy]
#         oy += 1
#     return f'{d+1}/{oy+1}/{a}'

# print(ikkinchi_vazifa(2000))
# print(ikkinchi_vazifa(2009))

#3
#Domla, agar xar bir sinfda toq son o'quvchilar bo'lsa shu bola uchin
#ham alohida parta kerak ekan, shuning uchun men sinf uchun qancha parta kerakligini aloxida xisobladim

# a = int(input("-->"))
# b = int(input("-->"))
# c = int(input("-->"))
# a /= 2
# b /= 2
# c /= 2
# if a % 1 != 0:
#     a += 0.5
# if b % 1 != 0:
#     b += 0.5
# if c % 1 != 0:
#     c += 0.5
# s = a + b + c
# print(int(s))

#nametaple vazifalari

# from collections import namedtuple
#1

# Cars = namedtuple('Cars', ('model', 'seria', 'make_year'))
# # cars = Cars('Gentra', '2342adx', '2020')
# # print(cars.model, cars.seria, cars.make_year)
#
# class World_cars(Cars):
#     def __new__(cls, model, seria, make_year, world_cars_id):
#         return super().__new__(cls, model, seria, make_year)
#
#     def __init__(self, model, seria, make_year, world_cars_id):
#         super().__init__(model, seria, make_year)
#         self.world_cars_id = world_cars_id

    # a = Cars('Gentra', '231jlk13', 2020)

    # print(a.model)
    # print(a.seria)
    # print(a.make_year)

#2
from collections import namedtuple

Person = namedtuple('Person', ['name', 'surname', 'age'])
# person = Person('Avazbek', 'Nodirov', 23)
# print(person.name, person.surname, person.age)


class Student(Person):
    def __new__(cls, name, surname, age, student_id):
        return super().__new__(cls, name, surname, age)

    def __init__(self, name, surname, age, student_id):
        super().__init__(name, surname, age)
        self.student_id = student_id

# a = Student('Barot', 'Mominov', 25, 's2233')
# print(a.name)
# print(a.surname)
# print(a.age)
# print(a.student_id)

#3
Planet = namedtuple('Planet', ['name', 'size_ss'])
# planet = Planet('Yupiter', 1)
# print(planet.name, planet.size_ss)

class Solar_sistem:
    def __new__(cls, name, size_ss, solar_sistem_id):
        return super().__new__(cls, name, size_ss)

    def __init__(self, name, size_ss, solar_sistem_id):
        self.solar_sistem_id = solar_sistem_id

a = Solar_sistem('Mars', 6, '212a3')

# print(a.name)
# print(a.size_ss)
# print(a.solar_sistem_id)

#4
Animal = namedtuple('Animal', ['name', 'tipe', 'age'])
# tiger = Animal('Yolbars', 'Tiger', '2')
# print(tiger.name, tiger.tipe, tiger.age)
class World(Animal):
    def __new__(cls, name, tipe, age, animal_id):
        return super().__new__(cls, name, tipe, age)

    def __init__(self, name, tipe, age, animal_id):
        self.animal_id = animal_id

a = Animal('Yolbars', 'Tiger', '2')
# print(a.name)
# print(a.tipe)
# print(a.age)
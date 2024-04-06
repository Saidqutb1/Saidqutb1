#Python dinamic
# from typing import List
#
# def uyga_vazifa_5_1(a: List[int]) -> int:
#     s: int = 0
#     for i in a:
#         if i % 2 != 0:
#             s += 1
#     return s
#
# a: List[int] = [475, 232, 324, 432, 324, 2, 4, 2, 23]
# print(uyga_vazifa_5_1(a))

#Static Python
from typing import List

def uyga_vazifa_5_1(a: List[int]) -> int:
    s: int = 0
    for i in a:
        if i % 2 != 0:
            s += 1
    return s

a: List[int] = [475, 232, 324, 432, 324, 2, 4, 2, 23]
print(uyga_vazifa_5_1(a))




# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in 1, 0:
#     for y in 1, 0:
#         for z in 1, 0:
#             print(f"{x= } {y= } {z= }  {(not(x or y or z)) == (not x) and (not y) and (not z)}")

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'X = {x}, Y={y}, Z = {z}')
            print(not (x or y or z) == (not x, not y, not z))
            print()

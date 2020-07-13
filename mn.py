import random

# magicNumber = 32
# # for n in range(0, 101):
# #     if n is magicNumber:
# #         print(n, "is the magic NUmber!")
# #         break
# #     else:
# #         print(n)


# for x in range(0, 101):
#     if x % 4 == 0:
#         print(x, "are the magic numbers")
#         continue
#     else:
#         print(x)
# print()

# teamNumbers = [2, 5, 9, 13, 16, 17, 20, 23, 25, 29]
#
# for n in range(0, 31):
#     if n in teamNumbers:
#         continue
#     print(n)


# def bitcoin_to_usd(btc):
#     total = btc * 9370
#     print(total)
#
#
# bitcoin_to_usd(0.0065473)
# bitcoin_to_usd(0.09453)def allowed_driving_age(current_age):
# #     drivers_age = current_age / 2 + 10
# #     return drivers_age
# #
# #
# # calx = allowed_driving_age(19)
# # frisk = allowed_driving_age(60)
# # brundle = allowed_driving_age(38)
# # print("Calx is only able to drive if his age is", calx, "at the current time")
# # print("Frisk is only able to drive if his age is", frisk, "at the current time")
# # print("Brundle is only able to drive if his age is", brundle, "at the current time")
# #
# # print()
# bitcoin_to_usd(200)
# bitcoin_to_usd(10)
# print()


#


# def get_gend(gender='Not disclosing'):
#     if gender is 'm':
#         gender = "Male"
#     elif gender is 'f':
#         gender = "Female"
#     print(gender)
#
#
# get_gend()
# get_gend('m')
# get_gend('f')
# print()
#
#
# def add_numbers(*args):
#     total = 0
#     for a in args:
#         total += a
#     print(total)


# add_numbers(1, 4, 7, 9, 23, 54, 26)
# add_numbers(140)
# add_numbers(12, 43, 56, 70)
# print()


# def health_calculator(age, apples_ate, cigs_smoked):
#     answer = (100 - age) + (apples_ate * 3.5) - (cigs_smoked * 2)
#     print(answer)
#
#
# calx_info = [21, 30, 0]
# vrit_info = [40, 10, 3]
# brit_info = [49, 12, 5]
#
# health_calculator(calx_info[0], calx_info[1], calx_info[2])
# health_calculator(*vrit_info)
# health_calculator(*brit_info)
# print()

groceries = {"Rice", "Spaghetti", "Tomato", "Pepper", "Cooking Oil", "Pepper", "Salt"}
print(groceries)

if "Tomato" in groceries:
    print("Hey we've got the sauce")
else:
    print("You missed a major")

Formula_1 = {'Mercedes': 'Lewis Hamilton and Valteri Bottas', 'Ferrari': 'Sebastian Vettel and Charles Leclerc', 'Redbull': 'Max Verstappen and Brandon Hartley'}

print(Formula_1)
print(Formula_1['Redbull'])
print(Formula_1['Ferrari'])

for k, v in Formula_1.items():
    print('Formula 1 team {} with their Two Drivers {}'.format(k, v))

lucky_winner = random.randrange(0, 100,)
print(lucky_winner)

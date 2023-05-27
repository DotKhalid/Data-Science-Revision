# birth_year = 1995
# current_year = 2023
#
# age =  current_year - birth_year
#
# print(age)


# first = "muhammad"
# middle = "khalid"
# last = "khan"
#
# fullname = first + "" + " " + middle + " "+last
#
# print(fullname)

# Exercise Numbers In Python
# Q1
#
field_long = 92
field_wide = 48.8

total_area =  field_long*field_wide

print(total_area)


# Q2

total_packs = 9
cost = 1.49
paid = 20

total_cost =  cost*total_packs

remaining = paid - total_cost

print("shop keeper give me : " , remaining ,"dollar")

#Q3

length = 5.5
area_of_square = length**2
cost = area_of_square *500
print("total cost for bathroom tiles replacement:",cost)


#Strings in Python

# Q1


street = "block 1"
city = "Karachi"
country = "Pakistan"

address = "my address is : "+ "\n" + street + "\n"  +  city + "\n" + country

print(address)

address = f"street : {street} \nCity: {city} \ncountry: {country}"

print(address)


# Q2


str = "Earth revolves Around The sun"

print(str[6:13])

print(str[-3:])


# Q3


no_of_fruits = 5
no_of_veggies = 3

print(f"I eat {no_of_veggies} veggies and {no_of_fruits} fruits daily")


# Q4

s = "maine 200 banana khaye"

new = s.replace("maine 200 banana khaye", "maine 10 samosa khaye")

print(f"old sentences is {s} and new sentence is :{new}")


# Exercise Python List
# Q1


exp = [2200,2350, 2600,2000, 2190]

feb_exp = int(exp[1]) - int(exp[0])

print(" extra spent in Feb is : " ,  feb_exp)

print("Total Expense of First Quarter : " , exp[0]+exp[1]+exp[2])

for index, value in enumerate(exp):
    if 3 in exp:
        print(f"found in {index}")
        break
    else:
        print("I didnt spent exactly 2000")


exp.append(1980)

print(exp)


exp[3]  = exp[3] + 200

print(exp)


# Q2

heros = ['spider man', 'thor' , 'hulk', 'iron man' , 'captain america']


print(len(heros))
print(heros)
heros.insert(3 , 'black panther')


print(heros)

heros[1:3] = ["doctor strange"]

print(heros)



#Exercise: If condition


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# user_input = input("Enter a City name: ")
#
# if user_input in india:
#     print(f"{user_input} is in India")
# elif user_input in pakistan:
#     print(f"{user_input} is in pakistan")
# elif user_input in bangladesh:
#     print(f"{user_input} is in bangladesh")

#
#
# city_1 = input("Enter first city : ")
# city_2 = input("Enter second city")
#
#
# if city_1 and city_2 in india:
#     print("both cities is in inda")
# elif city_1 and city_2 in pakistan:
#     print("both cities is in Pakistan")
# elif city_1 and city_2 in pakistan:
#     print("both cities is in Pakistan")
#
# else:
#     print("They don't belong to same country")
#




for i in range(1,6):
    answer = input("Are you tired : ")
    if answer == "yes":
        print("you didn't finish the race")
        break
    elif answer == "no":
        print(5-i, " km left bhagoo")
    if i == 5:
        print("congratulations you won the race")


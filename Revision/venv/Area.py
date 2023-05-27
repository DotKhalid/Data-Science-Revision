# base = 10
# height  = 5
#
# area =  1/2 * (base*height)
#
# print("Area of triangle is ",area)
#
#

# exp = [2340,2450,2464,3691,5896]
#
# total = 0
#
# for i in range(len(exp)):
#     print("Month: ", (i+1), "Expense: " , exp[i])
#     total= total + exp[i]
#
# print("total expense is :" , total)
#
#


key_location = "chair"
locations = ["garage","living room ","chair","closet"]

for i in locations:
    if i==key_location:
        print("key is found in ", i)
        break
    else:
        print("key is not found in ", i)

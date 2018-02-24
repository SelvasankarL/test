#!/usr/bin/python


#def bmi(a, b):
#	c = a/(pow(b, 2))
#	print (c)
#return c


#height = input("Enter the height: ")
#Weight = input("Enter the waight: ")

#result = bmi(Weight, height)
#print (result)


def calculate_BMI(new_weight, new_height):
    new_bmi = new_weight/(pow(new_height, 2))
    return new_bmi
 
weight = float(input('Enter weight in Kgs'))
height = float(input('Enter height in meters'))
bmi = calculate_BMI(weight, height)
print(bmi)

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 11:22:56 2017

@author: Isaac Ng
"""

def fahrenheit_to_celsius(temp):
    temp = temp - 32.0
    temp = temp * 5
    temp = temp / 9
    return temp

#######################################
def position_velocity(vinit, t):
    posT = (vinit * t) - (4.905 * (t ** 2))
    velT = vinit - (9.81 * t)
    posT = round (posT, 2)
    velT = round (velT, 2)
    return posT, velT

#######################################
def minutes_to_years_days(minutes):
    years = minutes / 525600
    minInDays = minutes % 525600
    days = minInDays / 1440
    return years, days

#######################################
from math import sqrt

class Coordinate:
    x = 0
    y = 0

def area_of_triangle(p1,p2,p3):
    side1 = sqrt(((p1.x-p2.x) ** 2) + ((p1.y-p2.y) ** 2))
    side2 = sqrt(((p2.x-p3.x) ** 2) + ((p2.y-p3.y) ** 2))
    side3 = sqrt(((p3.x-p1.x) ** 2) + ((p3.y-p1.y) ** 2))
    s = (side1 + side2 + side3)/2
    area = sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return area

#######################################
def compound_value_sixth_months(amt, rate):
    month = 0
    rateMonth = rate/12
    final = 0
    while month != 6:
        final = final + amt
        final = final + final*rateMonth
        month = month + 1
    return final

#######################################
def celsius_to_fahrenheit(fahrenheit):
    temp = fahrenheit * 9.0
    temp = temp / 5
    temp = temp + 32
    return temp

#######################################
def area_vol_cylinder(radius, height):
    area = radius * radius * height
    volume = area * length
    return area, height

#######################################
def wind_chill_temp(ta, v)
    index = 35.74+0.6215ta-35.75(v**0.16)+0.4275*ta*(v**0.16)
    return index

#######################################
def bmi(weight,height):
    kg = weight * 0.45359237
    meters = height * 0.0254
    myBMI = kg / meters**2
    return myBMI

#######################################
def investment_val(amount, annualRate, years):
    monthlyRate = annualRate / 1200
    months = years * 12
    futureInvVal = amount*((1+monthlyRate)**months)
    return futureInvVal
print investment_val (1000, 4.25, 1)


#######################################
def exponent(x, a):
    string = "x"
    string = string + ("*x" * a)
    return string















	
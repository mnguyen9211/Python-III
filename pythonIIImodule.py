from math import pi

def area():
    l = float(input("Length?"))
    w = float(input("Width?"))
    
    return l*w

def circumference():
    r = float(input("Radius?"))
    
    return float(2) * pi * r
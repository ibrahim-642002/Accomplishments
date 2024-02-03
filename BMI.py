def bmi():
    weight = float(input(" Please Enter Your Weight In kgs "))
    height = float(input(" Please Enter Your Height in Meters "))
    value = weight / (height ** 2)
    return value


val = bmi()
print(f" your Weight is {val}")
if val < 18.5:
    print(" Under Weight")

elif val >= 18.5 and val < 24.9:
    print(" Normal Weight")

elif val >= 25 and val < 29.9:
    print(" Over Weight")

else:
    print(" Obese")

weight=float(input("Enter the weight :"))
eight=float(input("Enter the height :"))
bmi=weight/(height**2)
if bmi<18.5:
    c="Underweight"
elif bmi<25:
    c="Normal"
else:
    c="Overweight"
print(f"BMI:{round(bmi,1)} Category:{c}")
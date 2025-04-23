#BMI calculating 

print("This is a BMI calculator.\nPlease enter your grade,class,seat number,and name.")
print("(Please press ENTER after each data.)")
Grade=int(input("Grade:"))
Class=int(input("Class:"))
Number=int(input("Seat Number:"))
Name=str(input("Name:"))
print("Please enter your height (meter) and weight (kilogram).")
print("(Please press ENTER after each data.)")
Height=float(input("Height:"))
Weight=float(input("Weight:"))
print("")
print(f"Grade: {Grade}\nClass: {Class}\nSeat number: {Number}\n\
Name: {Name}\nHeight: {Height}\nWeight: {Weight}")
print("Your BMI is %.2f ." % float(Weight / (Height**2)))
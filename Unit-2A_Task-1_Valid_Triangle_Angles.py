angle1 = float(input("Enter first angle in degrees: "))
angle2 = float(input("Enter second angle in degrees: "))
angle3 = float(input("Enter third angle in degrees: "))
if angle1+angle2+angle3 == 180 and angle1 > 0 and angle2>0 and angle3>0 :
    print(f"The triangle with angle {angle1}, {angle2}, and {angle3} is vaild")
else: 
    print(f"The triangle with angle {angle1}, {angle2}, and {angle3} is invaild")

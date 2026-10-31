principal = float(input("Enter principal: "))  
rate = float(input("Enter rate: "))         
time = float(input("Enter year: ")) 
total_amount = principal * (1 + rate / 100) ** time
compound_interest = total_amount - principal
print(compound_interest)

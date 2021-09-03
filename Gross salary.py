print("******GROSS SALARY******")
Basic_Salary=int(input("Enter the basic salary"))
DA=(Basic_Salary *20)/100
HRA= (Basic_Salary * 30)/100
Gross_Salary=Basic_Salary + DA +HRA
print("ALLOWANCE 40 % OF Basic_Salary :",DA)
print("HOUSE RENT 20 % OF Basic_Salary :",HRA)
print("Gross SALARY :",Gross_Salary)
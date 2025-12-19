salary = int(input("Enter the salary: "))
late_days = int(input("Enternumber of late days: "))
absent_days = int(input("Enter number of absent days: "))

final_salary = salary

if late_days > 5:
    late_deduction = final_salary - (final_salary * 0.05)
    final_salary = late_deduction
elif late_days > 10: 
    late_deduction = final_salary - (final_salary * 0.10)
    final_salary = late_deduction
if absent_days > 2:
    absent_deduction = final_salary - (final_salary * 0.05)
    final_salary = absent_deduction

print(final_salary)
    
    
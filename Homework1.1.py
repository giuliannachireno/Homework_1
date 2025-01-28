print("This is a Net Salary Calculator")
def calculate_net_salary():
    try:
        gross = float(input("Enter the gross salary: "))
        gross =  int(gross)
        children = int(input("Enter the number of children: "))
        if gross < 1000:
            tax_rate = 10
        elif gross < 2000:
            tax_rate = 12
        elif gross < 4000:
            tax_rate = 14
        else:
            tax_rate = 18
        if gross < 2000:
            tax_rate -= children * 1
        else:
            tax_rate -= children * 0.5
        tax_rate = max(tax_rate, 0)
        net_salary = gross - (gross * tax_rate / 100)
        print(f"The net salary is: {net_salary:.2f}")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

calculate_net_salary()

print("Thank you for using the calculator")



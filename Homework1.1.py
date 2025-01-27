def calculate_net_salary():
    try:
        # Firstly player should input gross salary and number of children
        gross = float(input("Enter the gross salary: "))
        gross =  int(gross)
        children = int(input("Enter the number of children: "))

        # Then given the constraints in the homework machine will determine the base tax rate
        if gross < 1000:
            tax_rate = 10
        elif gross < 2000:
            tax_rate = 12
        elif gross < 4000:
            tax_rate = 14
        else:
            tax_rate = 18

        # Adjust the tax rate based on the number of children
        if gross < 2000:
            tax_rate -= children * 1  # 1% per child
        else:
            tax_rate -= children * 0.5  # 0.5% per child

        # Tax rate cannot be less than zero if not the person would be earning money from this thus
        # # the following ensures that tax rate is not negative
        tax_rate = max(tax_rate, 0)

        # Finally calculate net salary
        net_salary = gross - (gross * tax_rate / 100)

        print(f"The net salary is: {net_salary:.2f}")

        #in order to prevent any potential problem have this condition
    except ValueError:
        print("Invalid input. Please enter numerical values.")


calculate_net_salary()



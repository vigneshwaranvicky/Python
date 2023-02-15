def calculate_net_salary(basic_salary):

    da = basic_salary * 0.05
    hra = basic_salary * 0.07
    pf = basic_salary * 0.03

    net_salary = basic_salary + da + hra - pf
    return net_salary

basic_salary = float(input("Enter basic salary: "))
net_salary = calculate_net_salary(basic_salary)

print(" DEARNESS ALLOW. : ",basic_salary * 0.05)
print(" HOUSE RENT ALLOW.: ",basic_salary * 0.07)
print(" PERSONAL ALLOW.: ",basic_salary * 0.03)
print("NET SALARY: ", net_salary)

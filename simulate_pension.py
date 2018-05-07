import numpy
import matplotlib.pyplot as plt

"""
Pension simulator to predict what is the actual value of the 
pension reserve by the goverment. 
Parameters to take into account:
1 - total_citizens = number of people living in the country
2 - working_citizens_prop = proportion of working people [0, 1]
3 - non_working_citizens_prop = 1 - working_citizens_prop
4 - retired_citizens_prop = proportion of working people with retirement rights
5 - monthly_pension = int
6 - monthly_salary = int from working citizens
7 - social_security_tax = percentage of monthly salary dedicated to pay retirement
8 - initial_gov_money = 60022000000  # data from Spanish gov from 2009
9 - official_gov_money_2017 = 7100000000
10 - input_money = total ammount contributed to the pension fund
11 - output_money = total ammount deducted from the pension fund
12 - pension_fund = actual ammount of government money to pay pensions
13 - current_year
14 - simulation_year = year up to which you want to simulate
"""

# initial parameters
initial_gov_money = 60022000000
current_year = 2009
simulation_year = 2020
monthly_salary = 1300
social_security_tax = 0.21
monthly_pension = 900

total_citizens = 46560000
working_citizens_total = 23302600
working_citizens_prop = working_citizens_total / total_citizens
print("this is the working proportion {0}".format(working_citizens_prop))
retired_citizens_2009 = 7600000
retired_citizens = retired_citizens_2009
retired_citizens_prop = retired_citizens_2009 / total_citizens
print("this is the total prop of retired {0}".format(retired_citizens_prop))
print("Proportion between Working and Retired is {0}".format(working_citizens_prop / retired_citizens_prop))

x_year = []
y_pension_fund = []
pension_fund = initial_gov_money
while current_year < simulation_year :
    # factors contributing to income on the government fund
    input_money = working_citizens_total * monthly_salary * 12 * social_security_tax # yearly income
    pension_fund += input_money
    # factors contributing to the spending on the government fund
    output_money = retired_citizens * monthly_pension * 12
    pension_fund -= output_money
    y_pension_fund.append(pension_fund / 1000000)
    x_year.append(current_year)
    print("Current value of pension_fund is {0} at year {1}".format(pension_fund / 1000000, current_year))
    current_year += 1
plt.plot(x_year, y_pension_fund)
plt.show()
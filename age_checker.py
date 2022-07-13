

from distutils.sysconfig import customize_compiler


age_year = int(input("Introduce your birth year :"))
current_year = int(2022)

customer_age = current_year - age_year

print("The customer age is :" + (str(customer_age)))

if customer_age > 17:
    print("You can buy this videogame ")
else:
    print("You can not buy this videogame")
#Write the necessary code to display the total population count for the next 3 years (without a leap year).

#Here are the specifications:

#In the country we want to investigate:

#The current population is 380,123,456
#One person is born every 6 seconds
#One person dies every 12 seconds
#One person immigrates every 40 seconds

population = 380123456
seconds_per_year = 31536000
birth_per_year = seconds_per_year // 6
death_per_year = seconds_per_year // 12
immigration_per_year = seconds_per_year // 40
grouth_per_three_years = birth_per_year *3 + immigration_per_year *3 - death_per_year *3
population_after_three_years = population + grouth_per_three_years
print(population_after_three_years)
import datetime

birth_year = 1972
age_begin_work = 1998
if birth_year == 1961 or birth_year == 1962:
    nb_trim = 169
elif birth_year == 1964:
    nb_trim = 170
elif birth_year == 1965:
    nb_trim = 171
else:
    nb_trim = 172

year_retraite = age_begin_work + nb_trim / 4
print(year_retraite)
nb_year_restant = year_retraite - datetime.datetime.now().year
print(nb_year_restant)

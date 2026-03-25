birth_year = 1972

if birth_year == 1961 or birth_year == 1962:
    nb_trimestre = 169
elif birth_year >= 1963 or birth_year <= 1965:
    nb_trimestre = 170
else:
    nb_trimestre = 172

work_age = 24
retraite_age = work_age + nb_trimestre / 4
print(retraite_age)


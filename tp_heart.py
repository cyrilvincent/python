# Ouvrir le fichier data/heart/data_cleaned_up.csv
# Compter combien de patient ont num==0 et num==1
# Calculer le ratio sex/num => pour num=1 quel est le ratio sex=0 et sex=1

import csv
import pickle
import json

with open("data/heart/data_cleaned_up.csv") as f:
    reader = csv.DictReader(f)
    nb_male_ok = 0
    nb_male_ko = 0
    nb_female_ok = 0
    nb_female_ko = 0
    for row in reader:
        sex = int(row["sex"])
        num = int(row["num"])
        if sex == 0 and num == 0:
            nb_female_ok += 1
        elif sex == 1 and num == 0:
            nb_male_ok += 1
        elif sex == 0 and num == 1:
            nb_female_ko += 1
        else:
            nb_male_ko += 1
    print(nb_female_ok, nb_male_ok, nb_female_ko, nb_male_ko)
    print(nb_male_ok / nb_female_ok, nb_male_ko / nb_female_ko)

with open("data/heart/heart.pickle", "wb") as f:
    pickle.dump((nb_male_ok, nb_female_ok, nb_male_ko, nb_female_ko), f)

nb_male_ok = 0

with open("data/heart/heart.pickle", "rb") as f:
    nb_male_ok, nb_female_ok, nb_male_ko, nb_female_ko = pickle.load(f)
    print(nb_male_ok)

dico = {"nb_male_ok": nb_male_ok, "nb_female_ok": nb_female_ok, "nb_male_ko": nb_male_ko, "nb_female_ko": nb_female_ko}
with open("data/heart/hear.json", "w") as f:
    json.dump(dico, f)
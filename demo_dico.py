import datetime

mesures = [
    {
        "id":"xbz007",
        "datetime": datetime.datetime.now(),
        "instrument_id": "voltmetre1",
        "unit": "mV",
        "data": [(0, 34.2), (1, 33.4), (2,42.2)]
    },
    {
        "id":"xbz008",
        "datetime": datetime.datetime(2026,3,17,9,37,0),
        "instrument_id": "voltmetre2",
        "unit": "mV",
        "data": [(0, 34.2), (1, 33.4), (2,42.2)]
    }
]

print(mesures[0]["id"])

# TP
# Afficher la datetime de la 2ème mesure
# Afficher les data du voltmetre2
# Afficher le nb de data du voltmetre2
# Bonus : Afficher la moyenne des mesures des data du voltmetre2
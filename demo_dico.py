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
    },
    {
        "id": "xbz008",
        "datetime": datetime.datetime(2026, 3, 17, 9, 37, 0),
        "instrument_id": "voltmetre2",
        "unit": "mV",
        "data": [(0, 44.2), (1, 43.4), (2, 42.2)]
    }
]

print(mesures[0]["id"])

# TP
# Afficher la datetime de la 2ème mesure
print(mesures[1]["datetime"])
# Afficher les data du voltmetre2

def get_mesure_by_instrument_id(instrument_id: str):
    return [mesure for mesure in mesures if mesure["instrument_id"] == instrument_id]

mesures = get_mesure_by_instrument_id("voltmetre2")
print(mesures[0]["data"])
for mesure in mesures:
    print(mesure["data"])

# Afficher le nb de data du voltmetre2
# Bonus : Afficher la moyenne des mesures des data du voltmetre2
data = mesures[0]["data"]
values = [t[1] for t in data]
print(values)
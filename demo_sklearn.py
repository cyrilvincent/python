import sklearn.preprocessing as pp
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.read_csv("data/heart/data_cleaned_up.csv")
print(df)

scaler = pp.RobustScaler()  # Instancier le scaler
scaler.fit(df)  # Calcul pour chaque colonne la mediane + q25 + q75
df_scale = scaler.transform(df) # Applique le scaling
df_scale = pd.DataFrame(df_scale, columns=df.columns)
print(df_scale)
# print(scaler.inverse_transform(df_scale))

ok = df_scale[df_scale["num"] == 0]
ko = df_scale[df_scale["num"] == 1]

print(f"Age OK: mean: {np.mean(ok["age"])}, std: {np.std(ok["age"])}")
print(f"Age KO: mean: {np.mean(ko["age"])}, std: {np.std(ko["age"])}")
print(f"Sex OK: mean: {np.mean(ok["sex"])}, std: {np.std(ok["sex"])}")
print(f"Sex KO: mean: {np.mean(ko["sex"])}, std: {np.std(ko["sex"])}")
print(f"Chol OK: mean: {np.mean(ok["chol"])}, std: {np.std(ok["chol"])}")
print(f"Chol KO: mean: {np.mean(ko["chol"])}, std: {np.std(ko["chol"])}")
print(f"Thalach OK: mean: {np.mean(ok["thalach"])}, std: {np.std(ok["thalach"])}")
print(f"Thalach KO: mean: {np.mean(ko["thalach"])}, std: {np.std(ko["thalach"])}")







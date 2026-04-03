import pandas as pd
import numpy as np # pip install openpyxl

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.read_csv("data/heart/data_cleaned_up.csv")
print(df)
print(df.corr())

# OK = num==0 df[df["num"]==0]
# KO = num == 1
# np.mean + np.std pour age + sex + chol + thalach

ok = df[df["num"] == 0]
ko = df[df["num"] == 1]

print(f"Age OK: mean: {np.mean(ok["age"])}, std: {np.std(ok["age"])}")
print(f"Age KO: mean: {np.mean(ko["age"])}, std: {np.std(ko["age"])}")
print(f"Sex OK: mean: {np.mean(ok["sex"])}, std: {np.std(ok["sex"])}")
print(f"Sex KO: mean: {np.mean(ko["sex"])}, std: {np.std(ko["sex"])}")
print(f"Chol OK: mean: {np.mean(ok["chol"])}, std: {np.std(ok["chol"])}")
print(f"Chol KO: mean: {np.mean(ko["chol"])}, std: {np.std(ko["chol"])}")
print(f"Thalach OK: mean: {np.mean(ok["thalach"])}, std: {np.std(ok["thalach"])}")
print(f"Thalach KO: mean: {np.mean(ko["thalach"])}, std: {np.std(ko["thalach"])}")


import pandas as pd
import numpy as np
import sklearn.neural_network as nn


class CancerService:

    def __init__(self, path: str):
        self.path = path
        self.data = None
        self.x = None
        self.y = None
        self.model = nn.MLPClassifier((30,30,30), max_iter=2000) # 30 | 30 | 30
        np.random.seed(0)

    def load(self):
        self.data = pd.read_csv(self.path)
        self.x = self.data.drop(["id", "diagnosis"], axis=1).values
        self.y = self.data["diagnosis"]

    def fit(self):
        self.model.fit(self.x, self.y)

    def score(self):
        return self.model.score(self.x, self.y)

    def predict(self, values: list[list[float]]) -> int:
        array = np.array(values)
        result = self.model.predict(array)
        return result[0]


if __name__ == '__main__':
    s = CancerService("data/cancer/data.csv")
    s.load()
    s.fit()
    print(s.score())
    values = [[17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]]
    print(s.predict(values))
    values = [[13.08,15.71,85.63,520,0.1075,0.127,0.04568,0.0311,0.1967,0.06811,0.1852,0.7477,1.383,14.67,0.004097,0.01898,0.01698,0.00649,0.01678,0.002425,14.5,20.49,96.09,630.5,0.1312,0.2776,0.189,0.07283,0.3184,0.08183]]
    print(s.predict(values))





import datetime


class Measure:

    def __init__(self, t: int, unit: str="ms", values: list[float]=[]):
        self.t = t
        self.unit = unit
        self.values = values


class Instrument:

    def __init__(self, name: str,
                 ip: str,
                 state: bool = True,
                 measure_types: list[str] = [],
                 date_calibration: datetime.datetime = datetime.datetime.now(),
                 measures: list[Measure] = []):
        self.name = name
        self.ip = ip
        self.state = state
        self.measure_types = measure_types
        self.date_calibration = date_calibration
        self.measures = measures

    def calibrate(self):
        self.date_calibration = datetime.datetime.now()

    def measure(self, frequency_range: tuple[float, float], nb_point: int=1):
        for i in range(nb_point):
            self.measures.append(Measure(i,"ms",[0,1,2]))


if __name__ == '__main__':
    m1 = Measure(0,"ms",[1,2,3])
    assert m1.t == 0
    i1 = Instrument("Voltmeter", "192.168.0.1")
    i1.measure((0,0.1), 10)
    assert len(i1.measures) == 10


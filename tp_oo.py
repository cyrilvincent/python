import datetime

class Instrument:

    def __init__(self, name: str, ip: str, state: bool = True, measure_types: list[str] = [], date_calibration: datetime.datetime = datetime.datetime.now()):
        self.name = name
        self.ip = ip
        self.state = state
        self.measure_types = measure_types
        self.date_calibration = date_calibration

    def calibrate(self):
        self.date_calibration = datetime.datetime.now()

    def measure(self, frequency_range: tuple[float, float], nb_point: int=1):
        pass


class Measure:

    def __init__(self, t: int, unit: str="ms", values: list[float]=[]):
        self.t = t
        self.unit = unit
        self.values = values


if __name__ == '__main__':
    m1 = Measure(0,"ms",[1,2,3])
    assert m1.t == 0


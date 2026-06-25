gammes = {
    "evo" : {
        "B01" : 700,
        "B02" : 750,
        "B03" : 800
    },
    "pure" : {
        "default" : 850
    },
    "diamond" : {}
}


class Cabine:

    def __init__(self, gamme: str, model: str, capacity: int, screen: bool, skirack: bool, light: bool, color: tuple[int, int, int]):
        self.gamme = gamme
        self.model = model
        self.capacity = capacity
        self.screen = screen
        self.skirack = skirack
        self.light = light
        self.color = color
        self.is_open = False
        self.seats_up = False

    def open_door(self):
        self.is_open = True
    
    def close_door(self):
        self.is_open = False

    def compute_max_weight(self):
        if self.gamme == "diamond":
            total =  self.capacity * 63
        else:
            total = gammes[self.gamme][self.model]   
        if self.skirack:
            total += 50 * self.capacity * 5
        if self.screen:
            total += 150
        return total

if __name__ == "__main__":
    c1 = Cabine(gamme="evo",
                model="B01",
                capacity=10,
                screen=True,
                skirack=True,
                light=False,
                color=(255,0,0))
    c1.open_door()
    print(c1.is_open)
    c1.close_door()
    print(c1.is_open)
    print(c1.compute_max_weight())


    

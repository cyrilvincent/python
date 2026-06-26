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

class Suspente:

    def __init__(self, weight: float, length: float):
        self.weight = weight
        self.length = length



class Cabine:

    nb = 0

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
        Cabine.nb += 1

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
    
    def __del__(self):
        Cabine.nb -= 1


class Vehicle:

    def __init__(self, name: str, cabine: Cabine, suspente: Suspente):
        self.name = name
        self.cabine = cabine
        self.suspente = suspente

    def total_weight(self):
        return self.cabine.compute_max_weight() + self.suspente.weight
    

class Lift:

    def __init__(self, vehicles: list[Vehicle] = []):
        self.vehicles = vehicles

    def total_weight(self):
        return sum([v.total_weight() for v in self.vehicles])
    
    def add_vehicule(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
     

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
    print(f"Nb cabine: {Cabine.nb}")
    c2 = Cabine(gamme="pure",
                model="default",
                capacity=10,
                screen=True,
                skirack=True,
                light=False,
                color=(255,0,0))
    print(f"Nb cabine: {Cabine.nb}")
    # del(c2)
    # print(f"Nb cabine: {Cabine.nb}")
    s1 = Suspente(200, 2.5)
    v1 = Vehicle("Evo", c1, s1)
    print(v1.total_weight())
    v2 = Vehicle("Evo", c2, Suspente(200, 2.5))
    print(v2.total_weight())
    l1 = Lift([v1, v2])
    print(l1.total_weight())


    
# 1 Créer la classe Suspente avec 2 attributs (dont un poids) et 0 méthodes
# 2 Créer la classe Vehicule qui contient 1 cabine + 1 suspente + la méthode total_weight
# 3 Créer la classe Remontee qui contient * vehicule
# 4 Dans Remontee créer la methode total_weight
# Tester

    

class Body:
    def __init__(self, mass, heat_capacity, temperature):
        while mass <= 0:
            mass = float(input("Mass must be greater than 0, enter mass again: "))
        while heat_capacity <= 0:
            heat_capacity = float(input("Heat capacity must be greater than 0, enter again: "))
        while temperature < 0:
            temperature = float(input("Temperature must be 0 or more, enter again: "))
        self.mass = mass
        self.heat_capacity = heat_capacity
        self.temperature = temperature


if __name__ == "__main__":
    body = Body(100, 0.15, 200)

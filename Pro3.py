class Vehicle:
    def speed(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def speed(self):
        return "The car can go up to 150 km/h."


class Bike(Vehicle):
    def speed(self):
        return "The bike can go up to 100 km/h."


class Train(Vehicle):
    def speed(self):
        return "The train can go up to 300 km/h."


def show_speed(vehicle):
    print(vehicle.speed())


# Example usage
if __name__ == "__main__":
    my_car = Car()
    my_bike = Bike()
    my_train = Train()

    show_speed(my_car)   # Output: The car can go up to 150 km/h.
    show_speed(my_bike)  # Output: The bike can go up to 100 km/h.
    show_speed(my_train) # Output: The train can go up to 300 km/h.

from playsound import playsound

class Car:

    def __init__(self,brand,model,speed,places):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.places = places
        self.passengers = []


    def accelerate(self,dif):
        self.speed = self.speed + dif
        return self.speed

    def deccelerate(self,dif):
        self.speed = self.speed - dif
        return self.speed

    def is_stopped(self):
        if self.speed == 0:
            return True
        return False

    def add_passenger(self,person):
        self.passengers.append(person)

    def get_passengers(self):
        return self.passengers

    def is_full(self):
        return len(self.passengers) == self.places

    def is_faster_than(self,car):
        if self.speed > car.speed:
            return True
        return False

    @staticmethod
    def klaxon():
        playsound('klaxon.mp3')

    def __str__(self):
        return self.brand + " " + self.model








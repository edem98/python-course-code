from classes_explanation import Person
from classes.vehicules.automile_classes import Car


def print_passenger(passengers) :
    for passenger in passengers :
        print(passenger)


bmw = Car("bmw", "anaconda", 20, 4)
print(bmw)
ez = Person("ez", "gbo", 35)
ko = Person("Ser", "Kos", 22)
al = Person("Pros", "Alk", 35)
bmw.add_passenger(ez)
bmw.add_passenger(ko)
bmw.add_passenger(al)
print_passenger(bmw.get_passengers())
bmw.klaxon()

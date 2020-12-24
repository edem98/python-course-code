class Person:

    def __init__(self,nom="Raymondo",prenom="Youdi",age=300,taille=150):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.taille = taille

    def get_age(self):
        return self.age

    def get_prenom(self):
        return self.prenom

    def __str__(self):
        return self.nom + " " + self.prenom

serge = Person("kossi","serge",22,173)
prosper = Person("Alikizang","Prosper",24,173)
ez = Person("Gbgogbo","Ez",30,175)
youdi = Person()

print(youdi)
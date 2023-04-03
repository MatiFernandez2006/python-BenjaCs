class Pet:

    def __init__(self, nombre , tipo, golosinas, salud, energia, ruido):
        self.spicke = nombre
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 100
        self.energia = 50
        self. ruido = ruido

    def dormir(self):
        self.energia += 25
        return self

    def comer(self):
        self.energia += 5
        self.salud += 10
        return self

    def jugar(self):
        self.salud += 5
        self.energia -= 15
        return self

    def ruido(self):
        print(self.ruido)

class Ninja:
    def  __init__(self,nombre,apellido,premios,comida_mascota,mascota):
        self .nombre = nombre
        self .apellido = apellido
        self .premios = premios
        self .comida_mascota = comida_mascota
        self .mascota = mascota

        def caminar(self):
         self.mascota.play()
         return self

    def alimentar(self):

        if len(self.comida_mascota) > 0:
            food = self.comida_mascota.pop()
            print(f"alimentar {self.comida_mascota.nombre} {food}!")
            self.comida_mascota.comer()
        else:
            print("Rayos y centellas, Spicke necesita comida")
        return self
    
    my_treats = ['carne','tocino',"basura"]
my_pet_food = ['pizza','galleta']

nibbles = Pet("caballo",['muerde las cosas','es invisible'],"")

benja = Ninja("Adrien","Dion",my_pet_food, nibbles)

benja.feed();
benja.feed();
benja.feed();
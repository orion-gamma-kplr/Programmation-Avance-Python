class Product:
	def __init__(self, cost, price, marque):
		self.cost = cost
		self.price = price
		self.marque = marque
		self.name=type(self).__name__

class Biens Consommation(Product):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Articles Menagers(Biens Consommation):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Meubles(Articles Menagers):
	def __init__(self, materiau, couleur, dimensions, cost, price, marque):
		super().__init__(cost, price, marque)
		self.materiau = materiau
		self.couleur = couleur
		self.dimensions = dimensions

class Canape(Meubles):
	def __init__(self, cost, price, marque, materiau, couleur, dimensions):
		super().__init__(cost, price, marque, materiau, couleur, dimensions)

class Chaise(Meubles):
	def __init__(self, cost, price, marque, materiau, couleur, dimensions):
		super().__init__(cost, price, marque, materiau, couleur, dimensions)

class Table(Meubles):
	def __init__(self, cost, price, marque, materiau, couleur, dimensions):
		super().__init__(cost, price, marque, materiau, couleur, dimensions)

class Appareils Electromenagers(Articles Menagers):
	def __init__(self, capacite, cost, price, marque, materiau, couleur, dimensions):
		super().__init__(cost, price, marque, materiau, couleur, dimensions)
		self.capacite = capacite

class Refrigerateur(Appareils Electromenagers):
	def __init__(self, efficacite, cost, price, marque, materiau, couleur, dimensions, capacite):
		super().__init__(cost, price, marque, materiau, couleur, dimensions, capacite)
		self.efficacite = efficacite

class Lave-vaisselle(Appareils Electromenagers):
	def __init__(self, programme, cost, price, marque, materiau, couleur, dimensions, capacite):
		super().__init__(cost, price, marque, materiau, couleur, dimensions, capacite)
		self.programme = programme

class Lave-linge(Appareils Electromenagers):
	def __init__(self, programme, cost, price, marque, materiau, couleur, dimensions, capacite):
		super().__init__(cost, price, marque, materiau, couleur, dimensions, capacite)
		self.programme = programme

class Ustensiles Cuisine(Articles Menagers):
	def __init__(self, materiaux, cost, price, marque, materiau, couleur, dimensions, capacite):
		super().__init__(cost, price, marque, materiau, couleur, dimensions, capacite)
		self.materiaux = materiaux

class Casserole(Ustensiles Cuisine):
	def __init__(self, diametre, cost, price, marque, materiau, couleur, dimensions, capacite, materiaux):
		super().__init__(cost, price, marque, materiau, couleur, dimensions, capacite, materiaux)
		self.diametre = diametre

class Batterie Cuisine(Ustensiles Cuisine):
	def __init__(self, nombre_pieces, cost, price, marque, materiau, couleur, dimensions, capacite, materiaux):
		super().__init__(cost, price, marque, materiau, couleur, dimensions, capacite, materiaux)
		self.nombre_pieces = nombre_pieces

class Habillement(Biens Consommation):
	def __init__(self, cost, price, marque, materiau, couleur, dimensions, capacite, materiaux):
		super().__init__(cost, price, marque, materiau, couleur, dimensions, capacite, materiaux)

class Vetements(Habillement):
	def __init__(self, taille, couleur, matiere, cost, price, marque, materiau, couleur, dimensions, capacite, materiaux):
		super().__init__(cost, price, marque, materiau, couleur, dimensions, capacite, materiaux)
		self.taille = taille
		self.couleur = couleur
		self.matiere = matiere

class Haut(Vetements):
	def __init__(self, cost, price, marque, materiau, couleur, dimensions, capacite, materiaux, taille, couleur, matiere):
		super().__init__(cost, price, marque, materiau, couleur, dimensions, capacite, materiaux, taille, couleur, matiere)

class Pantalon(Vetements):
	def __init__(self, cost, price, marque, materiau, couleur, dimensions, capacite, materiaux, taille, couleur, matiere):
		super().__init__(cost, price, marque, materiau, couleur, dimensions, capacite, materiaux, taille, couleur, matiere)

class Robe(Vetements):
	def __init__(self, cost, price, marque, materiau, couleur, dimensions, capacite, materiaux, taille, couleur, matiere):
		super().__init__(cost, price, marque, materiau, couleur, dimensions, capacite, materiaux, taille, couleur, matiere)

class Casquette(Habillement):
	def __init__(self, couleur, cost, price, marque, materiau, couleur, dimensions, capacite, materiaux, taille, couleur, matiere):
		super().__init__(cost, price, marque, materiau, couleur, dimensions, capacite, materiaux, taille, couleur, matiere)
		self.couleur = couleur

class Chaussures(Habillement):
	def __init__(self, pointure, cost, price, marque, materiau, couleur, dimensions, capacite, materiaux, taille, couleur, matiere):
		super().__init__(cost, price, marque, materiau, couleur, dimensions, capacite, materiaux, taille, couleur, matiere)
		self.pointure = pointure


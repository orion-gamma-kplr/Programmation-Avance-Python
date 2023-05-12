# Vous allez créer une classe InventoryProductEntry qui a pour role 
# de représenter une entrée d'inventaire pour un produit spécifique.
import sys,os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from classes.product_classes import Product

class InventoryProductEntry:
    
    # Initialisation de la classe, en prenant en argument un objet Product et une quantité initiale
    def __init__(self, product:Product, quantity=0,sales=0.0,expenses=0.0):
        """
        'product' : un objet de type produit qui rassemble les différents attributs et caractéristiques de ce dernier
        'quantity' : un entier qui représente le nombre des pièces du produit en question
        """
        # Initialisation des variables
        """
        Vous devez initialiser deux variables. 
        la variable 'sales' qui stocke le total des revenues des ventes du produit
        la variable 'expenses' qui stocke le total des dépenses pour restocker le produit
        sales
        """
        self.product=product
        self.stock=quantity
        self.sales=sales
        self.expenses=expenses

    #Méthode Sell
    """
    La méthode sell est utilisée pour retirer la quantité vendue du produit depuis le stock.
    Elle met également à jour les ventes totales pour le produit.    
    """
    def sell(self, quantity):
        #Avant de mettre à jour l'état du stocke du produit, on doit vérifier si on a déjà une quantité suffisante à vendre.

        if (self.stock < quantity):     #SI la quantité en stock est inférieure à la quantité demandée:
            print(f"Le stock du produit {self.product.marque} est insuffisant.")    # Afficher "Le stock du produit [nom du produit] est insuffisant."
            return False    # Retourner Faux
        else: #SINON:
            self.stock-=quantity  #Réduire la quantité en stock par la quantité demandée
            self.sales+=quantity*self.product.price # Ajouter le revenue total de la vente à la variable 'sales' en multipliant la quantité vendue par le prix du produit
            return True # Retourner Vrai    
    
    #Méthode Restock
    """
    La méthode restock est utilisée pour augmenter la quantité en stock lorsqu'un nouveau stock de produit est reçu. 
    Elle met également à jour les dépenses totales pour restocker ce produit.
    """
    def restock(self, quantity):
        self.stock+=quantity  #Ajouter la quantité reçue à la quantité en stock
        self.expenses+=quantity*self.product.cost #  Ajouter le coût total de la nouvelle quantité reçue  à la variable 'expenses' en multipliant la quantité reçue par le coût du produit

    #Méthode repr
    """
    La méthode repr est utilisée pour fournir une représentation en chaîne de caractères de l'objet InventoryProductEntry, 
    qui contient des informations utiles telles que le nom du produit, la marque, la quantité en stock et le prix du produit.

    """
    def __repr__(self):
        # Retourner une chaîne de caractères formatée contenant le nom du produit, la marque, la quantité en stock et le prix du produit.
        return f"name : {self.product.name} marque : {self.product.marque} quantité : {self.stock} prix : {self.product.price}"
    
def main():
# Début
    print("DEBUT")

# Initialisation des variables
    p1 = Product(100,200,"SIESTA")
    IEP1= InventoryProductEntry(p1,10)
    print(IEP1.__repr__())
    print(IEP1.sell(500))
# Enregistrement dans un fichier
    print(IEP1.__repr__())

# Fin
    print("FIN")

# Appeler la méthode generate_class_hierarchy pour générer le code des classes automatiquement en se basant sur le dictionnaire json_dict
# Stocker le résultat de la classe dans une variable
# Appeler la fonction write_content pour stocker le code des classes dans un fichier Python 'product_classes.py'

# Appeler la fonction principale
if __name__ == '__main__':
    main()
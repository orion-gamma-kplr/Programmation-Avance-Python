# La classe ProfitTracker est utilisée pour suivre les profits du magasin.
import sys,os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import des classes à tester
from classes.product_classes import Product

#from inventory.inventory_manager import InventoryManager
#from inventory.inventory_product_entry import InventoryProductEntry

class ProfitTracker:

    # Le constructeur initialise la variable balance (solde)
    def __init__(self,balance=1000):
        # Créer une variable 'balance' et l'initialiser à 1000 euros
        self.balance=balance
    
    #Méthode buy_product 
    """   
        La méthode buy_product est utilisée pour acheter un produit et mettre à jour le coût total et le solde.
    """     
    def buy_product(self, product: Product, quantity): 
        """
        Vérifie si le solde est suffisant pour acheter la quantité demandée de produit
            Si le solde est insuffisant:
                affiche un message d'erreur 
                retourne False pour indiquer que l'achat a échoué.
            Sinon, si le solde est suffisant:
                met à jour le solde en soustrayant le coût du produit multiplié par la quantité achetée
                retourne True pour indiquer que l'achat a réussi
        """
        solde=product.cost*quantity
        if (solde > self.balance):
            print(f"L'achat de {quantity} unité(s) du produit {product.name} pour un coût unitaire de {product.cost} n'est pas possible pour une balance de {self.balance}")
            return False
        else:
            self.balance-=solde
            return True

# Méthode sell_product 
    """   
        La méthode sell_product est utilisée pour vendre un produit et mettre à jour le solde.
    """
    def sell_product(self, product: Product, quantity):
        self.balance+=product.price*quantity
    # Met à jour le solde en ajoutant le prix du produit multiplié par la quantité vendue

# Fonction principale
def main():
# Initialisation des variables
    p1 = Product(100,200,"SIESTA")
    pt = ProfitTracker()
    vente=pt.buy_product(p1,1)
    print(vente)
    pt.sell_product(p1,1)
    print(pt.balance)

# Appeler la fonction principale
if __name__ == '__main__':
    main()

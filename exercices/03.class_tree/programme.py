# Import des modules nécessaires
import json
import os
from unidecode import unidecode
from treelib import Tree


def json_dict_from_file():
# Get the directory path of the current Python file
    local_path = os.path.dirname(os.path.abspath(__file__))
# Chargement des données JSON à partir du fichier dans un dictionnaire python
    json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
# il est nécessaire de reconvertir le dictionnaire en chaine de caractere pour le traiter ensuite
    json_str = json.dumps(json_data)
# Utilisation de la fonction unidecode pour enlever les accents et autres caractères spéciaux
    json_data = (unidecode(json_str))
# Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python
# Le dictionnaire python est plus pratique à manipuler que la chaine de caractère car il est structuré
    return json.loads(json_data)

# Fonction pour créer un arbre à partir d'un dictionnaire Python
def create_tree_from_dict(tree, parent_node_id, parent_dict):
    for key, value in parent_dict.items():
        if isinstance(value, dict):
# Créer un nouveau noeud pour la clé courante du dictionnaire
            if (key == "subclasses"):
                new_node_id = f"{parent_node_id}"
            else:
                new_node_id = f"{parent_node_id}.{key}"
                tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)

            # Créer récursivement le sous-arbre pour le dictionnaire courant
            create_tree_from_dict(tree, new_node_id, value)

#
# Main
#
def main():
# On charge le dictionnnaire
    json_dict=json_dict_from_file()

# On construit l'arbre
    my_tree = Tree()
    my_tree.create_node(tag="Racine", identifier="racine")
    create_tree_from_dict(my_tree, "racine", json_dict)
    my_tree.show()
    

# Appeler la fonction principale
if __name__ == '__main__':
    main()
import requests
from unidecode import unidecode
from bs4 import BeautifulSoup as bs

url="https://www.annonces-legales.fr"
url_consultation=url+"/consultation/numero_page?department=&newspaper=les-echos-judiciaires-girondins&form="

def main():

# Première consultation du site
        reponse = requests.get(url_consultation.replace('/numero_page',''))
        if reponse.ok:
                soup = bs(reponse.text,'lxml')

#-----------------------#
# Ouverture du stockage #
#-----------------------#
        with open("annonces_legales.csv","w") as file:
                file.write('date;societe;journal;typologie;href;texte\n')

#--------------------------------#
# Traitement de la première page #
#--------------------------------#
# Récupération de la première consultation du site
                annonce=recuperer_annonces(soup)

# On enregistre l'annonce dans le fichier de sortie
                file.write(annonce)

#--------------------------#
# Gestion de la pagination #
#--------------------------#
                pages=soup.findAll('a',{'class':'page-numbers'})
                pagination=0
                for page in pages:
                        if len(page.text) > 0:
                                if (int(page.text)>pagination):
                                        pagination=int(page.text)

# Parcours des autres pages
                for numero_page in range(2,pagination+1):
                        print(numero_page)
# Autres consultations du site
                        reponse = requests.get(url_consultation.replace('numero_page',str(numero_page)))
                        print(reponse.status_code)
                        if reponse.ok:
                                soup = bs(reponse.text,'lxml')
                                annonce=recuperer_annonces(soup)
# On enregistre l'annonce dans le fichier de sortie
                                file.write(annonce)

def recuperer_annonces(soup:bs):

# Initialisation des variables
        retour=""

#---------------------------#
# Récupération des annonces #
#---------------------------#
        trs=soup.findAll('tr',{'class':'tr__action'})

# Parcours des annonces légales
        for tr in trs:
#-------------------------------------#
# Informations générales de l'annonce #
#-------------------------------------#
                a=tr.find('a',{'class':'homepage-link text-decoration-none'})
# Nom de la société
                content=a.text.lstrip().rstrip()
# lien vers détail de l'annonce
                href=a['href']
# Date de parution
                date=tr.find('td',{'class':'mdc-typography--caption'}).text.lstrip().rstrip()
# Le reste de la ligne
                reste=tr.findAll('td',{'class':'mdc-typography--body2'})
# -> Le journal
                journal=reste[2].text.lstrip().rstrip()
# -> Typologie de l'annonce
                typologie=reste[3].text.lstrip().rstrip()

#--------------------#
# Texte de l'annonce #
#--------------------#
                detail=""
                annonce = requests.get(url+href)
                if annonce.ok:
                        soup = bs(annonce.text,'lxml')
                        divs=soup.findAll('div',{'class':'ad-text-wrapper'})
                        detail=str(divs[0].text).lstrip().rstrip()         
# On prépare le résultat
                        retour+=str(date+";"+content+";"+journal+";"+unidecode(typologie)+";"+url+href+";"+unidecode(detail)+"\n")

# On retourne l'information
        return(retour)

#------#
# Main #
#------#

main()
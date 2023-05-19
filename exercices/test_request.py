#import requests
from fastapi import FastAPI
import uvicorn

# xkcd
#url="https://xkcd.com/353/"
#url_img="https://imgs.xkcd.com/comics/python.png"

# httpbin.org
url="https://httpbin.org/get"
url_parameters={'page':2,'count':25}


app=FastAPI()

@app.get("/")
async def hello_world() -> dict[str,str]:
    return {"Hello":"world"}

"""
class API_Rest:

    def requete_get(self,requete : str,parameters : str = ""):
        if (len(parameters) > 0):
            return requests.get(str(requete),params=parameters) 
        else:
            return requests.get(str(requete)) 


def main():
    api=API_Rest()
    r=api.requete_get(url,url_parameters)

    print(r.status_code)

    if (r.status_code==200):
        for key,value in r.headers.items():
            print (f"clé: {key} valeur: {value}") 
        print(r.text)
#        with open('comics.png','wb') as file:
#            file.write(r.content)

main()
"""
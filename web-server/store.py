import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    categories =r.json() #esto es transformar en una lista para que python lo reconozca como lista con diccionarios y poder iterarlos
    for category in categories:
        print(category ['name'])


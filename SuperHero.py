import requests
from pprint import pprint
url = 'https://akabab.github.io/superhero-api/api/all.json'

def get_intelligence(url, names):
    super_heroes = {}
    web = requests.get(url).json()
    for superhero in names:
        name = superhero.capitalize()
        for s_h in web:
            if s_h['name'] == name:
                super_heroes[name] = s_h['powerstats']['intelligence']

    max_intelligence = max(super_heroes.values())
    for hero, intelligence in super_heroes.items():
        if max_intelligence == intelligence:
            return f'Супергерой "{hero}" самый умный и имеет интеллект - {intelligence}'


if __name__ == '__main__':
    print(get_intelligence(url, ['Hulk', 'Superman', 'Thanos']))




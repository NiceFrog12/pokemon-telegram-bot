from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hitpoints = self.get_stats()[0]
        self.attack = self.get_stats()[1]
        self.type_slot_1 = self.get_stats()[2]
        self.type_slot_2 = self.get_stats()[3]
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Pikachu (image search fail)"

    def get_stats(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['stats'][0]['base_stat'] , data['stats'][1]['base_stat'], data["types"][0]['type']['name']#,data["types"][1]['type']['name']
        else:
            return "Pikachu"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def show_stats(self):
        return f"your pokemon has {self.hitpoints}hp and {self.attack} attack. The pokemon types are {self.type_slot_1} and {self.type_slot_2}"




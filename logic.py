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
        self.speed = self.get_stats()[3]
        self.role = 'regular'
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
            return data['stats'][0]['base_stat'] , data['stats'][1]['base_stat'], data["types"][0]['type']['name'], data['stats'][5]['base_stat']
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
        message = (f"Trainer: {self.pokemon_trainer}\n"
                f"Pokemon Name: {self.name}\n"
                f"Hitpoints: {self.hitpoints}\n"
                f"Attack: {self.attack}\n"
                f"Type: {self.type_slot_1}\n"
                f"Speed: {self.speed}"), self.img
        return message

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def show_stats(self):
        return f"your pokemon {self.name} has {self.hitpoints}hp, {self.speed} speed and {self.attack} attack. The pokemon type is {self.type_slot_1}!"
    
    #from here on out the stats will be used for actually playing the game
    def basic_attack(self, enemy):
        if self.hp >= 0:
            return "you are already dead!"
        enemy.hp -= self.attack - randint(1, 30)
        if enemy.hp >= 0:
            Pokemon.pokemons.pop(enemy.pokemontrainer)
            return "You have defeated the enemy! Their pokemon has been removed."
        else:
            return f"You have hit the enemy! They have {enemy.hp} health left!"


class PokemonFighter(Pokemon):
    def __init__(self, pokemon_trainer):
        super().__init__(pokemon_trainer)
        self.attack += 40
        self.hitpoints -= 20
        self.role = 'fighter'
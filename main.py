import telebot 
from config import token
import random
from logic import Pokemon, PokemonFighter

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, pokemon.show_stats())
        randomizer = random.randint(1,2)
        if randomizer == 1:
            bot.send_message(message.chat.id, "Your pokemon has been assigned the fighter role!")
            Pokemon.pokemons[message.from_user.username].role = 'fighter'
            print(Pokemon.pokemons)
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack', 'fight'])
def fight(message):
    if message.reply_to_message:
        my_username = message.from_user.username
        enemy_username = message.reply_to_message.from_user.username

        if my_username not in Pokemon.pokemons:
            bot.send_message(message.chat.id, "You don't seem to have a pokemon. Try using /go")
            return
        if enemy_username not in Pokemon.pokemons:
            bot.send_message(message.chat.id, "Your enemy doesn't have a pokemon. Have some mercy!")
            return
        my_pokemon = Pokemon.pokemons[my_username]
        enemy_pokemon = Pokemon.pokemons[enemy_username]
        bot.send_message(message.chat.id, f"And so the fight beings! {my_pokemon.basic_attack(enemy_pokemon)}")
    else:
        bot.send_message(message.chat.id, "You need to reply to the message of the person you're trying to fight.")

@bot.message_handler(commands=['info', 'pokemon'])
def information(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info()[0])
        if pok.role == 'fighter':
            bot.send_message(message.chat.id, "Your Pokemon is also a fighter, which makes it's stats in battle modified!")
        bot.send_photo(message.chat.id, pok.info()[1])
    else:
         bot.send_message(message.chat.id, "You don't have a pokemon yet. Use the /go command to obtain one!")        


@bot.message_handler(commands=['feed', 'food'])
def feed(message):
    bot.send_message(message.chat.id, Pokemon.pokemons[message.from_user.username].feed())


bot.infinity_polling(none_stop=True)
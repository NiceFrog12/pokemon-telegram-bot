import telebot 
from config import token
import random
from logic import Pokemon, PokemonFighter

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, pokemon.show_stats())
        randomizer = random.randint(1,2)
        if randomizer == 1:
            bot.send_message(message.chat.id, "Your pokemon has been assigned the fighter role!")
            pokemon = PokemonFighter(message.from_user.username)
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
        bot.send_message(message.chat.id, f"And so the fight beings! {my_pokemon.attack(enemy_pokemon)}")
    else:
        bot.send_message(message.chat.id, "You need to reply to the message of the person you're trying to fight.")
bot.infinity_polling(none_stop=True)


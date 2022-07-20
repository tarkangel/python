import string
import random

#This is a simple password generator 8 digits longs that includes upper characters, lower 
# characters,numbers and special characters


def passwordGenerator():
        character = 'abcdefghijklmnopqrstuvwxyz'
        numbers = ('1','2','3','4','5','6','7','8','9','0')
        special_character = '!@#$%^&*()-=+_'

        password = (random.choice(character) 
        + random.choice(character.upper()) 
        + random.choice(numbers) 
        + random.choice(character) 
        + random.choice(character.upper()) 
        + random.choice(special_character) 
        + random.choice(special_character) 
        + random.choice(character.upper())
        )

        print('The password is : ' + password )


def run():
    passwordGenerator()

    

if __name__ == '__main__':
    run()




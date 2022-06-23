import random

def password_generator():
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 
    'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 
    'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 
    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 
    'y', 'z']
    numbers = ['1', '2', '3', '4', '5', 
    '6', '7', '8', '9', '0']
    symbols = ['*', '+', '-', '/', '@', '_', '?', 
    '!', '[', '{', '(', ')', '}', ']', ',', ';', 
    '.', '>', '<', '~', '°', '^', '&', '$', '#', 
    '"']
    characters = capital_letters + lowercase + numbers + symbols 
    
    password = []
    
    quantity = int(input("With how many characters you want your password: "))

    for i in range(quantity): 
        
        character_random = random.choice(characters) 
        password.append(character_random) 
    password = ''.join(password) 
    
    return password 


def run():
    password = password_generator()
    print('Your new password is: ' + password)
if __name__ == '__main__':
    run()
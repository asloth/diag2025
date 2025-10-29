import random

def generate_random_numbers():
    """Generate a list of n random numbers between start and end."""
    return random.randint(1, 100) 

def calculate_distance(guess:int, random_number:int) -> int:
    """Calculate the distance between the guessed number and the random number."""
    return abs(guess - random_number)


def game():
    """Main game loop to guess the random number."""
    random_number = generate_random_numbers() 
    
    player_name = str(input("Bienvenido, ingresa tu nombre: "))
    
    print(f"Hola {player_name}, he generado un número aleatorio entre 1 y 100.")
    print("Intenta adivinarlo.")
    number_of_attempts = 0
    while True:
        try:
            guess = int(input("Ingresa tu suposición: "))
            number_of_attempts += 1
    
            if guess == 0:
                print(f"No lo lograste a pesar de tratar {number_of_attempts} veces. Mas suerte para otra vez.")
                break
            
            if guess < 1 or guess > 100:
                print("Por favor, ingresa un número entre 1 y 100.")
                continue
            
            distance = calculate_distance(guess, random_number) 
            if distance == 0:
                print( f"Felicitaciones {player_name}, lo lograste en {number_of_attempts} intentos.")
                break
            elif distance <= 5:
                print( f"Sorry {player_name}, ese no es pero estas a una distancia menor igual a 5.")
            elif distance <= 10:
                print( f"Sorry {player_name}, ese no es pero estas a a una distancia mayor a 5 y menor igual que 10.")
            elif distance <= 20:
                print( f"Sorry {player_name}, ese no es pero estas a una distancia mayor a 10 y menor igual que 20.")
            else:
                print( f"Sorry {player_name}, ese no es pero estas a una distancia mayor a 20.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

if __name__ == "__main__":
    game()

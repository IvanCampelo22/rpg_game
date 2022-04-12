import random

título = str("Game")

opções = ("""
         Start Game
         Configurações
         Load
         """)
       
class Char_Status:
    def __init__(self, life):
        self.life = life
        self.punch = 10
        self.kick = 5
        self.sword = 30
        self.sword_head = 100
        self.axe = 40
        self.axe_head = 100
        self.critical_damage = 50
            
character = Char_Status(100)
print(f"Life Personal: {character.life}") 

class Enemy_Perfil:
    def __init__(self, life):
        self.life = life
    
       
enemy = Enemy_Perfil(100)
print(f"Life Enemy: {enemy.life}")

if __name__ == "__main__":

    def hit_punch():
        life_enemy = enemy.life
        punch_character = character.punch
        damage = life_enemy - punch_character
        life_enemy = damage
        return life_enemy
   
    def hit_kick():
        life_enemy = enemy.life
        kick_character = character.kick
        damage = life_enemy - kick_character
        life_enemy = damage
        return life_enemy
   
    def combat():
        print("Ataque!!!")
        print("""
        1. Chute
        2. Soque
        """)
        escolha = int(input())
        if escolha == 1:
            print(hit_kick())
        elif escolha == 2:
            print(hit_punch())
        else:
            print("Ataque seu adversário antes que seja tarde demais, seu idiota!!!")
            return combat
       
    print(combat())
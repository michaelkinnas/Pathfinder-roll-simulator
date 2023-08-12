import random
import time

class Character:
    def __init__(self, armor_class, hp, alive=True, immortal=False):
        self.armor_class = armor_class 
        self.hp = hp

        self.alive = alive
        self.immortal = immortal

    def get_AC(self):
        return self.armor_class
    
    def get_HP(self):
        return self.hp
    
    def is_alive(self):
        return self.alive

    def damage_hp(self, value):
        self.hp -= value
        if self.hp < 0:
            self.alive = False

    def get_attack_roll(self, attack_modifier=0):
        return random.randint(1,20) + attack_modifier
    
    def get_attack_damage(self, dice, damage_modifier=0):
        result = 0
        for i in range(int(dice[0])):
            result += random.randint(1, int(dice[2])) 
        return result + damage_modifier
    
def battle_simulaton(character_a, character_b):
    turn = 0
    char_a_hits = 0
    char_a_damage_done = 0
    char_b_hits = 0
    char_b_damage_done = 0

    while True:
        turn += 1
        print(f'Turn {turn} \n')
        time.sleep(2)
        print(f'Character A is attacking....')
        time.sleep(1)
        roll = character_a.get_attack_roll(+8)        
        if roll >= character_b.get_AC():
            print(f'HIT! Attack roll of {roll} hits opponent with AC{character_b.get_AC()}!')
            time.sleep(1)
            char_a_hits += 1
            dmg = character_a.get_attack_damage('2d6', +3)            
            character_b.damage_hp(dmg)
            char_a_damage_done += dmg
            print(f'Damage done: {dmg} on character B which now has {character_b.get_HP()} HP left')
            time.sleep(1)
            if not character_b.is_alive():
                break 
        else:
            print(f'MISS! Attack roll of {roll}, misses opponenet with AC{character_b.get_AC()}!')

        print(f'Character B is attacking....')
        time.sleep(1)
        roll = character_b.get_attack_roll(+7)
        if roll >= character_a.get_AC():
            print(f'HIT! Attack roll of {roll} hits opponent with AC{character_a.get_AC()}!')
            time.sleep(1)
            char_b_hits += 1
            dmg = character_b.get_attack_damage('2d6', +5)           
            character_a.damage_hp(dmg)
            char_b_damage_done += dmg
            print(f'Damage done: {dmg} on character A which now has {character_a.get_HP()} HP left')
            time.sleep(1)
            if not character_a.is_alive():
                break
        else:
            print(f'Attack roll of {roll}, misses opponenet with AC {character_a.get_AC()}!')

    print(f'Battle took {turn} turns')
    print(f'Character A hit his opponent {char_a_hits} times for a total damage of {char_a_damage_done} and has {character_a.get_HP()} hp left.')
    print(f'Character B hit his opponent {char_b_hits} times for a total damage of {char_b_damage_done} and has {character_b.get_HP()} hp left.')


def roll_stats(character_a, character_b, roll_number, attack_bonus, dice, damage_bonus):
    successfull_hits = 0
    total_damage = 0    
    
    for i in range(roll_number):
        roll = character_a.get_attack_roll(attack_bonus)        
        if roll >= character_b.get_AC():           
            successfull_hits += 1
            dmg = character_a.get_attack_damage(dice, damage_bonus)
            total_damage += dmg
    
    hit_rate = "{0:.2f}".format(successfull_hits / roll_number * 100)
    print(f'Character A with +{attack_bonus} attack bonus and +{damage_bonus} damage bonus against AC{character_b.get_AC()}')
    print(f'{successfull_hits} successfull hits out of {roll_number} attack rolls for a total damage of {total_damage}')
    print(f'{hit_rate}% hit rate')
    return successfull_hits, total_damage, hit_rate


# battle_simulaton(character_a, character_b)

character_a = Character(armor_class=20, hp=50)
character_b = Character(armor_class=26, hp=50)

roll_stats(character_a, character_b, 1000000, attack_bonus = +8, dice = '2d6', damage_bonus = +3)
roll_stats(character_a, character_b, 1000000, attack_bonus = +7, dice = '2d6', damage_bonus = +5)
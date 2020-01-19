import csv
import random
import numpy as np
from character import Character
from army import Army

def main():
    characters_list = []
    armies_list = []
    total_moral = 0
    armies_moral = np.zeros(5)
    chiefs_moral = np.zeros(5)

    with open('characters.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for line in csv_reader:
            if line_count != 0:
                new_character = Character(line[0], line[1], line[2], line[3], line[4])
                characters_list.append(new_character)
                chiefs_moral[line_count - 1] = new_character.moral_boost
            line_count += 1

    i = 0
    for character in characters_list:
        new_army = Army(character, random.uniform(20, 100))
        armies_list.append(new_army)
        army_total_moral = new_army.get_total_moral()
        print(army_total_moral)
        total_moral += army_total_moral
        armies_moral[i] = new_army.moral_base
        i += 1
    
    print("Moral : {}".format(total_moral))

    total_moral_numpy = np.dot(armies_moral, chiefs_moral)
    print("Moral NumPy : {}".format(total_moral_numpy))
    
if __name__ == "__main__":
    main()

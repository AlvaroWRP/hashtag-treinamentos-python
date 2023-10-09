import random
from numpy.random import choice

def current_state():
    print('\nRoom:    ', end='')

    for i in range(len(rooms)):
        print(f'{chr(65 + i)}', end=' ')

    print('\nDirty:   ', end='')

    for i in range(len(rooms)):
        if rooms[i] == 0:
            print('_', end=' ')

        if rooms[i] == 1:
            print('x', end=' ')

        if rooms[i] == 2:
            print('O', end=' ')

    print('\nCleaner: ', end='')

    for i in range(len(rooms)):
        if i == cleaner_position:
            print('X', end=' ')

        else: print('_', end=' ')

    print('\n')

while True:  # checagem da quantidade de salas e salas com lixo
    rooms_number = int(input('Total of rooms (1 - 10): '))

    if rooms_number > 0 and rooms_number < 11:
        dirty_rooms_number = int(input('Total of dirty rooms (0 - total of rooms): '))

        if dirty_rooms_number < 0 or dirty_rooms_number > rooms_number:
            print('\nThe number of dirty rooms should be within the same range of the rooms you set...\n')

        else: break
    
    else: print('\nYou must choose a number of rooms between 1 and 10...\n')

rooms = [0] * rooms_number
dirty_rooms = [1] * dirty_rooms_number

for _ in range(rooms_number - dirty_rooms_number):
    obstacle_position = random.randint(0, rooms_number - 1)
    rooms[obstacle_position] = 2

for index, value in zip(choice(range(len(rooms)), size=len(dirty_rooms), replace=False), dirty_rooms):
    rooms[index] = value

cleaner_position = random.randint(0, rooms_number - 1)

while True:
    current_state()

    if 1 not in rooms:
        print('\nAll clean, well done!')
        break

    user_choice = int(input('1 - Move cleaner | 2 - Clean room | 3 - Remove obstacle | 4 - Exit program: '))

    if user_choice == 1:
        direction = input('\nMove cleaner to (L)eft or (R)ight? ')

        new_dirty_room = random.randint(0, rooms_number - 1)
        new_dirty_room_chance = random.random()

        if new_dirty_room_chance <= 0.2:
            if rooms[new_dirty_room] != 0:
                pass

            else:
                rooms[new_dirty_room] = 1
                print('\nA room got dirty again...')

        if direction.lower() == 'l':
            cleaner_position -= 1

            if cleaner_position < 0:
                print('\nThere are no doors to the left here, go back...')
                cleaner_position += 1

            elif rooms[cleaner_position] == 2:
                print('\nThere is an obstacle blocking your way, get rid of it!')
                cleaner_position += 1

        elif direction.lower() == 'r':
            cleaner_position += 1
            
            if cleaner_position > len(rooms) - 1:
                print('\nThere are no doors to the right here, go back...')
                cleaner_position -= 1

            elif rooms[cleaner_position] == 2:
                print('\nThere is an obstacle blocking your way, get rid of it!')
                cleaner_position -= 1

        else: print('\nInvalid direction...')

    elif user_choice == 2:
        if rooms[cleaner_position] == 1:
            print('\nRoom cleaned!')
            rooms[cleaner_position] = 0

        else: print('\nThis room is already clean!')

    elif user_choice == 3:
        if rooms[cleaner_position - 1] == 2:
            print('\nObstacle removed!')
            rooms[cleaner_position - 1] = 0

        elif rooms[cleaner_position + 1] == 2:
            print('\nObstacle removed!')
            rooms[cleaner_position + 1] = 0

    elif user_choice == 4:
        print('\nTerminating process...')
        break

    else: print('\nInvalid option...')

import os
from random import randint, choice
from time import sleep

tiles = randint(5, 15)
random_movement = randint(1, 2)


class Floor:
    def __init__(self, size, stage_list, stains_floor, position, move):
        self.size = size
        self.stage = stage_list
        self.stains_floor = stains_floor
        self.position = position
        self.move = move

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_stage_list(self):
        return self.stage

    def set_stage_list(self, stage_list):
        self.stage = stage_list

    def get_stains_floor(self):
        return self.stains_floor

    def set_stains_floor(self, stains_floor):
        self.stains_floor = stains_floor

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def move_left(self):
        self.position -= 1

    def move_right(self):
        self.position += 1

    def get_move(self):
        return self.move

    def set_move(self, move):
        self.move = move


class Funcion:
    @staticmethod
    def clean_up():
        print('Floor cleaned')

    @staticmethod
    def clean_floor():
        print('The floor is already clean')

    @staticmethod
    def floor_not_cleanable():
        print('The floor cannot be cleaned here')

    @staticmethod
    def stage(tiles):
        return [x for x in range(tiles)]

    @staticmethod
    def position_initial(tiles):
        return choice(tiles)

    @staticmethod
    def generate_floor(tiles):
        floor = []
        state = [' ', '+', 'x', '#']

        for i in range(tiles):
            floor.append(choice(state))
        return floor

    @staticmethod
    def show_main_information(size_floor, stage_list, stains_floor, position):
        print(f'Map size: {size_floor}')
        print(f'Floor tiles: {stage_list}')
        print(f'Dirt: {stains_floor}')
        print(f'Initial position: {position}')
        time_finish = int(input('Seconds the vacuum cleaner will run: '))
        input('Press any key to start the vacuum cleaner work...')
        print()
        return time_finish

    @staticmethod
    def check_the_floor(stains_floor, position):

        if stains_floor[position] == ' ':
            Funcion.clean_floor()

        elif stains_floor[position] == '+':
            stains_floor[position] = ' '
            Funcion.clean_up()

        elif stains_floor[position] == 'x':
            stains_floor[position] = '+'
            Funcion.clean_up()

        else:
            Funcion.floor_not_cleanable()

        return stains_floor


ambient = Floor(
    tiles,
    Funcion.stage(tiles),
    Funcion.generate_floor(tiles),
    Funcion.position_initial(Funcion.stage(tiles)),
    random_movement
)


def main():
    movement_counter = 0
    final_position = 0
    aspirated = 0

    time_finish = Funcion.show_main_information(
        ambient.get_size(),
        ambient.get_stage_list(),
        ambient.get_stains_floor(),
        ambient.get_position()
    )

    while True:

        os.system('clear')

        vacuum_cleaner_position = [' ' for _ in range(ambient.get_size())]
        vacuum_cleaner_position[ambient.get_position()] = "@"

        if ambient.get_stains_floor()[ambient.get_position()] == 'x' or '+' or '#':
            aspirated += 1

        print(f'The vacuum cleaner is on the tile: {ambient.get_position()}')
        print(f'Current state of the floor: \n{vacuum_cleaner_position}\n{ambient.get_stains_floor()}')
        ambient.set_stains_floor(Funcion.check_the_floor(ambient.get_stains_floor(), ambient.get_position()))

        if ambient.get_position() <= 0:
            ambient.set_move(2)
        elif ambient.get_position() >= ambient.get_size() - 1:
            ambient.set_move(1)

        ambient.move_left() if ambient.get_move() == 1 else ambient.move_right()

        sleep(1)
        movement_counter += 1
        time_finish -= 1

        if time_finish <= 0:
            os.system('clear')
            break

    for i in vacuum_cleaner_position:
        if i == '@':
            break
        final_position += 1

    print(f'Final position: {final_position} | I do: {movement_counter} movements.')
    print(f'Final condition of the floor: \n{vacuum_cleaner_position}\n{ambient.get_stains_floor()}')

    print(str(aspirated))


if __name__ == '__main__':
    main()

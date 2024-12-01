import random

# Размеры поля
FIELD_SIZE = 10

# Корабли и их количество
SHIPS = {
    4: 1,  # 1 корабль длиной 4 клетки
    3: 2,  # 2 корабля длиной 3 клетки
    2: 3,  # 3 корабля длиной 2 клетки
    1: 4   # 4 корабля длиной 1 клетка
}

def create_empty_field():
    return [['~' for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]

def print_field(field):
    for row in field:
        print(' '.join(row))
    print()

def place_ship(field, ship_size):
    while True:
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            x = random.randint(0, FIELD_SIZE - 1)
            y = random.randint(0, FIELD_SIZE - ship_size)
            if all(field[x][y + i] == '~' for i in range(ship_size)):
                for i in range(ship_size):
                    field[x][y + i] = 'S'
                return
        else:
            x = random.randint(0, FIELD_SIZE - ship_size)
            y = random.randint(0, FIELD_SIZE - 1)
            if all(field[x + i][y] == '~' for i in range(ship_size)):
                for i in range(ship_size):
                    field[x + i][y] = 'S'
                return

def create_field_with_ships():
    field = create_empty_field()
    for ship_size, count in SHIPS.items():
        for _ in range(count):
            place_ship(field, ship_size)
    return field

# Создаем поля для игрока и компьютера
player_field = create_field_with_ships()
computer_field = create_field_with_ships()

print("Player Field:")
print_field(player_field)

print("Computer Field:")
print_field(computer_field)

def is_hit(field, x, y):
    return field[x][y] == 'S'

def mark_hit(field, x, y):
    field[x][y] = 'X'

def mark_miss(field, x, y):
    field[x][y] = 'O'

def all_ships_sunk(field):
    return all(cell != 'S' for row in field for cell in row)

def player_turn(computer_field):
    while True:
        try:
            x = int(input("Enter row (0-9): "))
            y = int(input("Enter column (0-9): "))
            if 0 <= x < FIELD_SIZE and 0 <= y < FIELD_SIZE:
                if is_hit(computer_field, x, y):
                    print("Hit!")
                    mark_hit(computer_field, x, y)
                else:
                    print("Miss!")
                    mark_miss(computer_field, x, y)
                break
            else:
                print("Invalid coordinates. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

def computer_turn(player_field):
    while True:
        x = random.randint(0, FIELD_SIZE - 1)
        y = random.randint(0, FIELD_SIZE - 1)
        if player_field[x][y] in ['~', 'S']:
            if is_hit(player_field, x, y):
                print("Computer hit your ship!")
                mark_hit(player_field, x, y)
            else:
                print("Computer missed!")
                mark_miss(player_field, x, y)
            break

def play_game():
    while True:
        print("Your turn:")
        player_turn(computer_field)
        if all_ships_sunk(computer_field):
            print("Congratulations! You won!")
            break

        print("Computer's turn:")
        computer_turn(player_field)
        if all_ships_sunk(player_field):
            print("Computer won! Better luck next time.")
            break

        print("Player Field:")
        print_field(player_field)

        print("Computer Field:")
        print_field(computer_field)

# Запуск игры
play_game()
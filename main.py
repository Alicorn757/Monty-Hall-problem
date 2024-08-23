import random

random.seed(0)         # Устанавливаем сид
test_count = 100_000   # Количество тестов

prize = lambda: random.randint(1, 3)     # Функция для выбора номера двери с призом
choice = lambda: random.randint(1, 3)    # Функция для выбора игроком двери

def scooter(prize_door: int, choice_door: int) -> int:
    '''Функция для открытия ведущим двери с самокатом'''
    for door in range(1, 4):
        if door != prize_door and door != choice_door:
            return door


def change_door(choice_door: int, scooter_door: int) -> int:
    '''Функция для смены двери игроком'''
    for door in range(1, 4):
        if door != choice_door and door != scooter_door:
            return door

def not_change_door(choice_door: int) -> int:
    '''
       Функция, которая оставляет изначальный выбор
       Возвращает значение изначального выбора
    '''
    return choice_door

# Счётчики
cs = 0       # change_strategy
not_cs = 0   # not_change_strategy

# Перебираем ситуации
for _ in range(test_count):
    prize_door = prize()                                     # Выбираем дверь с призом
    choice_door = choice()                                   # Выбираем дверь, которую выбрал игрок
    scooter_door = scooter(prize_door, choice_door)          # Номер двери, которую открыл ведущий

    change_strategy = change_door(choice_door, scooter_door) # Поменять дверь
    not_change_strategy = not_change_door(choice_door)       # Не менять дверь (с теми же условиями - альтернативный выбор)

    # Обновляем переменные
    if change_strategy == prize_door:
        cs += 1
    elif not_change_strategy == prize_door:
        not_cs += 1
    else:
        continue

# Вывод результата, округлённого до двух знаков после запятой: вероятность нахождения приза за дверью
print(f"Не менять дверь: {round(not_cs/test_count, 2)}\nПоменять дверь: {round(cs/test_count, 2)}")

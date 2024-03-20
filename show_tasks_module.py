print(
    """
        |------------------------------------------------------------------|
        |                         Калькулятор!                             |
        |       Программа может складывать, вычитать, делить               |
        |                   И многое другое - Попробуй!                    |
        |                      Тебе понравиться!                           |
        |                Для начала выбери действия,                       |
        |                 а дальше введи числа -и наблюдай                 |
        |------------------------------------------------------------------|  
        """
)


def plus(first_number=1, second_number=1):
    print(f"{first_number} + {second_number} = {first_number + second_number}")


def minus(first_number=1, second_number=1):
    print(f"{first_number} - {second_number} = {first_number - second_number}")


def mul(first_number=1, second_number=1):
    print(f"{first_number} * {second_number} = {first_number * second_number}")


def division(first_number=1, second_number=1):
    print(f"{first_number} / {second_number} = {first_number / second_number}")


def div(first_number=1, second_number=1):
    print(f"{first_number} // {second_number} = {first_number // second_number}")


def remainder(first_number=1, second_number=1):
    print(f"{first_number} % {second_number} = {first_number % second_number}")


def div_by_degree(first_number=1, second_number=1):
    print(f"{first_number} ** {second_number} = {first_number ** second_number}")

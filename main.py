from show_tasks_module import plus, minus, mul, division, div, remainder, div_by_degree


def main():
    """
    Функция спрашивает у пользователя какое он хочет сделать действие +-*/%//**,
    псле этого пользователь вводит два числа и получает результат своего запроса
    """
    math_operation = input("+-*/%//** or exit => ")
    msg = "Put integer number: "

    while math_operation != "exit":
        first_number = int(input(msg))
        second_number = int(input(msg))

        if math_operation == "+":
            plus(first_number, second_number)

        elif math_operation == "-":
            minus(first_number, second_number)

        elif math_operation == "*":
            mul(first_number, second_number)

        elif math_operation == "/":
            division(first_number, second_number)

        elif math_operation == "//":
            div(first_number, second_number)

        elif math_operation == "%":
            remainder(first_number, second_number)

        elif math_operation == "**":
            div_by_degree(first_number, second_number)

        else:
            print(f"Не понимаю тебя!{math_operation}")

        math_operation = input("+-*/%//** or exit => ")


if __name__ == "__main__":
    print("main.py - Я работаю самостоятельно, как независимый модуль.")
    main()
else:
    print("main.py - Я запущена как импортируемый модуль.")

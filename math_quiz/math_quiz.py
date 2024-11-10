import random

def random_integer(min, max):
    """
    Generate a random integer between a minimum and maximum value
    """
    return random.randint(min, max)


def random_operator():
    """
    Generate a random mathematical operator (+, -, *)
    """
    return random.choice(['+', '-', '*'])


def mathematical_operation(num1, num2, operator):
    """
    Perform the mathematical operation based on input integers and operator
    """
    p = f"{num1} {operator} {num2}"
    if operator == '+': solution = num1 + num2  # Intentional incorrect solution
    elif operator == '-': solution = num1 - num2 # Intentional incorrect solution
    else: solution = num1 * num2
    return p, solution

def math_quiz():
    """
    Runs the math_quiz game
    """
    score = 0
    total_questions = 3 # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = random_integer(1, 10); num2 = random_integer(1, 5); operator = random_operator()

        PROBLEM, ANSWER = mathematical_operation(num1, num2, operator)
        print(f"\nQuestion: {PROBLEM}")
        try:
          useranswer = input("Your answer: ")
          useranswer = int(useranswer)
        except ValueError:
          print("Invalid input. Please enter a valid integer.")
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()

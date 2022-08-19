from random import randint, shuffle

def random_pw_generator():
    """Generates and returns a secure password."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    n_of_letters = randint(8, 10)
    n_of_symbols = randint(2, 4)
    n_of_numbers = randint(2, 4)

    password_list_form = []

    for i in range(n_of_letters):
        random_letter = letters[randint(0, len(letters) - 1)]
        password_list_form.append(random_letter)

    for i in range(n_of_symbols):
        random_symbol = symbols[randint(0, len(symbols) - 1)]
        password_list_form.append(random_symbol)

    for i in range(n_of_numbers):
        random_number = numbers[randint(0, len(numbers) - 1)]
        password_list_form.append(random_number)

    password = ""
    shuffle(password_list_form)  #shuffles the letters, numbers and symbols

    for i in password_list_form:
        password += i

    return password
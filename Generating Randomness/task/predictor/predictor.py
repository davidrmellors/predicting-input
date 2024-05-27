def find_triads(characters):
    """
    This function takes a string of characters and finds all the triads (three consecutive characters).
    It returns a dictionary where the keys are the triads and the values are lists of two elements:
    the first element is the count of '0' following the triad and the second is the count of '1'.

    :param characters: A string of characters
    :return: A dictionary of triads and their counts
    """
    triads = dict()
    left = 0
    for right in range(3, len(characters)):
        triad = characters[left:right]

        if triad not in triads.keys():
            triads[triad] = [0, 0]

        if characters[right] == '0':
            triads[triad][0] += 1
        else:
            triads[triad][1] += 1
        left += 1

    return dict(sorted(triads.items()))


def predict_input(test_characters, triads):
    """
    This function takes a string of test characters and a dictionary of triads.
    It predicts the next character for each triad in the test characters based on the counts in the triads dictionary.
    It returns a string of predicted characters.

    :param test_characters: A string of test characters
    :param triads: A dictionary of triads and their counts
    :return: A string of predicted characters
    """
    left = 0
    computer_prediction = ""
    for right in range(3, len(test_characters)):
        triad = test_characters[left:right]
        if int(triads[triad][0]) > int(triads[triad][1]):
            computer_prediction += "0"
        else:
            computer_prediction += "1"
        left += 1

    return computer_prediction


def accuracy(predicted_input, test_characters):
    """
    This function takes a string of predicted characters and a string of test characters.
    It calculates the accuracy of the prediction and prints it.
    It also calculates the balance update based on the prediction accuracy and returns it.

    :param predicted_input: A string of predicted characters
    :param test_characters: A string of test characters
    :return: The balance update based on the prediction accuracy
    """
    correct = 0
    test_characters = test_characters[3:]
    total = len(test_characters)

    for i in range(len(predicted_input)):
        if predicted_input[i] == test_characters[i]:
            correct += 1
    incorrect = total - correct
    percentage_correct = round(float(correct / total) * 100, 2)

    print(f'\nComputer guessed {correct} out of {total} symbols right ({percentage_correct} %)')

    update_balance = incorrect - correct

    return update_balance


def get_random_string():
    """
    This function prompts the user to input a random string of characters.
    It returns the string if it contains at least 4 characters, otherwise it keeps prompting the user.

    :return: A string of characters
    """
    len_sequence = 0
    characters_to_predict = ""

    while len_sequence < 4:
        test_string = str(input("\nPrint a random string containing 0 or 1: "))
        if test_string.strip().lower() == "enough":
            return "enough"

        for char in test_string:
            if char == '1' or char == '0':
                characters_to_predict += char
            len_sequence = len(characters_to_predict)

        if len_sequence < 4:
            print(f'Current data length is {len_sequence}, please enter a new string with a min length of 4')
            characters_to_predict = ""
            len_sequence = 0

    return characters_to_predict


def init_game():
    """
    This function initializes the game.
    It prompts the user to input a string of characters until it contains at least 100 characters.
    It returns the final string of characters.

    :return: A string of characters
    """
    len_sequence = 0
    list_of_characters = ""
    min_input = 100

    print("Please provide AI some data to learn...")
    print("The current data length is 0, 100 symbols left")

    while len_sequence < min_input:
        sequence = str(input("Print a random string containing 0 or 1: "))
        for character in sequence:
            if character == '1' or character == '0':
                list_of_characters += character
        len_sequence = len(list_of_characters)
        if len_sequence < min_input:
            print(f'Current data length is {len_sequence}, {min_input - len_sequence} symbols left')

    print(f'\nFinal data string:\n{list_of_characters}')

    return list_of_characters


def start_game():
    """
    This function starts the game.
    It initializes the game, finds the triads in the initial string of characters, and starts the prediction loop.
    The loop continues until the user decides to stop or the balance reaches 0.
    """
    balance = 1000
    final_string = init_game()
    triad_stats = find_triads(final_string)

    print(f'''\nYou have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!''')

    while balance > 0:

        random_string = get_random_string()

        if random_string == "enough":
            break
        prediction = predict_input(random_string, triad_stats)
        print(f'predictions:\n{prediction}')

        new_balance = accuracy(prediction, random_string)

        balance = balance + new_balance
        if balance < 0:
            balance = 0

        print(f'Your balance is now ${balance}')

    print('Game over!')


start_game()

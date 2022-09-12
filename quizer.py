from termcolor import colored


def print_welcome():
    print('Welcome to the Quizapp')
    print('----------------------')


def print_goodbye():
    print('----------------------')
    print('Have a nice day!')


def print_menu():
    print(colored('S', 'green', attrs=['underline']) + 'equential')
    print(colored('R', 'green', attrs=['underline']) + 'andom')
    print(colored('Q', 'green', attrs=['underline']) + 'uit')


def read_user_option(valid_options):
    valid_options_str = '/'.join(valid_options)
    # Loops until the user input a valid option
    while True:
        # Reads user input
        option = input(colored(f'Please select one choice ({valid_options_str})', 'yellow') + ': ')
        # Obtains the first character (if any) of user input
        option = option[0:1].upper()
        # Check if user input is a valid option
        if option in valid_options:
            break
    # Successfully reads a valid option
    return option


def print_question(question):
    print(colored(question['source'], 'green', attrs=['bold']))
    print(question['description'])
    options = question['options']
    for index in range(len(options)):
        letter = chr(index + ord('A'))
        letter = colored(f'({letter})', 'green', attrs=['bold'])
        option = options[index]
        print(f'{letter} {option}')

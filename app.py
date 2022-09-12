import random

from termcolor import colored

import questions
import quizer

if __name__ == '__main__':
    # Prints menu and asks for a user choice
    quizer.print_welcome()
    quizer.print_menu()
    option = quizer.read_user_option(['S', 'R', 'Q'])

    # If the user would like to quit
    if option == 'Q':
        quizer.print_goodbye()
        exit()

    # Shuffles the problems if needed
    question_list = questions.question_list
    if option == 'R':
        random.shuffle(question_list)

    # Loops through all questions and record user answers
    num_correct = 0
    for question in question_list:
        print()
        quizer.print_question(question)
        choice = quizer.read_user_option(['A', 'B', 'C', 'D', 'E'])
        if choice == question['answer']:
            num_correct += 1
            print(colored('Cong, you are correct', 'blue'))
        else:
            print(colored('Sorry, you are wrong', 'red'))

    # Print report
    print()
    score = int(num_correct / len(question_list) * 100)
    print(f'Score: {score} [{num_correct} correct answer(s) out of {len(question_list)} total questions]')

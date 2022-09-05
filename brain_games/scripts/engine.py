import prompt


def play_engine(game, task_text):
    username = prompt.string('Welcome to the Brain Games!\n'
                             'May I have your name? ')
    print(f"Hello, {username}!")
    print(task_text)
    for i in range(3):
        question, result = game()
        print(question)
        user_answer = input('Your answer: ')
        if user_answer == result:
            print('Correct!')
        else:
            print(f'{question}\nYour answer: {user_answer}\n'
                  f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{result}'.\nLet's try again, {username}!")
            return
    print(f"Congratulations, {username}!")


if __name__ == "__main__":
    play_engine()

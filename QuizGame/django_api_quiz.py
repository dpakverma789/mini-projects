try:
    import random
    import requests
    import os
except ModuleNotFoundError:
    import os
    os.system('pip install requests')
    import requests

point = 0
incorrect_list = []
try:
    question = requests.get('http://127.0.0.1:7078/quiz/').json()
    ids = [i for i in range(question.__len__())]
    name = input('\nEnter your Name: ')
    if question:
        while ids:
            i = random.choice(ids)
            if question:
                print('\n\n', question[i]['question'], '\n',
                      'A: ', question[i]['option_1'], '\t', 'B: ', question[i]['option_2'], '\n',
                      'C: ', question[i]['option_3'], '\t', 'D: ', question[i]['option_4'], '\n')
                user_answer = input('Enter your answer: ').strip()
                if user_answer == question[i]['answer']:
                    point += 10
                else:
                    if user_answer not in ('exit', 'quit'):
                        incorrect_list.append(user_answer)
                if user_answer in ('exit', 'quit'):
                    break
            ids.remove(i)
            print("===" * 20)
        print(f'\n\n\tWell Played "{name.upper()}" Your Score is "{point}" out of "{question.__len__() * 10}"')
        print(f'\n\tYour incorrect answers are {incorrect_list}')
except Exception as error:
    print('Could not connect with the API! \n %s' %error)

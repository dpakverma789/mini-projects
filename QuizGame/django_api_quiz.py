import random
import os
import logging
PROJECT_DIRECTORY = os.path.join(os.getcwd(),'QuizGame')
os.chdir(PROJECT_DIRECTORY)
REQUIREMENTS_FILE = os.path.join(os.getcwd(), 'requirements.txt')
logging.basicConfig(
    level=logging.INFO,
    filename= os.path.join(PROJECT_DIRECTORY, "app.log"),
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def install_requirements(file=None):
    return os.system(f'pip install -r {file}')

def remove_requirements(file=None):
    if os.path.isfile(file):
        return os.system(f'pip uninstall -y -r {file}')
    return False

try:
    import requests
except ModuleNotFoundError:
    try:
        if not os.path.isfile(REQUIREMENTS_FILE):
            raise FileNotFoundError
        install_requirements(REQUIREMENTS_FILE)
    except FileNotFoundError:
        os.system('python -m pip install --upgrade pip')
        for pack in ('requests',):
            os.system(f'pip install {pack}')
        import requests
    finally:
        os.system('pip freeze > requirements.txt')


def quiz_game():
    logging.info('function called...OK')
    point = 0
    incorrect_list = []
    try:
        question_list = requests.get('https://django-project-apis.vercel.app/quiz/').json()
    except ConnectionError:
        print('\n *** Could not connect with the API! ***')
    except Exception as error:
        print(error)
        logging.error(f'{error}...Failed')
    else:
        logging.info('question fetched...OK')
        print("\t\t\tTo quit type q or x ")
        name = input('\nEnter Player Name Please: ')
        total_question = question_list.__len__()
        ids = list(map(lambda x: x['id'], question_list))
        question_asked_counter = question_counter = 5
        while question_asked_counter:
            question_id = random.choice(ids)
            question = list(filter(lambda x: x['id'] == question_id, question_list))
            if question:
                QUESNO = (total_question + 1) - len(ids)
                question_data = {
                    QUESNO: f"{question[0]['question']}?",
                    'A': question[0]['option_1'],
                    'B': question[0]['option_2'],
                    'C': question[0]['option_3'],
                    'D': question[0]['option_4'],
                }
                ans_key = [key for key, val in question_data.items() if val == question[0]['answer']][0]
                question_data.update({'ANS': ans_key})
                for key, val in question_data.items():
                    if key != 'ANS':
                        print(f'{key}: {val}')
                user_answer = input('\nEnter your answer: ').strip().upper()
                ans_key = question_data.get('ANS')
                if user_answer in (ans_key, question_data.get(ans_key)):
                    point += 10
                else:
                    if user_answer not in ('Q', 'X'):
                        incorrect_list.append(f'Q{QUESNO}:{user_answer}')
                if user_answer in ('Q', 'X'):
                    break
            ids.remove(question_id)
            question_asked_counter -= 1
            print("===" * 20)
        print(f'\n\n\tWell Played "{name.upper()}" Your Score is "{point}" out of "{question_counter * 10}"')
        print(f'\n\tYour incorrect answers are {incorrect_list}')
    finally:
        print('\n\tBye-Bye')
        logging.info('executed successfully...OK')
        return


if __name__ == '__main__':
    quiz_game()

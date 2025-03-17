import random
import os
import sys
PROJECT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
REQUIREMENTS_FILE = os.path.join(PROJECT_DIRECTORY,'requirements.txt')
root_dir = os.path.dirname(PROJECT_DIRECTORY)
sys.path.insert(0, root_dir)

def install_requirements(file=None):
    return os.system(f'pip install -r {file}')

def remove_requirements(file=None):
    if os.path.isfile(file):
        return os.system(f'pip uninstall -y -r {file}')
    return False

try:
    from Mini_Projects.Python_DB_ORM.orm2 import *
except ModuleNotFoundError:
    try:
        if not os.path.isfile(REQUIREMENTS_FILE):
            raise FileNotFoundError
        install_requirements(REQUIREMENTS_FILE)
    except FileNotFoundError:
        os.system('python -m pip install --upgrade pip')
        for pack in ('requests',):
            os.system(f'pip install {pack}')
        from Mini_Projects.Python_DB_ORM.orm2 import *
    finally:
        os.system('pip freeze > requirements.txt')


def get_question():
    point = 0
    incorrect_list = []
    try:
        question_ids = fetch_record(db_name="django-project-apis",table_name='questionbank_questionbank')
        ids = list(map(lambda x: x['id'], question_ids))
        total_question = len(ids)
        question_asked_counter = question_counter = 5
        while question_asked_counter:
            question_id = random.choice(ids)
            question = list(filter(lambda x: x['id'] == question_id, question_ids))
            if question:
                ques_no = (total_question+1) - len(ids)
                question_data = {
                    ques_no: question[0]['question'],
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
                        incorrect_list.append(f'Q{ques_no}:{user_answer}')
                if user_answer in ('Q', 'X'):
                    break
            ids.remove(question_id)
            question_asked_counter -= 1
            print("==="*20)
        return point, question_counter, incorrect_list
    except Exception as e:
        print(e)


# collecting question and its details
def question_collection():
    question_data = {
        'question': None,
        'option_1': None,
        'option_2': None,
        'option_3': None,
        'option_4': None,
        'answer': None,
    }
    for user_input in question_data:
        question_data[user_input] = input(f'Enter your {user_input}? :')
    try:
        print("\n\t\tPlease wait while we are updating question...")
        rowcount = create_record(db_name='django-project-apis', table_name='questionbank_questionbank', values=question_data)
        if rowcount:
            print("\n\t\t\tUpdated Question in QuestionBank!!\n")
            return True
        print("\n\t\t\tUpdated Question Failed!!\n")
        return False
    except Exception as error:
        print(error)
        return False


# main thread
if __name__ == '__main__':
    try:
        choice = int(input("\nPRESS 1 FOR PLay Quiz  \t\t PRESS 2 FOR Update Question Bank: "))
        if choice == 1:
            name = input("\nEnter your name: ")
            print("\n\t\t\t===== WELCOME TO QUIZ GAME %s =====" % name.upper())
            print("\t\t\tTo quit type q or x ")
            print("\t\t\tPlease wait loading the questions... \n")
            point, total, incorrect = get_question()
            print(f'\n\n\tWell Played "{name.upper()}" Your Score is "{point}" out of "{total*10}"')
            print(f'\n\tYour incorrect answers are {incorrect}')
            del point, total, incorrect
        elif choice == 2:
            number_of_question = int(input("Enter Number of Question to be Updated? :"))
            try:
                for _ in range(1, number_of_question+1):
                    question_collection()
            except Exception as error:
                print('\n\t\t\t\t QuestionBank Update Failed!!\n', error)
        else:
            print('\n\t\t\t\tOpps Invalid Selection !!\n')
    except:
        print('\n\t\t\t\tDatabase Connection Failed!!\n')

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
    question = requests.get('https://django-project-apis.vercel.app/quiz/').json()
except Exception as error:
    print('\n *** Could not connect with the API! ***')
    # print(error)
else:
    name = input('\nEnter your Name: ')
    total_question = question.__len__()
    ids = list(map(lambda x: x['id'], question))
    while ids:
        question_id = random.choice(ids)
        list(filter(lambda x: x['id'] == question_id, question))
        database.execute(f"select * {from_table} where id = {question_id}")
        question = database.fetchall()
        if question:
            QUESNO = (11 - len(ids))
            question_data = {
                QUESNO: question[0][1],
                'A': question[0][2],
                'B': question[0][3],
                'C': question[0][4],
                'D': question[0][5],
            }
            ANSKEY = [key for key, val in question_data.items() if val == question[0][6]][0]
            question_data.update({'ANS': ANSKEY})
            for key, val in question_data.items():
                if key != 'ANS':
                    print(f'{key}: {val}')
            user_answer = input('\nEnter your answer: ').strip()
            ans_key = question_data.get('ANS')
            if user_answer in (ans_key, question_data.get(ans_key)):
                point += 10
            else:
                if user_answer not in ('exit', 'quit'):
                    incorrect_list.append(f'Q{QUESNO}:{user_answer}')
            if user_answer in ('exit', 'quit'):
                break
        ids.remove(question_id)
        print("===" * 20)
finally:
    print('\n\tBye-Bye')

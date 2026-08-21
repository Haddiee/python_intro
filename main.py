from quiz_data import get_questions
import random, datetime

question_bank = get_questions()

print(question_bank)

random.shuffle(question_bank)
print("=" * 50)
print(" ")
print(question_bank)

questions_only = []
answers_only = []
user_response = []

for question in question_bank:
    #print(question[0])
    questions_only.append(question[0])
    answers_only.append(question[1])

print(questions_only)
print(answers_only)

def ask(question):
    response = input(f"{question} :")
    return response

#

while True:
        for que in questions_only:
            ans = ask(que)
            user_response.append(ans)

        break

# for correct_answers in answers_only:
#      for responses in user_response:
#           if responses == correct_answers:
#               print("Correct")
#         else: 
#           print("Incorrect")

record = []

def get_record(question, mark):
     for ans in answers_only:
          record.append(f{"quest"}, f"ans")
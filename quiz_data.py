question_bank = [
    ("What is html?", "Hypertext Markup Language"),
    ("What is CSS?", "Cascading Style Sheets"),
    ("What is http?", "Hypertext Transfer Protocol"),
    ("What is API?", "Application Programming Interface"),
    ("What is RAG?", "Retrieval Augmented Generation"),
]

def get_questions():
    return question_bank

questions = get_questions()

print(questions)
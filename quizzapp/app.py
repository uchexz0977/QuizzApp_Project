from flask import Flask, render_template, request

app = Flask(__name__)

# Sample quiz data
quiz_data = {
    'title': 'Python Programming Quiz',
    'questions': [
        {
            'id': 1,
            'question_text': 'What is the capital of France?',
            'options': ['Paris', 'Berlin', 'London', 'Madrid'],
            'correct_answer': 'Paris'
        },
        {
            'id': 2,
            'question_text': 'Which programming language is this quiz about?',
            'options': ['Java', 'Python', 'C++', 'JavaScript'],
            'correct_answer': 'Python'
        },
        {
            'id': 3,
            'question_text': 'Which of the following is used in pencils?',
            'options': ['Graphite', 'Iron', 'Carbon', 'Silicon'],
            'correct_answer': 'Graphite'
        },
        # Add more questions as needed
    ]
}

@app.route('/')
def home():
    return render_template('quiz.html', title=quiz_data['title'], quiz_title=quiz_data['title'], questions=quiz_data['questions'])

@app.route('/quiz', methods=['POST'])
def quiz():
    user_answers = {key: value for key, value in request.form.items()}
    score, total_questions = calculate_score(user_answers)
    return render_template('result.html', title='Quiz Result', score=score, total_questions=total_questions)


def calculate_score(user_answers):
    score = 0
    total_questions = len(quiz_data['questions'])

    for question in quiz_data['questions']:
        question_id = question['id']
        user_answer = user_answers.get(str(question_id))  # Convert question_id to string
        if user_answer and user_answer == question['correct_answer']:
            score += 1

    return score, total_questions

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0", port = 3000)

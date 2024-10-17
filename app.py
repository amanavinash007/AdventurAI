from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_wtf.csrf import CSRFProtect
import form_handler
import json
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('anything_in_the_world')  # Use environment variable
csrf = CSRFProtect(app)

@app.route('/')
def index():
    session.clear()  # Clear any existing session data
    return render_template('index.html')

@app.route('/question/<int:question_number>', methods=['GET', 'POST'])
def question(question_number):
    if question_number < 1 or question_number > 8:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        session[f'q{question_number}'] = request.form[f'question{question_number}']
        next_question = question_number + 1
        if next_question <= 8:
            return redirect(url_for('question', question_number=next_question))
        else:
            return redirect(url_for('process'))
    
    # Ensure user can't skip questions
    if question_number > 1 and f'q{question_number-1}' not in session:
        return redirect(url_for('question', question_number=question_number-1))
    
    return render_template(f'question{question_number}.html')

@app.route('/process')
def process():
    # Ensure all questions have been answered
    if not all(f'q{i}' in session for i in range(1, 9)):
        return redirect(url_for('index'))
    
    answers = [session.get(f'q{i}', '') for i in range(1, 9)]
    try:
        result = form_handler.handle_form(answers)
        return jsonify(result)
    except Exception as e:
        app.logger.error(f"Error processing form: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')
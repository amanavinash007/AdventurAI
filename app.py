from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import form_handler
import json
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.secret_key = 'anything_in_the_world'  # Replace with a real secret key

@app.route('/')
def index():
    session.clear()  # Clear any existing session data
    return render_template('index.html')

@app.route('/question1', methods=['GET', 'POST'])
def question1():
    if request.method == 'POST':
        session['q1'] = request.form['question1']
        return redirect(url_for('question2'))
    return render_template('question1.html')

@app.route('/question2', methods=['GET', 'POST'])
def question2():
    if request.method == 'POST':
        session['q2'] = request.form['question2']
        return redirect(url_for('question3'))
    return render_template('question2.html')

@app.route('/question3', methods=['GET', 'POST'])
def question3():
    if request.method == 'POST':
        session['q3'] = request.form['question3']
        return redirect(url_for('question4'))
    return render_template('question3.html')

@app.route('/question4', methods=['GET', 'POST'])
def question4():
    if request.method == 'POST':
        session['q4'] = request.form['question4']
        return redirect(url_for('question5'))
    return render_template('question4.html')

@app.route('/question5', methods=['GET', 'POST'])
def question5():
    if request.method == 'POST':
        session['q5'] = request.form['question5']
        return redirect(url_for('question6'))
    return render_template('question5.html')

@app.route('/question6', methods=['GET', 'POST'])
def question6():
    if request.method == 'POST':
        session['q6'] = request.form['question6']
        return redirect(url_for('question7'))
    return render_template('question6.html')

@app.route('/question7', methods=['GET', 'POST'])
def question7():
    if request.method == 'POST':
        session['q7'] = request.form['question7']
        return redirect(url_for('question8'))
    return render_template('question7.html')

@app.route('/question8', methods=['GET', 'POST'])
def question8():
    if request.method == 'POST':
        session['q8'] = request.form['question8']
        return redirect(url_for('process'))
    return render_template('question8.html')

@app.route('/process')
def process():
    answers = [session.get(f'q{i}', '') for i in range(1, 9)]
    result = form_handler.handle_form(answers)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
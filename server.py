from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "This is the mega crazy securedddddddd key"

@app.route('/')
def index(): 
    
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def reset():
    session.clear()
    session['visits'] = 0
    return redirect('/')

@app.route('/add_2')
def add_2():
    session['visits'] += 1
    return redirect('/')

@app.route('/custom', methods=['POST'])
def custom():
    session['add_custom'] = int(request.form['add_custom'])
    session['visits'] += session['add_custom']-1
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
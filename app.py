from flask import Flask, render_template, request

app = Flask(__name__)
balance = 100
transactions = []

@app.route('/')
def home():
    return render_template('index.html', balance=balance)

@app.route('/deposit', methods=['POST'])
def deposit():
    global balance
    amount = int(request.form['amount'])
    balance += amount
    transactions.append(f"Deposited: {amount}")
    return render_template('index.html', balance=balance, msg="Deposit Successful")

@app.route('/withdraw', methods=['POST'])
def withdraw():
    global balance
    amount = int(request.form['amount'])
    
    if amount > balance:
        return render_template('index.html', balance=balance, msg="Insufficient Balance")
    
    balance -= amount
    transactions.append(f"Withdrawn: {amount}")
    return render_template('index.html', balance=balance, msg="Withdrawal Successful")

@app.route('/transactions')
def show_transactions():
    return render_template('transactions.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)

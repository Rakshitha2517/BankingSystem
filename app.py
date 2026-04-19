from flask import Flask, render_template, request

app = Flask(__name__)


balance = 0
transactions = []

@app.route('/')
def home():
    return render_template('index.html', balance=balance, msg="")
@app.route('/deposit', methods=['POST'])
def deposit():
    global balance
    amount = request.form.get('amount')

    if not amount:
        return render_template('index.html', balance=balance, msg="Enter amount")

    try:
        amount = int(amount)
    except:
        return render_template('index.html', balance=balance, msg="Invalid input")

    if amount <= 0:
        return render_template('index.html', balance=balance, msg="Amount must be > 0")

    balance += amount
    transactions.append(f"Deposited: {amount}")

    return render_template('index.html', balance=balance, msg="Deposit Successful")
@app.route('/withdraw', methods=['POST'])
def withdraw():
    global balance
    amount = request.form.get('amount')

    if not amount:
        return render_template('index.html', balance=balance, msg="Enter amount")

    try:
        amount = int(amount)
    except:
        return render_template('index.html', balance=balance, msg="Invalid input")

    if amount > balance:
        return render_template('index.html', balance=balance, msg="Insufficient Balance")

    balance -= amount
    transactions.append(f"Withdrawn: {amount}")

    return render_template('index.html', balance=balance, msg="Withdrawal Successful")
@app.route('/transactions')
def show_transactions():
    return render_template('transactions.html', transactions=transactions)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)from flask import Flask, render_template, request

app = Flask(__name__)

balance = 100
transactions = []

@app.route('/')
def home():
    return render_template('index.html', balance=balance, transactions=transactions, msg="")

@app.route('/deposit', methods=['POST'])
def deposit():
    global balance
    amount = request.form.get('amount')

    if not amount:
        return render_template('index.html', balance=balance, transactions=transactions, msg="Enter amount")

    try:
        amount = int(amount)
    except:
        return render_template('index.html', balance=balance, transactions=transactions, msg="Invalid input")

    if amount <= 0:
        return render_template('index.html', balance=balance, transactions=transactions, msg="Amount must be > 0")

    balance += amount
    transactions.append(f"Deposited: {amount}")

    return render_template('index.html', balance=balance, transactions=transactions, msg="Deposit Successful")

@app.route('/withdraw', methods=['POST'])
def withdraw():
    global balance
    amount = request.form.get('amount')

    if not amount:
        return render_template('index.html', balance=balance, transactions=transactions, msg="Enter amount")

    try:
        amount = int(amount)
    except:
        return render_template('index.html', balance=balance, transactions=transactions, msg="Invalid input")

    if amount > balance:
        return render_template('index.html', balance=balance, transactions=transactions, msg="Insufficient Balance")

    balance -= amount
    transactions.append(f"Withdrawn: {amount}")

    return render_template('index.html', balance=balance, transactions=transactions, msg="Withdrawal Successful")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

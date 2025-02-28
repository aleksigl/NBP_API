import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/currency_calculator', methods=['GET', 'POST'])
def index():
    response = requests.get("https://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()

    rates = data[0]['rates']
    currencies = [{
        'currency': currency['currency'], 
        'code': currency['code'], 
        'bid': currency['bid']
        } 
        for currency in rates]

    if request.method == 'POST':
        selected_currency_code = request.form['currency']
        amount = float(request.form['amount'])

        selected_currency = next((currency for currency in currencies if currency['code'] == selected_currency_code), None)

        if selected_currency:
            cost_in_pln = '{:.2f}'.format(amount * selected_currency['bid'])
            return render_template('currency_calc.html', currencies=currencies, result=cost_in_pln, amount=amount, currency_code=selected_currency_code)

    return render_template('currency_calc.html', currencies=currencies)

if __name__ == '__main__':
    app.run(debug=True)
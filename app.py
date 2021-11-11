
from flask import Flask, render_template, request
import requests, json
import config
app=Flask(__name__, template_folder='template')

@app.route('/',methods =["POST", "GET"])
def get_company():

    company = request.form.get("company")

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"

    querystring = {"symbol": company,"region":"US"}

    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': config.api_key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    obj = response.json()
    stock_price = obj["price"]['currencySymbol'] + obj["price"]["regularMarketOpen"]["fmt"]
    
    return render_template("index.html", company_name=company, price=stock_price)

if __name__ == '__main__':
    app.run(debug=True)

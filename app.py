from flask import Flask, render_template, request, redirect, url_for, session
import requests
from bs4 import BeautifulSoup
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret'

# Ye apna database hai 
def initialize_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

initialize_db()

# User logged in hai ya nahi check krega ye 
def logged_in():
    return 'username' in session

#Ye function data fetch krega
def get_prices(product):
    amazon_url = f"https://www.amazon.in/s?k={product}"
    flipkart_url = f"https://www.flipkart.com/search?q={product}"

    amazon_page = requests.get(amazon_url)
    flipkart_page = requests.get(flipkart_url)

    amazon_soup = BeautifulSoup(amazon_page.content, 'html.parser')
    flipkart_soup = BeautifulSoup(flipkart_page.content, 'html.parser')

    amazon_price = amazon_soup.find('span', {'class': 'a-price-whole'})
    flipkart_price = flipkart_soup.find('div', {'class': '_30jeq3'})  

    # Check krega data fetch hua ya nahi 
    if amazon_price:
        amazon_price = amazon_price.text.strip()
    else:
        amazon_price = "N/A"

    if flipkart_price:
        flipkart_price = flipkart_price.text.strip()
    else:
        flipkart_price = "N/A"

    return amazon_price, flipkart_price



# Home page
@app.route('/')
def home():
    if logged_in():
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

# Login ka page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', message='Invalid username or password')
    else:
        return render_template('login.html')

# Signup ka page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    else:
        return render_template('signup.html')

# Logout ka page
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

# Price comparison wala pagge
@app.route('/compare', methods=['GET', 'POST'])
def compare():
    if logged_in():
        if request.method == 'POST':
            return compare_prices()
        else:
            return render_template('compare.html')
    else:
        return redirect(url_for('login'))


#Price Compare karne wala function / ye function data display krega
def compare_prices():
    product = request.form['product']
    amazon_price, flipkart_price = get_prices(product)
    return render_template('compare.html', amazon_price=amazon_price, flipkart_price=flipkart_price, product=product)




if __name__ == '__main__':
    app.run(debug=True)

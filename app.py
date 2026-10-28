from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from datetime import datetime
import json, os

app = Flask(__name__)
app.secret_key = 'restaurant-secret-key-2024'

# In-memory storage (replace with a DB in production)
reservations = []
messages = []

MENU = {
    "Starters": [
        {"name": "Bruschetta al Pomodoro", "desc": "Toasted sourdough, heirloom tomatoes, fresh basil, aged balsamic", "price": 12},
        {"name": "Burrata & Prosciutto", "desc": "Creamy burrata, San Daniele prosciutto, truffle honey, rocket", "price": 18},
        {"name": "Zuppa del Giorno", "desc": "Chef's daily soup, artisan bread, herb oil", "price": 10},
        {"name": "Calamari Fritti", "desc": "Crispy squid rings, lemon aioli, chilli flakes, fresh parsley", "price": 15},
    ],
    "Mains": [
        {"name": "Tagliatelle al Tartufo", "desc": "Handmade pasta, black truffle, parmesan cream, toasted walnuts", "price": 28},
        {"name": "Branzino al Forno", "desc": "Whole sea bass, lemon butter, capers, braised fennel", "price": 34},
        {"name": "Costata di Manzo", "desc": "28-day dry-aged ribeye 300g, roasted garlic butter, bone marrow jus", "price": 52},
        {"name": "Risotto ai Funghi", "desc": "Wild mushroom risotto, aged pecorino, fresh thyme, truffle oil", "price": 24},
        {"name": "Pollo alla Parmigiana", "desc": "Free-range chicken breast, San Marzano tomato, mozzarella, basil", "price": 26},
    ],
    "Desserts": [
        {"name": "Tiramisu della Casa", "desc": "House tiramisu, espresso-soaked ladyfingers, mascarpone, cocoa", "price": 12},
        {"name": "Panna Cotta", "desc": "Vanilla panna cotta, seasonal berry compote, mint", "price": 10},
        {"name": "Tartufo al Cioccolato", "desc": "Dark chocolate truffle, pistachio, vanilla gelato", "price": 14},
    ],
    "Drinks": [
        {"name": "Aperol Spritz", "desc": "Aperol, Prosecco, soda, orange slice", "price": 12},
        {"name": "Negroni Sbagliato", "desc": "Campari, sweet vermouth, Prosecco", "price": 14},
        {"name": "House Wine (glass)", "desc": "Curated Italian selection — red, white or rosé", "price": 9},
        {"name": "San Pellegrino", "desc": "Sparkling mineral water 750ml", "price": 5},
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', menu=MENU)

@app.route('/reservations', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        data = {
            'id': len(reservations) + 1,
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'date': request.form.get('date'),
            'time': request.form.get('time'),
            'guests': request.form.get('guests'),
            'notes': request.form.get('notes', ''),
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        reservations.append(data)
        flash('success')
        return redirect(url_for('reserve'))
    return render_template('reservations.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        msg = {
            'id': len(messages) + 1,
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'subject': request.form.get('subject'),
            'message': request.form.get('message'),
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        messages.append(msg)
        flash('success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

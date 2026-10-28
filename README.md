# Osteria Lumina — Restaurant Web App

A full-featured restaurant website built with Python Flask.

## Features
- **Home** — Hero section, about, menu preview, reservation call-to-action
- **Menu** — Tabbed menu (Starters, Mains, Desserts, Drinks) with prices
- **Reservations** — Booking form with date/time/guest selection + sidebar info
- **Contact** — Contact form + address, hours, phone, email

## Project Structure
```
restaurant/
├── app.py               # Flask routes & data
├── requirements.txt
└── templates/
    ├── base.html        # Shared nav, footer, styles
    ├── index.html       # Homepage
    ├── menu.html        # Menu page
    ├── reservations.html
    └── contact.html
```

## Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
python app.py

# 3. Open in browser
# http://localhost:5000
```

## Customisation Tips
- **Menu items**: Edit the `MENU` dict in `app.py`
- **Restaurant name/address**: Update `base.html` footer and `contact.html`
- **Production**: Replace in-memory `reservations` / `messages` lists with a database (SQLite, PostgreSQL, etc.)
- **Email notifications**: Integrate Flask-Mail to send confirmation emails on booking

## Production Deployment
For production, use Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 app:app
```

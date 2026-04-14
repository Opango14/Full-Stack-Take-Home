# Full-Stack-Take-Home
# Eng-Swahili Translator - Full Stack Take Home

A simple and clean full-stack web application that translates text between **English** and **Swahili** using a predefined dictionary.

Built with **Django** as requested, following best practices for structure and clarity.

---

## Features

- Clean and responsive user interface
- Translate from English → Swahili and Swahili → English
- RESTful API endpoint: `POST /api/v1/translate-text`
- In-memory translation using a JSON dictionary (easy to extend)
- No external APIs or database required
- Supports Enter key to translate
- Proper error handling and loading states
- Fully functional offline

---

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **API**: JSON-based REST endpoint
- **Translation**: Custom bidirectional dictionary (JSON)

---

### 1. Clone the Repository

```bash
git clone https://github.com/Opango14/Full-Stack-Take-Home.git
cd Full-Stack-Take-Home
```
### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install django
```
### 4. Run Migrations
```bash
python manage.py migrate
```
### 5. Start the Development Server
```bash
python manage.py runserver
```
Open your browser and go to:
http://127.0.0.1:8000

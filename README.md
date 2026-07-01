# 📝 Quick Note App

A secure web-based **Quick Note Application** built using **Python Flask**, **SQLite**, and **Bootstrap**. The application allows users to register, log in securely, and manage personal notes through Create, Read, Update, and Delete (CRUD) operations.

---

## 📌 Features

### User Authentication
- User Registration
- User Login
- User Logout
- Password Hashing using Werkzeug
- Email Validation
- Account Lock after 3 Failed Login Attempts
- Automatic Unlock after 5 Minutes

### Notes Management
- Create Notes
- View Personal Notes
- Edit Notes
- Delete Notes
- Each user can only access their own notes

### Security Features
- Password Hashing
- CSRF Protection using Flask-WTF
- Session Timeout (2 Minutes)
- XSS Protection (Escapes HTML/JavaScript)
- Login Required for Protected Pages

---

## 🛠 Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

---

## 📂 Project Structure

```
QuickNoteApp/
│
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   └── home.html
│
├── static/
│   └── style.css
│
├── instance/
│   └── database.db
│
├── run.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shariya97/QuickNoteApp.git
```

### 2. Navigate to the Project

```bash
cd QuickNoteApp
```

### 3. Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Activate the virtual environment

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python run.py
```

---

## 🌐 Access the Application

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📖 How to Use

1. Register a new account.
2. Log in using your credentials.
3. Add new notes.
4. Edit existing notes.
5. Delete unwanted notes.
6. Log out securely.

---

## 🔒 Security Implemented

- Passwords are securely hashed before storage.
- CSRF protection is enabled for all forms.
- Sessions automatically expire after 2 minutes of inactivity.
- Accounts are locked for 5 minutes after 3 consecutive failed login attempts.
- User input is escaped to prevent Cross-Site Scripting (XSS).

---

## 🗄 Database

The application uses SQLite with two tables:

### Users

| Field | Description |
|--------|-------------|
| id | User ID |
| username | Username |
| email | Email Address |
| password_hash | Encrypted Password |
| failed_attempts | Failed Login Count |
| lock_until | Account Lock Timestamp |

### Notes

| Field | Description |
|--------|-------------|
| id | Note ID |
| text | Note Content |
| date_created | Creation Date |
| user_id | Owner of the Note |

---

## 📸 Application Features

- User Registration
- User Login
- Personal Dashboard
- Add Notes
- Edit Notes
- Delete Notes
- Session Timeout
- Account Lockout
- Secure Authentication

---

## 👨‍💻 Author

**Shariya**

GitHub: https://github.com/shariya97

---

## 📄 License

This project was developed for educational purposes.

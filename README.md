"# fitness_tracker" 
# 🏋️ Fitness Tracker Web App

A simple and powerful **Django-based web application** to track daily fitness activities like exercise, duration, calories burned, and date.

---

## 🚀 Features

- 🔐 User Authentication (Login / Register)
- ➕ Add Fitness Data
- 📊 View Fitness Records
- 👤 User-specific data tracking
- 🛠️ Admin Panel (Django Admin)
- 💾 SQLite Database

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

fitness_project/
│
├── fitness_project/      # Main project settings
├── tracker/              # App (models, views, urls)
├── templates/            # HTML files
├── db.sqlite3            # Database
├── manage.py             # Django entry point

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the repository
git clone https://github.com/NARENDRA970ROYAL/fitness_tracker.git
cd fitness_tracker/fitness_project

### 2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install dependencies
pip install django

### 4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

### 5️⃣ Start server
python manage.py runserver

### 6️⃣ Open in browser
http://127.0.0.1:8000/

---

## 🔐 Admin Panel

Access admin panel:
http://127.0.0.1:8000/admin/

Create superuser:
python manage.py createsuperuser

---

## 🎯 Usage

- Register a new user  
- Login to your account  
- Add fitness data  
- View your personal fitness records  

---

## 📸 Screenshots

(Add your project screenshots here)

---

## 👨‍💻 Author

Narendra Reddy  
GitHub: https://github.com/NARENDRA970ROYAL  

---

## 📌 Future Improvements

- 📊 Charts & Graphs  
- ✏️ Edit/Delete Data  
- 📱 Mobile Responsive UI  
- ☁️ Deployment (Live App)  

---

## ⭐ If you like this project, give it a star!

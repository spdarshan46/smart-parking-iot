🚗 Smart Parking IoT System

A Django-based IoT simulation system that tracks parking space occupancy in real-time using REST APIs and an automated device simulator.

---

\ 📌 Project Overview

This project simulates a smart parking system where a device updates the parking slot state (`empty` or `occupied`) via a REST API every 5 seconds.

The system stores the state in a database and dynamically updates the frontend.

---

🚀 Features

- Django Backend
- Django REST Framework API
- Real-time state update via simulator
- Automatic database creation
- API endpoint for device communication
- Clean frontend UI
- Static image switching (Empty / Occupied)
- Admin panel support

---

🛠 Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- HTML / CSS
- REST API
- Requests Library (Simulator)

---

 🧠 System Architecture

Device (Simulator Script)
        ↓
PUT Request → Django REST API
        ↓
Database Update
        ↓
Frontend Render (Live State Display)

---

 📂 Project Structure

```

smart-parking-iot/
│
├── manage.py
├── smartParkingSystem/
├── iot/
│   ├── models.py
│   ├── views.py
│   ├── api.py
│   ├── simulator/
│   │   └── parking_simulator.py
│   └── templates/
├── static/
├── requirements.txt
└── .gitignore

```

---

⚙️ Installation & Setup

 1️⃣ Clone Repository

```

git clone [https://github.com/spdarshan46/smart-parking-iot.git](https://github.com/spdarshan46/smart-parking-iot.git)
cd smart-parking-iot

```

2️⃣ Create Virtual Environment

```

python -m venv venv
venv\Scripts\activate

```

 3️⃣ Install Dependencies

```

pip install -r requirements.txt

```

 4️⃣ Run Migrations

```

python manage.py migrate

```

5️⃣ Start Server

```

python manage.py runserver

```

Open:
```

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

```

---

 🤖 Run IoT Simulator

In another terminal:

```

python iot/simulator/parking_simulator.py

```

This will update parking state every 5 seconds.

---

🔌 API Endpoint

GET current state:

```

[http://127.0.0.1:8000/api/state/1/](http://127.0.0.1:8000/api/state/1/)

```

Update state:

```

PUT /api/state/1/
{
"name": "occupied"
}

```

---

 📈 Future Improvements

- Real IoT device integration (ESP32 / Arduino)
- WebSocket real-time updates
- Multiple parking slots support
- Dashboard analytics
- Deployment on cloud
- Authentication system

---

 👨‍💻 Author

Darshan S P  
Computer Science Engineer  
Backend & IoT System Developer

---

 ⭐ Project Purpose

This project demonstrates:
- Backend development skills
- REST API design
- IoT simulation architecture
- Database handling
- Automation scripting
```

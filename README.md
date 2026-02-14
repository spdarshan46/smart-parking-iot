 🚗 Smart Parking IoT System

A Django-based IoT simulation system that monitors parking slot occupancy in real time using REST APIs and an automated simulator.

<img width="1361" height="720" alt="image" src="https://github.com/user-attachments/assets/332ee356-0579-484a-802d-38e94c23a88a" />
<img width="1365" height="718" alt="image" src="https://github.com/user-attachments/assets/1abbfa5d-19be-4d4e-b350-214fbf9164e9" />
<img width="1363" height="725" alt="image" src="https://github.com/user-attachments/assets/1d9b4221-448b-4072-8650-62ddf7d27dc9" />

---

📌 Project Overview

This project simulates a Smart Parking System where a parking sensor (simulated device) updates the parking slot state (`empty` or `occupied`) every 5 seconds via a REST API.

The backend stores the state in a database and dynamically displays it on a web interface.

---

 🚀 Features

- Django Backend
- Django REST Framework API
- Real-time state updates
- IoT Simulator Script
- Automatic state creation
- Static UI with dynamic image change
- Clean project architecture
- SQLite database integration

---

🛠 Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- HTML & CSS
- REST API
- Requests Library

---

🧠 System Architecture

IoT Device (Simulator Script)
        ↓
PUT Request → Django REST API
        ↓
Database Update
        ↓
Frontend Displays Current Parking Status

---

 📂 Project Structure

```

smart-parking-iot/
│
├── manage.py
├── smartParkingSystem/
│
├── iot/
│   ├── models.py
│   ├── views.py
│   ├── api.py
│   ├── serializers.py
│   ├── simulator/
│   │   └── parking_simulator.py
│   └── templates/
│
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

 4️⃣ Apply Migrations

```

python manage.py migrate

```

 5️⃣ Run Server

```

python manage.py runserver

```

Open in browser:

```

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

```

---

 🤖 Run IoT Simulator

Open another terminal and run:

```

python iot/simulator/parking_simulator.py

```

The simulator updates parking state every 5 seconds.

---

🔌 API Endpoint

Get current parking state:

```

GET [http://127.0.0.1:8000/api/state/1/](http://127.0.0.1:8000/api/state/1/)

```

Update state manually:

```

PUT [http://127.0.0.1:8000/api/state/1/](http://127.0.0.1:8000/api/state/1/)
{
"name": "occupied"
}

```

---

 📈 Future Improvements

- Multiple parking slots support
- Real IoT hardware integration (ESP32 / Arduino)
- WebSocket for live updates
- Authentication system
- Dashboard analytics
- Cloud deployment

---

👨‍💻 Author

S P Darshan
Computer Science Engineer  
Backend & IoT System Developer

---

 ⭐ Purpose

This project demonstrates:

- Backend API development
- Database management
- IoT simulation logic
- Automation scripting
- Full-stack integration
```


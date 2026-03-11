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


<img width="1361" height="720" alt="image" src="https://github.com/user-attachments/assets/332ee356-0579-484a-802d-38e94c23a88a" />
<img width="1365" height="718" alt="image" src="https://github.com/user-attachments/assets/1abbfa5d-19be-4d4e-b350-214fbf9164e9" />
<img width="1363" height="725" alt="image" src="https://github.com/user-attachments/assets/1d9b4221-448b-4072-8650-62ddf7d27dc9" />

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

IoT Device (Simulator Script)
        ↓
PUT Request → Django REST API
        ↓
Database Update
        ↓
Frontend Render (Live State Display)

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
│   ├── simulator/
│   │   └── parking_simulator.py
│   └── templates/
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
[http://127.0.0.1:8000/]

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

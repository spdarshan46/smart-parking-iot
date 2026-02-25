<<<<<<< HEAD
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
=======
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
>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5

---

🛠 Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
<<<<<<< HEAD
- HTML / CSS
- REST API
- Requests Library (Simulator)

---

 🧠 System Architecture

Device (Simulator Script)
=======
- HTML & CSS
- REST API
- Requests Library

---

🧠 System Architecture

IoT Device (Simulator Script)
>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5
        ↓
PUT Request → Django REST API
        ↓
Database Update
        ↓
<<<<<<< HEAD
Frontend Render (Live State Display)
=======
Frontend Displays Current Parking Status
>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5

---

 📂 Project Structure

```

smart-parking-iot/
│
├── manage.py
├── smartParkingSystem/
<<<<<<< HEAD
=======
│
>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5
├── iot/
│   ├── models.py
│   ├── views.py
│   ├── api.py
<<<<<<< HEAD
│   ├── simulator/
│   │   └── parking_simulator.py
│   └── templates/
=======
│   ├── serializers.py
│   ├── simulator/
│   │   └── parking_simulator.py
│   └── templates/
│
>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5
├── static/
├── requirements.txt
└── .gitignore

```

---

⚙️ Installation & Setup

<<<<<<< HEAD
 1️⃣ Clone Repository
=======
1️⃣ Clone Repository
>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5

```

git clone [https://github.com/spdarshan46/smart-parking-iot.git](https://github.com/spdarshan46/smart-parking-iot.git)
cd smart-parking-iot

```

<<<<<<< HEAD
2️⃣ Create Virtual Environment
=======
 2️⃣ Create Virtual Environment
>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5

```

python -m venv venv
venv\Scripts\activate

```

 3️⃣ Install Dependencies

```

pip install -r requirements.txt

```

<<<<<<< HEAD
 4️⃣ Run Migrations
=======
 4️⃣ Apply Migrations
>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5

```

python manage.py migrate

```

<<<<<<< HEAD
5️⃣ Start Server
=======
 5️⃣ Run Server
>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5

```

python manage.py runserver

```

<<<<<<< HEAD
Open:
=======
Open in browser:

>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5
```

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

```

---

 🤖 Run IoT Simulator

<<<<<<< HEAD
In another terminal:
=======
Open another terminal and run:
>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5

```

python iot/simulator/parking_simulator.py

```

<<<<<<< HEAD
This will update parking state every 5 seconds.
=======
The simulator updates parking state every 5 seconds.
>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5

---

🔌 API Endpoint

<<<<<<< HEAD
GET current state:

```

[http://127.0.0.1:8000/api/state/1/](http://127.0.0.1:8000/api/state/1/)

```

Update state:

```

PUT /api/state/1/
=======
Get current parking state:

```

GET [http://127.0.0.1:8000/api/state/1/](http://127.0.0.1:8000/api/state/1/)

```

Update state manually:

```

PUT [http://127.0.0.1:8000/api/state/1/](http://127.0.0.1:8000/api/state/1/)
>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5
{
"name": "occupied"
}

```

---

 📈 Future Improvements

<<<<<<< HEAD
- Real IoT device integration (ESP32 / Arduino)
- WebSocket real-time updates
- Multiple parking slots support
- Dashboard analytics
- Deployment on cloud
- Authentication system

---

 👨‍💻 Author

Darshan S P  
=======
- Multiple parking slots support
- Real IoT hardware integration (ESP32 / Arduino)
- WebSocket for live updates
- Authentication system
- Dashboard analytics
- Cloud deployment

---

👨‍💻 Author

S P Darshan
>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5
Computer Science Engineer  
Backend & IoT System Developer

---
<<<<<<< HEAD

 ⭐ Project Purpose

This project demonstrates:
- Backend development skills
- REST API design
- IoT simulation architecture
- Database handling
- Automation scripting
```
=======
>>>>>>> 11523fd62e18fdec4a40e041f27a32cb76dc73b5

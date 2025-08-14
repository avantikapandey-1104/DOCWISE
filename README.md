
# Docwise – Smart Health Assistant 🩺🤖
Docwise is an intelligent, interactive web-based health assistant built with Flask, HTML, CSS, and JavaScript, designed to help users get instant health guidance, schedule doctor appointments, and manage health records.
The system provides symptom-based advice, voice input, chatbot interaction, PDF health reports, and doctor recommendations for multiple cities in India — all without using Machine Learning models.

🚀 Features

🩺 Symptom Checker – Get instant health advice based on symptoms entered.

🎤 Voice Input – Speak your symptoms for hands-free interaction.

💬 Chatbot – Ask health-related questions and get instant responses.

🏥 Doctor Finder – Suggests doctors in your city with specialization.

📅 Appointment Scheduler – Book and manage doctor appointments.

📄 PDF Report Generator – Generate and download your diagnosis report.

🎨 Responsive UI – Clean, mobile-friendly interface with centered forms and chatbot.

🌍 City-wise Doctor Data – Preloaded famous doctors from all major Indian cities.

🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Python (Flask)

Database: JSON-based data (for doctors & chatbot knowledge base)

Other: FPDF for PDF generation, Web Speech API for voice input

📂 Project Structure
Docwise/
│
├── static/                 # CSS, JS, images
│   ├── style.css           # Main styling
│   └── chatbot.js          # Chatbot logic
│
├── templates/              # HTML pages
│   ├── index.html          # Main form
│   ├── result.html         # Prediction result page
│   └── chatbot.html        # Chat interface
│
├── app.py                  # Flask backend
├── doctors.json            # Doctor database by city
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation


Open in browser
http://127.0.0.1:5000

📸 Screenshots

<img width="347" height="300" alt="Screenshot 2025-08-14 113353" src="https://github.com/user-attachments/assets/b2ae9b85-eeb5-4f1c-accf-dc618f59c36b" />

<img width="968" height="858" alt="Screenshot 2025-08-14 113448" src="https://github.com/user-attachments/assets/e839397e-72ae-4031-94cb-e0e5bfcf21a7" />

<img width="1226" height="565" alt="Screenshot 2025-08-14 113616" src="https://github.com/user-attachments/assets/c06764ff-2370-4c2d-9063-c75d12990553" />


📅 Future Enhancements

🧠 AI-based symptom diagnosis

🌐 Multi-language support

📊 Health analytics dashboard

🔒 User authentication & profile management

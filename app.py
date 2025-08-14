from flask import Flask, render_template, request
from fpdf import FPDF
from flask import send_file
import datetime
import os

app = Flask(__name__)

# ----------------------------
# 🧠 Step 1: Health Knowledge Base
# ----------------------------
health_knowledge = {
    "fever": "Fever is a temporary increase in body temperature, often due to infection.",
    "cold": "Common cold is a viral infection that affects your nose and throat.",
    "cough": "Cough is a reflex action to clear your airways of mucus or irritants.",
    "diabetes": "Diabetes is a condition that impairs the body's ability to process blood glucose.",
    "blood pressure": "Normal blood pressure is around 120/80 mmHg.",
    "headache": "Headaches can be caused by stress, dehydration, or neurological conditions.",
    "vomiting": "Vomiting is the body's way of removing harmful substances from the stomach.",
    "sore throat": "Sore throat is often caused by viral or bacterial infections.",
    "itching": "Itching can be caused by allergies, skin conditions, or infections."
    # ✅ You can keep adding more questions and answers here.
}


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    age = int(request.form['age'])
    symptoms = request.form['symptoms'].lower()
    city = request.form['city'].lower()

    # 1️⃣ Disease Diagnosis Logic
    if any(word in symptoms for word in ['fever', 'cough', 'cold', 'breath','running nose']):
        diagnosis = "Possible flu, COVID-19, or common cold. Stay hydrated and rest. Consult a doctor if symptoms worsen."
    elif any(word in symptoms for word in ['headache', 'migraine', 'dizziness','sad','tired','low','anxious']):
        diagnosis = "May be due to stress, dehydration, or migraine. Do meditaion and exercises."
    elif any(word in symptoms for word in ['stomach', 'nausea', 'vomit', 'diarrhea','constipation']):
        diagnosis = "Could be food poisoning or gastrointestinal issue."
    elif any(word in symptoms for word in ['chest', 'pain', 'palpitation']):
        diagnosis = "Possible heart-related issue. Please consult a cardiologist."
    elif any(word in symptoms for word in ['rash', 'itching', 'allergy']):
        diagnosis = "May be an allergic reaction or skin infection."
    elif any(word in symptoms for word in ['eye', 'blur', 'vision']):
        diagnosis = "Might be related to eye strain or infection."
    elif any(word in symptoms for word in ['fatigue', 'tired', 'weakness']):
        diagnosis = "General fatigue. May need rest and nutrition."
    else:
        diagnosis = "Symptoms not clearly matched. Please consult a doctor."

    # 2️⃣ Doctor Recommendation by City
    doctors = {
    "delhi": [
        "Dr. Mehta - AIIMS",
        "Dr. Arora - Max Hospital, Saket",
        "Dr. Gupta - Apollo Hospitals, Sarita Vihar"
    ],
    "mumbai": [
        "Dr. Joshi - Lilavati Hospital, Bandra",
        "Dr. Shah - Kokilaben Dhirubhai Ambani Hospital, Andheri",
        "Dr. Patel - P.D. Hinduja National Hospital, Mahim"
    ],
    "bangalore": [
        "Dr. Rao - Manipal Hospital, Malleshwaram",
        "Dr. Das - Fortis Hospital, Bannerghatta Road",
        "Dr. Kumar - Apollo Hospital, Jayanagar"
    ],
    "chennai": [
        "Dr. Sundaram - Apollo Hospitals, Greams Road",
        "Dr. Krishnan - Global Hospitals, Perumbakkam",
        "Dr. Sivakumar - MIOT Hospitals, Manapakkam"
    ],
    "kolkata": [
        "Dr. Banerjee - AMRI Hospitals, Mukundapur",
        "Dr. Mukherjee - Fortis Hospital, Anandapur",
        "Dr. Chatterjee - Apollo Gleneagles, Salt Lake"
    ],
    "hyderabad": [
        "Dr. Reddy - Apollo Hospitals, Jubilee Hills",
        "Dr. Sharma - Yashoda Hospitals, Secunderabad",
        "Dr. Singh - CARE Hospitals, Banjara Hills"
    ],
    "pune": [
        "Dr. Deshmukh - Ruby Hall Clinic, Shivajinagar",
        "Dr. Kulkarni - Aditya Birla Hospital, Kalyani Nagar",
        "Dr. Patil - Jehangir Hospital, Sassoon Road"
    ],
    "ahmedabad": [
        "Dr. Shah - Sterling Hospital, Navrangpura",
        "Dr. Mehta - Apollo Hospitals, Ghodasar",
        "Dr. Doshi - CIMS Hospital, Vastrapur"
    ],
    "lucknow": [
        "Dr. Verma - SGPGI",
        "Dr. Tiwari - Sahara Hospital",
        "Dr. Gupta - KGMU Medical College"
    ],
    "patna": [
        "Dr. Sinha - Paras HMRI",
        "Dr. Pandey - Ruban Hospital",
        "Dr. Kumar - Indira Gandhi Institute of Medical Sciences"
    ],
    "kanpur": [
        "Dr. Mohd Shahid - Apollo Spectra",
        "Dr. Manish Verma - Fortune Hospital",
        "Dr. Singh - Ganesh Shankar Vidyarthi Memorial (GSVM) Hospital"
    ],
    "jaipur": [
        "Dr. Sharma - SMS Hospital, Ram Nagar",
        "Dr. Jain - Fortis Escorts",
        "Dr. Mehta - Santokba Durlabhji Memorial Hospital"
    ],
    "coimbatore": [
        "Dr. Rangan - PSG Institute Hospital",
        "Dr. Krishnan - Kovai Medical Center & Hospital",
        "Dr. Iyer - Sri Ramakrishna Hospital"
    ],
    "indore": [
        "Dr. Agarwal - Bombay Hospital",
        "Dr. Sharma - Choithram Hospital",
        "Dr. Jain - Apollo Hospital"
    ],
    "nagpur": [
        "Dr. Deshmukh - Wockhardt Hospitals",
        "Dr. Patil - Orange City Hospital",
        "Dr. Kulkarni - Mayo Hospital"
    ],
    "vadodara": [
        "Dr. Patel - Sterling Hospital",
        "Dr. Mehta - Apollo Hospitals",
        "Dr. Trivedi - LN Hospital"
    ],
    "kochi": [
        "Dr. Nair - Amrita Hospital",
        "Dr. Thomas - Lakeshore Hospital",
        "Dr. Menon - Aster Medcity"
    ],
    "thiruvananthapuram": [
        "Dr. Varma - Trivandrum Medical College",
        "Dr. Kumar - Jubilee Mission Hospital",
        "Dr. Menon - KIMS Hospital"
    ],
    "visakhapatnam": [
        "Dr. Rao - Apollo Hospitals",
        "Dr. Reddy - Apollo Institute of Medical Sciences",
        "Dr. Sinha - CARE Hospitals"
    ]
}


    recommended_doctors = doctors.get(city, ["Sorry, no doctor data found for your city."])

    # 3️⃣ Generate PDF Report
    from fpdf import FPDF
    import datetime
    import os

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    pdf.cell(200, 10, txt="Health Report", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Age: {age}", ln=True)
    pdf.cell(200, 10, txt=f"City: {city.title()}", ln=True)
    pdf.multi_cell(200, 10, txt=f"Symptoms: {symptoms}")
    pdf.multi_cell(200, 10, txt=f"Diagnosis: {diagnosis}")
    pdf.multi_cell(200, 10, txt=f"Recommended Doctors: {', '.join(recommended_doctors)}")
    pdf.cell(200, 10, txt=f"Date & Time: {now}", ln=True)

    pdf_filename = f"report_{name.replace(' ', '_')}.pdf"
    pdf_path = os.path.join("static", pdf_filename)
    pdf.output(pdf_path)

    # 4️⃣ Show Result Page with Doctor List + Download Option
    return render_template("result.html", name=name, diagnosis=diagnosis,report_file=pdf_filename,doctors=recommended_doctors)


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['question'].lower()

    # Keyword-based lookup
    response = "Sorry, I couldn't understand that. Please consult a doctor."

    for keyword in health_knowledge:
        if keyword in user_input:
            response = health_knowledge[keyword]
            break

    return render_template("chat.html", question=user_input, answer=response)

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    doctor = request.form['doctor']
    date = request.form['date']
    time = request.form['time']

    # Optionally save to file (for now)
    with open('appointments.csv', 'a') as f:
        f.write(f"{name},{doctor},{date},{time}\n")

    confirmation_msg = f"✅ Appointment confirmed with {doctor} on {date} at {time} for {name}."
    return render_template("confirmation.html", message=confirmation_msg)



if __name__ == '__main__':
    app.run(debug=True)

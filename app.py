from flask import Flask, render_template, request
import os
from pyngrok import ngrok

app = Flask(__name__)

UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():

    file = request.files['image']

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(filepath)

    filename = file.filename.lower()

    if filename.startswith("helmet"):
        violation = "Helmet Detected ✅"
        fine = 0
        explanation = "The rider is wearing a helmet properly, so no traffic violation was found. Safety rules are being followed correctly."


    elif filename.startswith("triple"):
        violation = "Triple Riding Detected ❌"
        fine = 1000
        explanation = "More than two people were found riding on the same bike. Triple riding is unsafe because it can cause imbalance and increase accident risk. A fine has been issued for violating traffic safety rules."

    elif filename.startswith("signal"):
        violation = "Signal Jumping Detected 🚦"
        fine = 1500
        explanation = "The vehicle appears to have crossed the signal during a restricted stop. Ignoring traffic signals can lead to serious accidents and puts other people on the road at risk."

    else:
        violation = "No Helmet Detected ❌"
        fine = 500
        explanation = "The rider was not wearing a helmet while driving. Helmets are important for safety and help reduce serious head injuries during accidents. A safety fine has been applied."

    return render_template(

    'result.html',
    image=file.filename,
    violation=violation,
    fine=fine
)

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')
@app.route('/complaint')
def complaint():
    return render_template('complaint.html')

if __name__ == '__main__':
   public_url = ngrok.connect(5000)

print("Public URL:", public_url)

app.run(port=5000)
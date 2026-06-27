from flask import Flask,render_template, url_for,request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load(r"Model\\RandomForestClassifier.lb")

df=pd.read_csv("Data\\medical_disease.csv")


Gender_list = df['Gender'].unique().tolist()
Gender_dict = {Gender: i for i, Gender in enumerate(Gender_list)}

Smoking_dict={'No':0,'Yes':1}

Alcohol_dict={ 'No':0,'Yes':1}

FamilyHistory_dict={"NO":0,"Yes":1}

PhysicalActivity_dict={'Medium':2, 'High':3, 'Low':1}

Disease_dict={'Healthy':1, 'Pre-Diabetes':2, 'Hypertension':3, 'Heart Disease':4, 'Diabetes':5}
reverse_Disease={v:k for k,v in Disease_dict.items()}

def get_dropdown_options():

    return {
        'Genders': Gender_list,
        'Smokings': list(Smoking_dict.keys()),        
        'Alcohols': list(Alcohol_dict.keys()),
        'FamilyHistories':list(FamilyHistory_dict.keys()),
        'PhysicalActivities': list(PhysicalActivity_dict.keys()),
    }

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/project')
def project():
    return render_template(
        'project.html',
        **get_dropdown_options()
    )


@app.route('/predict', methods=['POST','GET'])
def predict():
    
    age=int(request.form['age'])
    gender=request.form['gender']
    bmi=float(request.form['bmi'])
    bloodpressure=int(request.form['bloodpressure'])
    glucoselevel=int(request.form['glucoselevel'])
    cholesterol=int(request.form['cholesterol'])
    heartrate=int(request.form['heartrate'])
    smoking=request.form['smoking']
    alcohol=request.form['alcohol']
    physicalactivity=request.form['physicalactivity']
    familyhistory=request.form['familyhistory']
    
    
    gender= Gender_dict.get(gender)
    smoking= Smoking_dict.get(smoking)
    alcohol= Alcohol_dict.get(alcohol)
    physicalactivity= PhysicalActivity_dict.get(physicalactivity)
    familyhistory= FamilyHistory_dict.get(familyhistory)
    
    print(age, gender,bmi, bloodpressure, glucoselevel, cholesterol, heartrate, smoking, alcohol, physicalactivity,familyhistory)
    print(type(age), type(gender), type(bmi), type(bloodpressure), type(glucoselevel),type(cholesterol), type( heartrate), type(smoking), type(alcohol), type(physicalactivity), type(familyhistory))

    data = [[age, gender,bmi, bloodpressure, glucoselevel, cholesterol, heartrate, smoking, alcohol, physicalactivity,familyhistory]]
    pred = model.predict(data)
   

    pred = model.predict(data)[0]
    disease= reverse_Disease[pred]
    print("Prediction 🤖🤖>>>>", disease)

    return render_template('project.html',**get_dropdown_options(),prediction=disease)
   


if __name__ == "__main__":
    app.run(debug=True)
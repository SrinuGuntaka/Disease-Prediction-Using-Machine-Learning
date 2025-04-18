from flask import Flask, request
from flask import render_template
from model_and_symptoms import symptoms_name, symptoms_array, disease_name, model
import os
import pandas as pd

app = Flask(__name__)


# main function to render html template
@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        l = [request.form.get('select_symptom_1').lower(),request.form.get('select_symptom_2').lower(),request.form.get('select_symptom_3').lower(),request.form.get('select_symptom_4').lower(),request.form.get('select_symptom_5').lower()]
        """if request.form.get('select_symptom_1').lower() == 'none' and  request.form.get('select_symptom_2').lower() == 'none'\
                and request.form.get('select_symptom_3').lower() == 'none':"""
        print(l.count('none'))
        """if request.form.get('select_symptom_1').lower() == 'none' and  request.form.get('select_symptom_2').lower() == 'none'\
                and request.form.get('select_symptom_3').lower() == 'none':"""
        if l.count('none')>=3:
            prediction = "Please select minimum 3 symptoms"
            Answer= "Please select minimum 3 symptoms"
        else:
            prediction = f"According to the symptoms you may have '{predict_disease()}' "
            XXX =  f'{predict_disease()}'
            df = pd.read_csv("precaution.csv")
            #df2=df[df['Disease']==XXX]
            Answer1=df.loc[df['Disease'] == XXX, 'Precaution_1'].iloc[0]
            Answer2=df.loc[df['Disease'] == XXX, 'Precaution_2'].iloc[0]
            Answer3=df.loc[df['Disease'] == XXX, 'Precaution_3'].iloc[0]
            Answer = str(Answer1) + ", " +str(Answer2) + ", "+str(Answer3) 


    else:
        prediction = "Prediction will show here"
        Answer= "Cures shown here"

    symptoms_name_with_none = symptoms_name.copy()
    sorted_symptoms_name = sorted(symptoms_name_with_none)
    sorted_symptoms_name.insert(0, 'none')
    
    return render_template('index.html', columns_name=sorted_symptoms_name, prediction=prediction, prediction2 = Answer)

def request_symptoms():
    user_symptoms = [request.form.get('select_symptom_1'), request.form.get('select_symptom_2'),
                     request.form.get('select_symptom_3'), request.form.get('select_symptom_4'),
                     request.form.get('select_symptom_5')]

    if request.method == 'POST':
        c=user_symptoms.count('none')
        while 'none' in user_symptoms:
            user_symptoms.remove('none')

        return user_symptoms


def assign_value_to_symptom():
    symptoms_array_copy = symptoms_array.copy()
    user_symptoms = request_symptoms()
    for idx in range(len(symptoms_name)):
        for symptom in user_symptoms:
            if symptom == symptoms_name[idx]:
                symptoms_array_copy[idx] = 1

    return symptoms_array_copy


def predict_disease():
    symptoms = assign_value_to_symptom()
    print(len(symptoms))
    predicted_disease = model.predict([symptoms])
    return predicted_disease[0]


if __name__ == '__main__':
    app.run(debug=True)

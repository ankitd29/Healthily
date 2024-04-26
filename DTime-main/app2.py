from flask import Flask, render_template, request
import pandas as pd
import joblib
import pickle
#from chatbot_healthcare import ml

app = Flask(__name__)

# Load the trained model
# model = joblib.load("HealthiLy\DTime-main\chatbot_ml_healthcare.pkl")


# load the data from the pickle file
#with open("my_data.pkl2", "rb") as f:
    #data = pickle.load(f)

# your existing code here ...

# use the data from the pickle file
#clf = data["clf"]
#le = data["le"]
#la = data["la"]
#symptoms_dict = data["symptoms_dict"]
#severityDictionary = data["severityDictionary"]
#description_list = data["description_list"]
#precautionDictionary = data["precautionDictionary"]


@app.route("/")
@app.route("/home")
def homepage():
    return render_template("index2.html")

@app.route("/mybot")
def mybot():
    return render_template("mybot.html")    
# @app.route("/mybot", methods=["POST"])
    # def upload():
    # Get the uploaded files
    #dataset = request.files["dataset"]
    #symptom_description = request.files["symptom_Description"]
    #symptom_precaution = request.files["symptom_precaution"]
    #symptom_severity = request.files["symptom_severity"]
    #testing_data = request.files["Testing_Data"]
    #training_data = request.files["Training_Data"]

    # p=ml()
    # input_data=request.form.get('input_data')
    # info=p.getInfo(input_data)
    # return render_template('mybot.html',info=info)

    # Use the loaded model to make predictions on the data in the CSV files
    # predictions = model.predict(df_dataset)

    # Process the predictions and return the result
    # result = ...

    # return result


if __name__ == "__main__":
    app.run(debug=True)

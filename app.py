from cmath import nan
from crypt import methods
from operator import methodcaller
from flask import Flask, request, render_template
from tensorflow import keras
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Create an app object using Flask
app = Flask(__name__)

# Load the model
model = keras.models.load_model('models/model.h5')

# Use route() to define URL

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()] # convert string to float
    features = [int_features] # convert input to numpy array
    prediction = model.predict(features)[0][0] # predict using the loaded model
    
    prediction = np.around(prediction, decimals=2)*100

    return render_template('index.html', features= '{}'.format(features), prediction_text='Prediction is {}%'.format(prediction))

if __name__ == "__main__":
    app.run()
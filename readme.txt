Created by Jesús Sánchez Rodríguez
jsr90pro@gmail.com

The purpose of this project is to create a classifier based on
10 inputs to know someone's possibility of suffering a brain stroke.

Link to the dataset: https://www.kaggle.com/datasets/zzettrkalpakbal/full-filled-brain-stroke-dataset

Structure of the project:

data
    full_data.csv
    out.csv
models
    model.h5
templates
    index.html
app.py
neuralNetwork.ipynb
preprocessing.ipynb
readme.txt

Running order:
    1. preprocessing.ipynb (optional, generates out.csv)
    2. neuralNetwork.ipynb (optional, generates model.h5)
    3. app.py
# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'customerpredictionLogRegmodel.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        DayDiff = float(request.form['DayDiff'])
        Recency = int(request.form['Recency'])
        RecencyCluster = int(request.form['RecencyCluster'])
        Frequency = int(request.form['Frequency'])
        FrequencyCluster = int(request.form['FrequencyCluster'])
        Revenue = float(request.form['Revenue'])
        RevenueCluster = int(request.form['RevenueCluster'])
        OverallScore = int(request.form['OverallScore'])
        Segment = int(request.form['Segment'])
        DayDiff1 = float(request.form['DayDiff1'])
        DayDiff2 = float(request.form['DayDiff2'])
        DayDiff3 = float(request.form['DayDiff3'])
        DayDiffMean = float(request.form['DayDiffMean'])
        DayDiffStd = float(request.form['DayDiffStd'])
        #Segment_HighValue = int(request.form['Segment_HighValue'])
        #Segment_LowValue = int(request.form['Segment_LowValue'])
        #Segment_MidValue = int(request.form['Segment_MidValue'])
        
        data = np.array([[DayDiff, Recency, RecencyCluster, Frequency, 
                          FrequencyCluster, Revenue, RevenueCluster, 
                          OverallScore, Segment, DayDiff1, DayDiff2, DayDiff3, 
                          DayDiffMean, DayDiffStd]])#, Segment_HighValue, 
                          #Segment_LowValue, Segment_MidValue]])
        my_prediction = classifier.predict(data)
        
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)
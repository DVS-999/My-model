import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
from flask import Flask, request, render_template
import pickle

app = Flask("__name__")

df_1=pd.read_excel("churn.xlsx",engine='openpyxl')

q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")


@app.route("/", methods=['POST'])
def predict():

    '''
    CUS_Gender
    CUS_Marital_Status
    CUS_Month_Income
    TotaldebittransactionsforS1
    TotaldebittransactionsforS2
    TotaldebittransactionsforS3
    TotaldebitamountforS1
    TotaldebitamountforS2
    TotaldebitamountforS3
    TotalcredittransactionsforS1
    TotalcredittransactionsforS2
    TotalcredittransactionsforS3
    TotalcreditamountforS1
    TotalcreditamountforS2
    TotalcreditamountforS3
    Totaldebitamount
    Totaldebittransactions
    Totalcreditamount
    Totalcredittransactions
    Totaltransactions
    CUS_Target
    '''
    
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']
    inputQuery9 = request.form['query9']
    inputQuery10 = request.form['query10']
    inputQuery11 = request.form['query11']
    inputQuery12 = request.form['query12']
    inputQuery13 = request.form['query13']
    inputQuery14 = request.form['query14']
    inputQuery15 = request.form['query15']
    inputQuery16 = request.form['query16']
    inputQuery17 = request.form['query17']
    inputQuery18 = request.form['query18']
    inputQuery19 = request.form['query19']
    inputQuery20 = request.form['query20']
    inputQuery21 = request.form['query21']
    
    model = pickle.load(open("model.dvs", "rb"))
    
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, 
             inputQuery8, inputQuery9,inputQuery10, inputQuery11,inputQuery12, inputQuery13,inputQuery14, 
             inputQuery15, inputQuery16,inputQuery17, inputQuery18,inputQuery19,inputQuery20,inputQuery21]]
    
    new_df = pd.DataFrame(data, columns = ['CUS_Gender','CUS_Marital_Status','CUS_Month_Income','TotaldebittransactionsforS1',
                                            'TotaldebittransactionsforS2','TotaldebittransactionsforS3','TotaldebitamountforS1','TotaldebitamountforS2','TotaldebitamountforS3',
                                            'TotalcredittransactionsforS1','TotalcredittransactionsforS2','TotalcredittransactionsforS3','TotalcreditamountforS1','TotalcreditamountforS2',
                                            'TotalcreditamountforS3','Totaldebitamount','Totaldebittransactions','Totalcreditamount','Totalcredittransactions','Totaltransactions','CUS_Target'])
    
    df_2 = pd.concat([df_1, new_df], ignore_index = True) 
    
    
    
    
    
    new_df__dummies = pd.get_dummies(df_2[['CUS_Gender','CUS_Marital_Status','CUS_Month_Income','TotaldebittransactionsforS1',
                                            'TotaldebittransactionsforS2','TotaldebittransactionsforS3','TotaldebitamountforS1','TotaldebitamountforS2','TotaldebitamountforS3',
                                            'TotalcredittransactionsforS1','TotalcredittransactionsforS2','TotalcredittransactionsforS3','TotalcreditamountforS1','TotalcreditamountforS2',
                                            'TotalcreditamountforS3','Totaldebitamount','Totaldebittransactions','Totalcreditamount','Totalcredittransactions','Totaltransactions','CUS_Target']])
    
    
    #final_df=pd.concat([new_df__dummies, new_dummy], axis=1)
        
    
    single = model.predict(new_df__dummies.tail(1))
    probablity = model.predict_proba(new_df__dummies.tail(1))[:,1]
    
    if single==1:
        o1 = "This customer is likely to be churned!!"
        o2 = "Confidence: {}".format(probablity*100)
    else:
        o1 = "This customer is likely to continue!!"
        o2 = "Confidence: {}".format(probablity*100)
        
    return render_template('home.html', output1=o1, output2=o2, 
                            query1 = request.form['query1'], 
                            query2 = request.form['query2'],
                            query3 = request.form['query3'],
                            query4 = request.form['query4'],
                            query5 = request.form['query5'], 
                            query6 = request.form['query6'], 
                            query7 = request.form['query7'], 
                            query8 = request.form['query8'], 
                            query9 = request.form['query9'],
                            query10 = request.form['query10'],
                            query11 = request.form['query11'],
                            query12 = request.form['query12'],
                            query13 = request.form['query13'],
                            query14 = request.form['query14'],
                            query15 = request.form['query15'],
                            query16 = request.form['query16'],
                            query17 = request.form['query17'],
                            query18 = request.form['query18'],
                            query19 = request.form['query19'],
                            query20 = request.form['query20'],
                            query21 = request.form['query21'])
    
app.run(debug=True)


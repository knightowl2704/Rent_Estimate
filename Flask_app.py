#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask 
import numpy as np 
import pandas as pd
from flask import jsonify
from flask import render_template

import pickle
# Flask constructor takes the name of  
# current module (__name__) as argument. 
app = Flask(__name__)
  
# The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function. 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/?bedrooms=<bedrooms>&bathrooms=<bathrooms>&area=<area>') 
def rent_estimate(bedrooms,bathrooms,area):
    no_bathrooms = bathrooms
    no_bedrooms = bedrooms
    area = area
    
    model = pickle.load(open('pickle_model.pkl','rb'))
    encoder = pickle.load(open('encoder.pkl','rb'))
    minmax = pickle.load(open('minmax.pkl','rb'))
    d = {'Bedrooms': [no_bedrooms], 'Bathrooms': [no_bathrooms]}
    df = pd.DataFrame(data=d)
    citytransform = encoder.transform([area])
    citytransform = pd.DataFrame(citytransform)
    df = pd.concat([df, citytransform], axis=1)
    ans = model.predict(df).reshape(-1,1)
    rent_estimate = minmax.inverse_transform(ans)[0][0]
    response = {
        'Bedrooms':no_bedrooms,
        'Bathrooms':no_bathrooms,
        'Area':area,
        'Estimated Rent':rent_estimate
    }
    json_resp = jsonify(response)
    json_resp.status_code = 200
    print(json_resp)
    return json_resp

# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the lo
    app.run(debug=True)
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)


# In[12]:





# In[ ]:





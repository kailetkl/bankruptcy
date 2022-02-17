#!/usr/bin/env python
# coding: utf-8

# In[47]:


from flask import Flask


# In[48]:


app = Flask(__name__)
#ensures that this is your programme, not sklearn.py


# In[49]:


from flask import request, render_template
from keras.models import load_model

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        NPTA = request.form.get("NPTA")
        TLTA = request.form.get("TLTA")
        WCTA = request.form.get("WCTA")
        print(NPTA, TLTA, WCTA)
        model=load_model("bankruptcy")        
        pred=model.predict([[float(NPTA),float(TLTA),float(WCTA)]])
        s = "The predicted bankruptcy score is: " + str(pred)
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("80"))
    
#only if it is ur programme, then run 


# In[ ]:





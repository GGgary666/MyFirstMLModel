from flask import request, render_template
from flask import Flask
import joblib
import sys
app = Flask(__name__)
path = sys.path[0]
model = joblib.load(path+"/ChocolateTaste")

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        print("dsds")
        sugar = request.form.get("sugar")
        milk = request.form.get("milk")
        print(sugar,milk)
        pred = model.predict([[sugar,milk]])
        print(pred)
        pred = pred[0]
        s = "The predicted Chocolate Taste is :",str(pred)
        return(render_template("index.html",result = s))
    else:
        return(render_template("index.html",result = "Chocolate Taste Prediction"))

if __name__ == "__main__":
    app.run()

from flask import Flask, render_template,request
import json
import urllib.request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if (request.method) == "GET":
        return render_template("index.html")
    elif (request.method) == "POST":
        data =  {
  "Inputs": {
    "data": [
      {
        "Gender": "example_value",
        "Age": 0,
        "Annual Income (k$)": 0
      }
    ]
  },
  "GlobalParameters": 1.0
}
        body = str.encode(json.dumps(data))

        url = 'http://f2e66717-cb27-4169-929e-c690c7478809.eastus.azurecontainer.io/score'
        api_key = '' # Replace this with the API key for the web service

        # The azureml-model-deployment header will force the request to go to a specific deployment.
        # Remove this header to have the request observe the endpoint traffic rules
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib.request.Request(url, body, headers)
        response = urllib.request.urlopen(req)
        result = response.read()
        dict_str = json.loads(result.decode("UTF-8"))
        my_data = dict_str.get('Results')[0]
        return render_template("index.html",output=my_data)
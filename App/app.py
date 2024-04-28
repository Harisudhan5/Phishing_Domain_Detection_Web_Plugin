from flask import Flask, request, jsonify
import pickle
from FeatureExtraction import FeatureExtraction
import numpy as np

app = Flask(__name__)

@app.route('/get_url', methods=['POST'])
def get_url():
    try:
        data = request.get_json()
        url = data['url']
        print("ok done")
        with open('C://Projects//Phishing_Domain_Detection_Web_Extension//Model//phish.pkl', 'rb') as file:
            print("readed--------")
            print(url)
            gbc = pickle.load(file)
            urls = url
            ul = FeatureExtraction(urls)
            print("Extracted Features........",ul)
            x = np.array(ul.getFeaturesList()).reshape(1,30) 
            y_pred =gbc.predict(x)[0]
            print("Responding for the request sent by Flask application")
            print(y_pred)
            y_pro_phishing = gbc.predict_proba(x)[0,0]
            y_pro_non_phishing = gbc.predict_proba(x)[0,1]
            print("output == ",y_pred)
            print("phishing probabilty :",y_pro_phishing)
            print("non phishing probability :",y_pro_non_phishing)
            print(y_pred)
            rests = 0
            if y_pred == 1:rests = "The site is Safe"
            else:rests = "The site is Unsafe"
            # Example: You can return a JSON res    ponse.
            print(rests)
        response_data = {'result':rests ,"val":y_pro_non_phishing}
        return jsonify(response_data)
    except Exception as e:
        return jsonify({'error + error occured'})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

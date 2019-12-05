from flask import Flask,jsonify, request
app = Flask(__name__)

#function for generating error strings
# Error code 1 - wrong format 
# Error code 2 - wrong request type
def getErrorStatements(errorCode):
    errorMessage1 = "You have entered a wrong format. Kindly retry request using string format"
    errorMessage2 = "You used a wrong format for the request, kindly use a GET request to the route /permutation-index"

@app.route('/',methods=['GET','POST'])
def index():
    some_json = request.get_json()
    return jsonify({'you sent' : some_json}),201
@app.route('/permutation-index',methods=['GET'])
def getPermutation():
    if (request.method == 'GET'):
        some_json = request.get_json()
        return jsonify({'"indexOfGivenPermutation":' : some_json}),201
    else:
        some_json = request.get_json()
        return jsonify({"about":some_json})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template, jsonify
import json
obj = Flask(__name__)

@obj.route('/')
def welcome():
    return "Welcome to Flask."

@obj.route('/cal',methods=["GET"])
def math_operator():
    operation= request.json["operation"]
    number1= int(request.json["number1"])
    number2=int(request.json["number2"])

    if operation =="add":
        result = number1 + number2
    elif operation == "multiply":
        result = number1*number2
    elif operation == "divide":
        result = number1/number2
    else:
        result = number1-number2

    #return jsonify(result)
    return "The operaton is {} and the result is {}".format(operation, result)

if __name__== '__main__':
    obj.run(debug=True)

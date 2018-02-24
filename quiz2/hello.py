from flask import Flask,request,Response
from flask import jsonify
app=Flask(__name__)
global dict1
dict1 ={}


@app.route("/")
def hello():
    
    return "hello world"
 

@app.route('/users',methods=['POST','GET'])
def get1():
    if request.method=='POST':
        #dict1={}
        dict1["id"]=1
        dict1["name"]=request.form["name"]
        #dict1.save()
        return jsonify(dict1) 
@app.route('/users/<id1>',methods=['GET','DELETE'])
def get2(id1):
    if request.method=='GET':
        if dict1["id"]==int(id1):
            return jsonify(dict1)
    if  request.method=='DELETE':
         if dict1["id"]==int(id1):
             del dict1["id"]
             del dict1["name"]
             return jsonify(dict1)      
        
    





        

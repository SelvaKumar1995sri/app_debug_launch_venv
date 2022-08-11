from flask import Flask,request,Response
import json

app = Flask(__name__)

@app.route('/',methods=['Get'])
def view():
    x=open('fish_data.json','r')
    data_obj=json.load(x)
    data_list=data_obj['fish_collection']
    
    return Response(json.dumps(data_list),  mimetype='application/json')

@app.route('/add',methods=['POST'])
def add():
    val = request.get_json()   
    x=open("fish_data.json",'r')
    data_obj = json.load(x) 
    data_list = data_obj['fish_collection']
    data_list.append(val)
    with open('fish_data.json','w') as y:
        json.dump(data_obj,y)
    return "Success"

    


if __name__ == ('__main__'):
    app.run(debug=True)
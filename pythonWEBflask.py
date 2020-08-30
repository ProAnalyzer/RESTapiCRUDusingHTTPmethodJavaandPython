#http://127.0.0.1:7777//
#http://127.0.0.1:7777//empdb/employee  (GET,POST)
#http://127.0.0.1:7777//empdb/employee/E01   (GET,PUT,DELETE)

from flask import Flask, request, jsonify, abort
app = Flask(__name__)
empDB=[
 {
 'empNo':'E01',
 'empName':'Pronay',
 'position':'Technical Leader'
 },
 {
 'empNo':'E02',
 'empName':'Ayan',
 'posiiton':'Sr Software Engineer'
 }, 
 {
 'empNo':'E03',
 'empName':'Pratap',
 'position':'Sales Manager'
 }
 ]

@app.route("/")
def hello():
    return "Welcome to R.S family!"

@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})

@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['empNo'] == empId) ] 
    return jsonify({'emp':usr})


@app.route('/empdb/employee/<empId>',methods=['PUT'])
def updateEmp(empId): 
    em = [ emp for emp in empDB if (emp['empNo'] == empId) ] 
    if 'empName' in request.json : 
        em[0]['empName'] = request.json['empName'] 
    if 'position' in request.json:
        em[0]['position'] = request.json['position'] 
    return jsonify({'emp':em[0]})


@app.route('/empdb/employee',methods=['POST'])
def createEmp(): 
    dat = {
    'empNo': request.json['empNo'],
    'empName': request.json['empName'],
    'position': request.json['position']
    }
    empDB.append(dat)
    return jsonify(dat)


@app.route('/empdb/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId): 
    em = [ emp for emp in empDB if (emp['empNo'] == empId) ] 
    if len(em) == 0:
        abort(404) 
    empDB.remove(em[0])
    return jsonify({'response':'Success'})


if __name__ == "__main__":
    app.run(port = 7777)
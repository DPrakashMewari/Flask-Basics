from flask import Flask,jsonify,request

Prakash = Flask(__name__)

# GET
@Prakash.route("/for_get",methods=['GET'])
def for_get():
    if request.method == 'GET':
        d1 = {
			"Hello": "World"
		}

        return jsonify(d1) 

# POST    
@Prakash.route("/for_post",methods=['POST'])
def for_post():
    if request.method == 'POST':
        name=request.form.get("name"),
        map_url=request.form.get("map_url")
        print(name,map_url)  
        resp= {}
        resp['name'] = str(name)
        resp['map_url'] = str(map_url)
        return jsonify(resp)    

# DELETE
@Prakash.route("/for_delete/<id>",methods=['DELETE'])
def for_delete(id):
    resp = {'1' :'name','2': 'surname'}
    if request.method == 'DELETE':
        if id in resp.keys():
            print('INSIDE')
            del resp[id]
            return 'Success'
        return 'Success'

# UPDATE
@Prakash.route("/for_update/",methods=['PUT'])
def for_update():
    resp = request.get_json()
    return resp



if __name__ == "__main__":
    Prakash.run(debug=True)
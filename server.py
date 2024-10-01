import flask, BivittatusDB as bdb, requests
import requests.cookies
PORT = 54505
app=flask.Flask(__name__)

###################### USERS ######################
#Get list of users when get method is called
@app.route("/users", methods=['GET'])
def GET_USER():
    pass

#Get user by ID
@app.route("/users/<int:id>", methods=['GET'])
def GET_USER_BY_ID(id:int):
    pass

#create new user when post method is called
@app.route("/users", methods=['POST'])
def MAKE_USER():
    data=flask.request.get_json()
    pass

#Update user from id
@app.route("/users/<int:id>", methods=['PUT'])
def UPDATE_USER(id: int):
    data=flask.request.get_json()
    pass

#delete user by Id
@app.route("/users/<int:id>", methods=["DELETE"])
def DELETE_USER(id: int):
    pass

###################### DATABASE ######################
#get a list of databases
@app.route("/database", methods=["GET"])
def GET_DATABASE():
    pass

#get list of tables from database
@app.route("/database/<string:basename>", methods=["GET"])
def GET_TABLES(basename:str):
    pass

#create a new database
@app.route("/database/<string:basename>", methods=["POST"])
def CREATE_DATABASE(basename:str):
    data=flask.request.get_json()
    pass

#delete a database by name
@app.route("/database/<string:basename>", methods=["DELETE"])
def DELETE_DATABASE(basename:str):
    pass

#############################################
# I don't have a "PUT" method for databases #
# yet cause I don't have a viable idea for  #
# what updating the database (as opposed    #
# to updating a table) is. Our library only #
# has get and make type methods. Possibly   #
# something to look into.                   #
#############################################

###################### TABLES ######################
#Return database data as JSON
@app.route("/database/<string:basename>/<string:table>", methods=["GET"])
def GET_DATA(basename:str, table:str):
    pass

@app.route("/database/<string:basename>/<string:table>", methods=["POST"])
def MAKE_TABLE(basename:str, table:str):
    data=flask.request.get_json()
    pass

@app.route("/database/<string:basename>/<string:table>", methods=["PUT"])
def UPDATE_TABLE(basename:str, table:str):
    data=flask.request.get_json()
    pass

@app.route("/database/<string:basename>/<string:table>", methods=["DELETE"])
def DELETE_TABLE(basename:str, table:str):
    pass

###################### SYS ######################
# set a system variable using localhost:/sys/<varaible_name>?value=<Value>
@app.route("/sys/<string:var>", methods=["GET"])
def SET_VAR(var:str):
    if flask.request.args.get('value'):
        resp=flask.make_response()
        resp.set_cookie(var, flask.request.args.get('value'))
        return resp
    else:
        r=flask.request.cookies.get(var)
        return r

@app.route("/sys/exec")
def EXEC():
    exec(flask.request.args.get('query'))

if __name__=='__main__':
    app.run(port=PORT)
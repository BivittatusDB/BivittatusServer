port=54505

import requests

keywords=[
    "TABLE",
    "DATABASE",
    "USER",
    "USE",
    "SET",
    "SYS"
]
SESS=requests.Session()
db=None
tb=None

class req:
    def __init__(self, path) -> None:
        self.root_path=path

    def GET(self, data=..., var_name="query"):
        if data:
            SESS.get(self.root_path+f"?{var_name}={data}")
        else:
            SESS.get(self.root_path)

    def POST(self, data):
        SESS.post(self.root_path, json=data)

    def PUT(self, data):
        SESS.put(self.root_path, json=data)
    
    def DELETE(self):
        SESS.delete(self.root_path)

class TABLE(req):
    def __init__(self) -> None:
        super().__init__(f"http://localhost:{port}/database/{db}/{tb}")

class DATABASE(req):
    def __init__(self) -> None:
        super().__init__(f"http://localhost:{port}/database/{db}")

class USER(req):
    def __init__(self, id:int|None=None) -> None:
        super().__init__(f"http://localhost:{port}/users/{id}")

class SET(req):
    def __init__(self, var) -> None:
        super().__init__(f"http://localhost:{port}/sys/{var}")

class SYS(req):
    def __init__(self) -> None:
        super().__init__(f"http://localhost:{port}/sys/exec")

class USE:
    #TODO: ADD checks
    def database(self, name):
        global db
        db=name

    def table(self, name):
        global tb
        tb=name

def prompt():
    if tb and db:
        return f"bdb/{db}/{tb}>"
    if db:
        return f"bdb/{db}>"
    else:
        return f"bdb>"

while True:
    command=input(prompt())
    for key in keywords:
        if key in command:
            command=command.split(" ")
            if key=="USE":
                exec(f"USE().{command[1]}(\"{command[2]}\")")
                print(db, tb)
            if key=="SET":
                r=...
                exec(f"SET(\"{command[1]}\").GET(\"{command[2]}\", 'value')")
            if key=="SYS":
                exec(f"SYS().GET(\"{" ".join(command[1:])}\")")
            #TODO: ADD Table wrapper for api
        else:
            exec(command)
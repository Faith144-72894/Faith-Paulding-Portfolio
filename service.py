import importlib.util,json,sqlite3
from pathlib import Path
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
ROOT=Path(__file__).resolve().parent
ROLES=["AI-Technical-Program-Manager","Principal-AI-Solution-Architect","Director-AI-Digital-Transformation","Principal-Technical-Program-Manager","Enterprise-AI-Architect","Director-Business-Intelligence","Director-Enterprise-Applications","Director-Technology-Programs"]
def evaluate(role,payload):
    if role not in ROLES or not isinstance(payload,dict): raise ValueError('Invalid request')
    spec=importlib.util.spec_from_file_location('engine',ROOT/'Role_Specific_Portfolio'/role/'flagship'/'app.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod.evaluate(payload)
def record(role,payload,result,path=None):
    db=sqlite3.connect(path or ROOT/'portfolio-local.sqlite3')
    try:
        with db:
            db.execute('create table if not exists runs(id integer primary key, role text, request text, result text, created_at text default current_timestamp)')
            db.execute('insert into runs(role,request,result) values(?,?,?)',(role,json.dumps(payload),json.dumps(result,allow_nan=False)))
    finally: db.close()
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs): super().__init__(*args,directory=str(ROOT/'docs'),**kwargs)
    def do_POST(self):
        status=200
        try:
            if not self.path.startswith('/api/'): raise ValueError('Unknown endpoint')
            if self.headers.get_content_type()!='application/json': raise ValueError('JSON required')
            size=int(self.headers.get('Content-Length','0'))
            if not 0<size<=65536: raise ValueError('Invalid request size')
            role=self.path[5:];payload=json.loads(self.rfile.read(size));result=evaluate(role,payload)
            body=json.dumps({'result':result},allow_nan=False);record(role,payload,result)
        except (ValueError,TypeError,KeyError,AttributeError,OverflowError,RecursionError):
            status=400;body=json.dumps({'error':'Invalid request or inputs'})
        except Exception:
            status=500;body=json.dumps({'error':'Service error'})
        self.send_response(status);self.send_header('Content-Type','application/json');self.end_headers();self.wfile.write(body.encode())
if __name__=='__main__':
    ThreadingHTTPServer(('127.0.0.1',8765),Handler).serve_forever()

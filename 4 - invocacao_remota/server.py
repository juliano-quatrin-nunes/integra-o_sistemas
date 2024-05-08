from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2')

with SimpleXMLRPCServer(('localhost', 8005), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def adder_function(x, y):
        print(x+y)
        return x+y
    
    def subtractor_function(x, y):
        print(x-y)
        return x-y
    
    def multiplier_function(x, y):
        print(x*y)
        return x*y
    
    def divider_function(x, y):
        print(x/y)
        return x/y
    
    def power_function(x, y):
        print(x**y)
        return x**y
    
    server.register_function(adder_function, 'add')
    server.register_function(subtractor_function, 'sub')
    server.register_function(multiplier_function, 'mult')
    server.register_function(divider_function, 'div')
    server.register_function(adder_function, 'pwr')

    server.serve_forever()
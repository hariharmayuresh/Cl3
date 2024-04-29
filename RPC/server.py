'''Design a distributed application using RPC for remote computation where client submits an 
integer value to the server and server calculates factorial and returns the result to the client 
program '''

from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(factorial, "factorial")
server.serve_forever()

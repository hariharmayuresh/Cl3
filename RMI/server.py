import Pyro4

# Define the class that will be accessed remotely
@Pyro4.expose
class StringConcatenator:
    def concatenate_strings(self, str1, str2):
        return str1 + str2

# Create a Pyro4 daemon and register the remote object
daemon = Pyro4.Daemon()
uri = daemon.register(StringConcatenator)

print("Server URI:", uri)

# Start the Pyro4 event loop
daemon.requestLoop()
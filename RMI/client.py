import Pyro4

# Get the URI of the remote object from the server
uri = input("Enter the server URI: ")

# Create a proxy for the remote object
string_concatenator = Pyro4.Proxy(uri)

# Get input strings from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Call the remote method to concatenate the strings
result = string_concatenator.concatenate_strings(str1, str2)

print("Concatenated string:", result)
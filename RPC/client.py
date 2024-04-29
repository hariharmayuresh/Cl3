import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
num = int(input("Enter a number to calculate factorial: "))
result = proxy.factorial(num)
print(f"Factorial of {num} is {result}")
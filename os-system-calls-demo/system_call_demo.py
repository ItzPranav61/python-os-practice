import os

print("Current Process ID:", os.getpid())
print("Current Working Directory:", os.getcwd())

filename= "pranav_test.txt"

with open(filename, "w") as file:
    file.write("Hello, I'm Pranav")

with open(filename, "r") as file:
    content=file.read()

print("File Exists:", os.path.exists(filename))
print("File Content:", content)
print("File Size:", os.path.getsize(filename), "bytes")
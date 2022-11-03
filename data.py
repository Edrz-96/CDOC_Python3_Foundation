import sys

# Useful data
# 'r' open existing file for read (default)
# 'w' open file for write, create or overwrite existing file
# 'a' open file for append, create if does not exist
# 'x' create file and open for write, fails if file exists (3.3)
# 'r+' open existing file for read/write
# 'w+' create & truncate file for read/write
# 'a+' create & append file for read/write

f = open("drop/Errors.txt", "r+")

print("split", f.read().splitlines())  # splits the whole file in a list
print("readlines", f.readlines())  # produces a list but remains a new char
print("read", f.read())  # reads the whole file as one string
# Read can return read(nth) lines

# Most pythonic way
with open("file.txt", "r") as f:
    for line in f:
        print(line)

# Flush
# What does it mean to flush a file?
# Typically this means that the data will be copied from the program buffer to the operating system buffer

# Safer way to open files
with open("drop/Errors.txt") as new_f:
    for i in new_f:
        print(i)

# Write to a file
append = open("drop/Errors.txt", "a")
write = open("drop/Errors.txt", "w")
append.write("check ")
append.writelines(["val", "val", "val"])

# Print to file
print("New line in file", file=write)

# Binary file mode
binary = open("drop/binary.txt", "w+")

print("Random data", file=binary)

for line in open("drop/binary.txt", "rb"):
    # If you recall, the same b is being used as when we have bytes/bytearray vars
    print(line.decode(), end="")

dat = open('drop/out.dat', 'wb')
# Equally, we can encode or write bytes to a file like below
nb = dat.write(b'Single bytes string ')
s = "Native string as a line\r\n"
nb = dat.write(s.encode())

# stdin,out and err
import sys

sys.stdout.write("Please enter a value: ")
sys.stdout.flush()
reply = sys.stdin.readline()
sys.stdout.write("Please enter a value: ")
safe_reply = sys.stdin.readline().strip()
print(f"Input was {reply} and {safe_reply}")

# File navigation
f = open("drop/binary.txt", "rb")
# Binary file access produces better offset
i = {}
key = input("input val")
while True:
    # Get
    l = f.readline()
    if not l: break
    field = l.decode()
    # Set dict with decoded field entries
    i[field[0]] = f.tell() - len(l)
    # Ask user for query
print(i)
# Navigate to location
# f.seek(i[key])
print(f.readline().decode(), end="")

# Simple example
# Opening text file
f = open("drop/Errors.txt", "r")

f.seek()

# prints current position
print(f.tell())

print(f.readline().splitlines())
f.close()

# Pickling
# 1) saving a program's state data to disk so that it can carry on where it left off when restarted (persistence)
#
# 2) sending python data over a TCP connection in a multi-core or distributed system (marshalling)
# Assuming safe to do so

# Small example
import pickle

# Convention is to use *.pickle for your pickles
new_obj = {"n": "val", "i": "val"}
# Creating new pickle file in drop
with open('drop/pickle-file.pickle', 'wb') as f:
    pickle.dump(new_obj, f)
# Del file to prove data is store on hdd
del new_obj
# Ensure correct file type
with open('drop/pickle-file.pickle', 'rb') as f:
    stored_obj = pickle.load(f)
# print stored file
print(stored_obj)

#section 1
is_online=True
has_access=False
print(is_online and has_access)
#section 2
print(is_online or has_access)
#section 3
status = False
print(not status)
#section 4
age = 20 
has_id = True
print(age and has_id)
#section 5
level = 3
print(level>1 and level<5)
#section 6
a = 0
b = "hello"
c = ""
print (bool(a))
print (bool(b))
print (bool(c))
#section 7
x = None 
y = 42
print(x or y)
# the value of y is retured becous y is the true wan
#section 8
username = "" 
default = "guest"
final_username=default or username
print(final_username)
#section 9
print(True and False or True)
print(True and False or True)
print("first and result false then or with true or false")
#section 1
door_locked = True
has_key = False
admin_override = True
print(admin_override or has_key and door_locked)
#section 2
message = "" 
backup_message = "No message found"
print(message or backup_message)
#section 3
x = None
print(x is None)
#befuor using a value chek if it exists
#section 4
a = 0
b = "ready"
c = 42
print(a or b or c)
#the or is giving the first value thats true
#section 5
score = 85
print ("pass") if score>=60 else print("fail")
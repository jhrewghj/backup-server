import hashlib
def hashedinfo(username, password):
	content = username
	hash_object = hashlib.sha256(content.encode('utf-8'))
	hex_dig = hash_object.hexdigest()
	hash_object1 = hashlib.md5(hex_dig.encode('utf-8'))
	hex_dig1 = hash_object1.hexdigest()
	content1 = password
	hash_object2 = hashlib.sha256(content1.encode('utf-8'))
	hex_dig2 = hash_object2.hexdigest()
	hash_object3 = hashlib.md5(hex_dig2.encode('utf-8'))
	hex_dig3 = hash_object3.hexdigest()
	final = f"Hashed version of username: {hex_dig1}\nHashed version of password: {hex_dig3}"
	return [hex_dig1,hex_dig3]

#DO NOT REMOVE 

# def ha(thing):
# 	content = thing
# 	hash_object = hashlib.sha256(content.encode('utf-8'))
# 	hex_dig = hash_object.hexdigest()
# 	print(f"Hashed version: {hex_dig}")
	

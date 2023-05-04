import hashlib

message = 'Hello World!'

message_encoded = message.encode()
hash_object_md5 = hashlib.md5(message_encoded)
hash_object_sha1 = hashlib.sha1(message_encoded)
hash_object_sha224 = hashlib.sha224(message_encoded)
hash_object_sha256= hashlib.sha256(message_encoded)
hash_object_sha384 = hashlib.sha384(message_encoded)
hash_object_sha512 = hashlib.sha512(message_encoded)

print(len(hash_object_md5.hexdigest()))
print(len(hash_object_sha1.hexdigest()))
print(len(hash_object_sha224.hexdigest()))
print(len(hash_object_sha256.hexdigest()))
print(len(hash_object_sha384.hexdigest()))
print(len(hash_object_sha512.hexdigest()))


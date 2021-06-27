#FriendFace Post
post = {"user_id": 200, "Message": "Welcome Home","Language":"English"}
print(post)

post2 = dict(Message = "Welcome2", language = "English")

post2["UserName"] = "Albert"
post2["Surname"] = "Ealbert"

#access library

#handling Error in Dict

if 'Location' in post2:
    print(post2['Location'])
else:
    print("The post does not contain a location value")

try:
    print(post2['Location'])
except KeyError:
    print("Location does not exist")

loc = post2.get("Location",None)
print(loc)

#looping through Dictionary
for key in post.keys():
    value = post[key]
    print(key, "=", value)

#Second looping of dict
for key, value in post.items():
    print(key, "=", value)
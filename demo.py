import json
# inbuilt mehtods
# dump(),dumps()
# python data----->json.dumps()
# dump used to convert binary data  to json data

# load(),loads()
# json data----->json.loads()------->python data
# load- used to convert binary data to python data 
p_data={'name':'Pradhyumn','age':20}
j_data=json.dumps(p_data)
print(j_data)
print(type(j_data))


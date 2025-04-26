band = dict(vocals= "Music" , Guitar="Instrument")
# print(band)
# print(type(band))
# print(len(band))

# Access items
# print(band["vocals"])
# print(band.get("Guitar"))

# List all keys and values
# print(band.keys())
# print(band.values())

# list all values in tuples
# print(band.items())

# verifying a key exists
# print("Guitar" in band)
# print("vocals" in band)
# print("angles" in band)

# For changing values
# band["vocals"] = "Saregamapa"
# print(band)
# Band pop item remove the item just updated or added before
# print(band.popitem())

#  For adding a new pair in a dictionary
band.update({"Mango": "Fruit"})
print(band)

# For removing items
# print(band.pop("Guitar")) 
# print(band)

# delete and clear 
del band["Guitar"]
print(band)

band2 =dict(Laptop = "electronic" , earbuds = "headphones" )
print(band2)
# band2.clear()
# print(band2)
# del band2
# print(band2)

# Copy dictionaries
# band2 = band
# print(band)
# print("Bad Copy!")
# print(band2)
# print(band)

# band2["Laptop"] = "Dave"
# print(band)

# band2 = band.copy()
# band2 ["Laptop"] = "Dave"
# print(band2)
# print(band)
# print("This is what actual copying dictionaries mean!!!")

# or use the dict() constructor function
# band3 = dict(band)
# print("This will also work")
# print(band3)
# band.update({"Mouse" : "Fuss"})
# print(band)
# print(band3)

# Nested dictionaries: A dictionary can contain dictionaries,
#  this is called nested dictionaries.
 
# member1 = {
#       "name": "Ash",
#       "Last": "Rai" 
#     #   comma , is very important here 
#  }
# member2 = {
#       "name": "Utk",
#       "Last": "Gur" 
#  }
# band = {
#    "member1" : member1,
#    "member2" : member2,
# }
# print(band)
# print(band["member1"]["name"])
# print(band["member2"]["name"])

# Sets

nums1 =  {1,2,3,4}
nums2 = set ((1,2,3,4))
print(type(nums2))
print(len(nums2))

# No duplicate allowed
nums1 = {1,2,2,3}
print(nums1)

# True is a dupe of 1 , False is a dupe of 0 
nums1 = {1,True,2,False,3,4,0}
print(nums1)

# check if a value is there in a set
print(2 in nums2)

# but you cannot refer to an elemet in the set with an index position or a key 

#  adding a new element to a set 
nums1.add(8)
print(nums1)
morenums = (7,6,9,99)
nums1.update(morenums)
print(nums1)

# Merge two sets to create a new set by using union
yes = {1,2,3,4}
no = {5,4,2,3,7,8}
yes.intersection_update(no)
print(yes)

# newset = yes.union(no)
# print(newset)

# when taking comom or keeping duplicates use intersection

# newset = yes.intersection(no)

# print(newset)

#  keeping everthhing except the duplicates

yes.symmetric_difference_update(no)
print(yes)
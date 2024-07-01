# `Pickling` converts Python objects to byte streams, known as serialization.
# `Unpickling` is the reverse, converting byte streams back to Python objects, known as deserialization.
# In Python, we use `pickle.dump` and `pickle.load` for serialization and deserialization.

import pickle
data= {
    "names":["aman", "prem", "lary"],
    "id":[1, 2,4 ]
}
output = open("./data.pkl", "wb")
pickle.dump(data, output)
output.close()
# unpickling
stream =open("./data.pkl", 'rb')
data= pickle.load(stream)
print(data)
stream.close()

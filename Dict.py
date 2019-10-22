import pickle

database = pickle.load(open('userData/database.p', 'rb'))
print(database)

pickle.dump(database, open('userData/database.p', 'wb'))

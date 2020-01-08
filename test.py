from QL_Agent import *

filename = "test.pkl"

a = QLearning(filename)
a.QValueTable = generate_QValueTable_of_NaiveRLstate()


a.save()




with open(filename, 'rb') as file:
    T = pickle.loads(file.read())

print(T.QValueTable)
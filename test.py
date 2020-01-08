from QL_Agent import *

filename = "T1"
QL = None
with open(filename+".pkl", 'rb') as file:
    QL = pickle.loads(file.read())

print(QL.Description)

# comments = "5x5 map LR=0.9 D=0.8 T=200\n\
# Reward: eatFoodReward = 100  deathReward = -500  getCloserReward = 0  getFurtherReward = 0\n"

# if QL.Description == None:
#     QL.Description = comments
# else:
#     QL.Description += comments

# QL.save()
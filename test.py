from QL_Agent import *

filename = "T2"
QL = None
with open(filename+".pkl", 'rb') as file:
    QL = pickle.loads(file.read())




# # QL.Epsilon = 1.0
# # QL.name = "T2"

# comments = "Epsilon was reset 20x20 map LR=0.5 D=0.9 T=250\n\
# Reward: eatFoodReward = 500  deathReward = -500  getCloserReward = 100  getFurtherReward = -50\n"

# if QL.Description == None:
#     QL.Description = comments
# else:
#     QL.Description += comments

# QL.save()


# print(QL.Description)


# Step 1. Importing Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random


# Step 2.  Importing the dataset Files..
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')


# Step 3.  Thompson Sampling Algorithm
N = 10000
d= 10
ads_selected = []
no_of_rewards_1 = [0]*d
no_of_rewards_0 = [0]*d
total_reward = 0

for n in range(N):
    ad = 0
    max_random = 0
    for i in range(d):
        random_beta = random.betavariate(no_of_rewards_1[i]+1,no_of_rewards_0[i]+1)
        if random_beta>max_random:
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    if(reward == 1):
        no_of_rewards_1[ad]+=1
    else:
        no_of_rewards_0[ad]+=1
    total_reward = total_reward + reward
    

for i in range(len(ads_selected)-9599):
    print("User",i,"Selectd Ad no ",ads_selected[i])
print('These are about 400 entries');
print("Note: Must see the corpus Variable. It is a list variable can't be seen fully on dashboard as it contains about 10000(10K) Entries")    
    
    
print('Total no of rewards',total_reward)   
# Step 4.  Visualizing the Results
plt.hist(ads_selected)
plt.title('Histogram of Ads Selections')
plt.xlabel('Ads')
plt.ylabel('No of time each  Ad selected')
plt.show();
        
        
        
    
                                                                              
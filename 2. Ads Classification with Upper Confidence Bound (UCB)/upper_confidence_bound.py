

# Step 1. Importing Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# Step 2.  Importing the dataset Files..
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Step 3.  Upper Confidence Bound(UCB) Algorithm

# (i) of the Algo
N = 10000# no of Users in the dataset
d = 10 # No of Ads in the dataset
no_of_selections = [0]*d
sum_of_rewards  = [0]*d
ads_selected = []
total_reward = 0
#  (ii) of the Algo
for n in range(0,N):
    ad = 0;
    max_upper_bound = 0;
    for i in range(0,d):
        if(no_of_selections[i] >0):
            avg_reward = sum_of_rewards[i]/no_of_selections[i]# Computer r_i^(n) = r_i(n)/n_i(n)
            # COmputing Delta[i]
            delta_i = math.sqrt(3/2* math.log(n+1)/no_of_selections[i]) 
            upper_bound = delta_i+ avg_reward
        else:
            upper_bound = 10e400
#  (iii) of the Algo
        if(upper_bound > max_upper_bound):
            max_upper_bound = upper_bound
            ad  = i
    ads_selected.append(ad)
    no_of_selections[ad]+=1
    reward = dataset.values[n,ad]
    sum_of_rewards[ad]+=reward
    total_reward+= reward
    
for i in range(len(ads_selected)-9599):
    print("User",i,"Selectd Ad no ",ads_selected[i])
print('These are about 400 entries');
print("Note: Must see the corpus Variable. It is a list variable can't be seen fully on dashboard as it contains about 10000(10K) Entries")    
    
    
print('Total no of rewards',total_reward)   
    
# Step 4.  Visualizing the Results
plt.hist(ads_selected)
plt.title('Histogram of Ads Selection')
plt.xlabel('Ads')
plt.ylabel('No of times each Ad was selected')
plt.show()

    
 
            
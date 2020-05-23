

# Step 1. Importing Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

# Step 2.  Importing the dataset Files..
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')


# Step 3.  Random Selection Algorithm
N = 10000
d = 10
ads_selected = []
total_reward = 0
for n in range(N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    total_reward += reward
for i in range(len(ads_selected)-9599):
    print("User",i,"Selectd Ad no ",ads_selected[i])
print('These are about 400 entries');
print("Note: Must see the corpus Variable. It is a list variable can't be seen fully on dashboard as it contains about 10000(10K) Entries")    
    
   
print('Total no of rewards',total_reward)      
# Step 4.  Visualizing the Results
plt.hist(ads_selected)
plt.title('Histogram of Ads Selection')
plt.xlabel('Ads')
plt.ylabel('No of times each Ad was Selected')
plt.show()
        

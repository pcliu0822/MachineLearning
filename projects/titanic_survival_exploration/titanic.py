import pandas as pd
import numpy as np
from IPython.display import display
from matplotlib import pyplot as plt

fulldata = pd.read_csv("titanic_data.csv")
#print(fulldata.head())

#see all column names
colnames = fulldata.columns
#create y data
outcome = fulldata['Survived']
#create x data
data = fulldata.drop('Survived',axis = 1)

#create accuracy function
def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """
    
    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred): 
        
        # Calculate and return the accuracy as a percent
        return "accuracy_score for Question 1 is %.2f" % ((truth == pred).mean()*100)
    
    else:
        return "Number of predictions does not match number of outcomes!"
	
# Test the 'accuracy_score' function
predictions = pd.Series(np.ones(5, dtype = int))
print(accuracy_score(outcome[:5],predictions))

#Question1: predict all as not survivied
prediction1 = np.zeros(len(outcome))
print(accuracy_score(outcome,prediction1))

#Question2: predict based on sex
sexLabel = print(data['Sex'].unique())
femaleSum = outcome[data['Sex']=='female'].mean()
maleSum = outcome[data['Sex']=='male'].mean()


prediction2 = data['Sex'].map({'male':0,'female':1})
print(accuracy_score(outcome,prediction2))

#Question3: predict based on age and sex
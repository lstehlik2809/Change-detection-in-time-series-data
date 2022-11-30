# -*- coding: utf-8 -*-
"""
Change detection in time series data
Created on Tue Sep  6 12:42:21 2022
@author: Ludek Stehlik

"""
# library for computing means and standard deviations
import numpy as np

# example of 13 months long time series of three collaboration metrics (number of meetings, sent emails, and sent instant messages)
ts={"cntMeetings": [1.8, 1.3, 1.6, 1.5, 1.6, 1.6, 1.2, 1.7, 1.4, 1.4, 3, 1.5, 1.4],
    "cntSentEmails": [2.4, 1.8, 2.1, 2, 4.1, 4.3, 3.2, 3.3, 2.1, 2, 3.6, 1.9, 1.5],
    "cntSentChat": [25.1, 17.5, 19.2, 16.7, 18.9, 15.7, 12.4, 18.6, 17.2, 17.9, 36.6, 18.3, 12.8]
   } 

# function for computing standardized change of metrics during the last three months 
def myFunction(tsDict):

    outputDict={}
    
    for metric in tsDict:
        
        # computing raw differences between values from consecutive months
        differences=[]
        counter=0
        for value in range(0, len(tsDict[metric])):
            if counter<len(tsDict[metric])-1:
                diff=(tsDict[metric][value+1]-tsDict[metric][value])
                differences.append(diff)
            else:
                break
            counter+=1
        
        # computing mean, standard deviation, and z-scores
        avg=np.mean(differences)
        sd=np.std(differences)
        standardizedDiff=(differences-avg)/sd
        
        # computing average standardized change across the last 3 months
        lastThreeMonthsAvgStandDiff=np.mean(standardizedDiff[-3:])
        
        outputDict.update({metric: lastThreeMonthsAvgStandDiff})
        
    return outputDict


# computing standardized change of three example metrics in the last three months
output = myFunction(ts)
print(output)

# ordering metrics in descending order by the absolute value of average size of their respective change during the last 3 months
print(sorted([(np.abs(value),key) for (key,value) in output.items()], reverse=True))

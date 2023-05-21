#!/usr/bin/env python
# coding: utf-8

# ## Task_1_Prediction_using_Supervised ML

# ### Simple Linear Regression
# In this regression task we will predict the percentage of marks that a student is expected to score based upon the number of hours they studied. This is a simple linear regression task as it involves just two variables.
# 
# 

# In[34]:


# Importing all libraries required in this notebook

import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
get_ipython().run_line_magic('matplotlib', 'inline')


# In[39]:


# Reading data from remote link
score = pd.read_csv('https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv')
score.head(10)


# In[41]:


'''Let's plot our data points on 2-D graph to eyeball our dataset and see if we can manually find any relationship between 
the data. We can create the plot with the following script:'''

# Plotting the distribution of scores

score.plot(x='Hours', y='Scores', style='*')  
plt.title('Hours vs Percentage')  
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score')  
plt.show()


# In[11]:


'''From the graph above, we can clearly see that there is a positive linear relation between the number of hours studied 
and percentage of score.'''

#Preparing the data

#The next step is to divide the data into "attributes" (inputs) and "labels" (outputs).'

X = data.iloc[:, :-1].values  
y = data.iloc[:, 1].values  


# In[12]:


'''Now that we have our attributes and labels, the next step is to split this data into training and test sets.
We'll do this by using Scikit-Learn's built-in train_test_split() method:'''

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                            test_size=0.2, random_state=0) 


# In[13]:


'''Training the Algorithm
We have split our data into training and testing sets, and now is finally the time to train our algorithm. '''

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train) 

print("Training complete.")


# In[45]:


# Plotting the regression line
e_line = regressor.coef_*X+regressor.intercept_

# Plotting for the test data
plt.scatter(X, y)
plt.plot(X, line);
plt.show()


# In[15]:


#Making Predictions
#Now that we have trained our algorithm, it's time to make some predictions.

print(X_test) # Testing data - In Hours
y_pred = regressor.predict(X_test) # Predicting the scores


# In[16]:


# Comparing Actual vs Predicted
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
df 


# In[17]:


# You can also test with your own data
hours = np.array(9.25).reshape(-1, 1)
own_pred = regressor.predict(hours)
print("No of Hours = {}".format(hours))
print("Predicted Score = {}".format(own_pred[0]))


# In[18]:


#Evaluating the model

'''The final step is to evaluate the performance of algorithm. This step is particularly important to compare how well different
algorithms perform on a particular dataset. For simplicity here, we have chosen the mean square error. There are many such 
metrics.'''

from sklearn import metrics  
print('Mean Absolute Error:', 
      metrics.mean_absolute_error(y_test, y_pred)) 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





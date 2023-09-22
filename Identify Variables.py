#!/usr/bin/env python
# coding: utf-8

# # **Automatidata project**
# **Identify variables and get dataset ready for analysis**

# Welcome to the Automatidata Project!
# 
# New York City Taxi and Limousine Commission (New York City TLC), has hired the Automatidata team for its reputation in helping their clients develop data-based solutions.
# 
# The team is still in the early stages of the project. To get clear insights, New York TLC's data must be analyzed, key variables identified, and the dataset ensured it is ready for analysis.
# 

# # Inspect and analyze data
# 
# Examine data provided and prepare it for analysis. This will help ensure the information is:
# 
# 1.   Ready for visualizations
# 
# 2.   Ready for future hypothesis testing and statistical methods
# <br/>    
# 
# **The purpose** of this project is to investigate and understand the data provided.
#   
# **The goal** is to use a dataframe contructed within Python, perform a cursory inspection of the provided dataset.
# <br/>  
# *This activity has three parts:*
# 
# **Part 1:** Understand the situation 
# * Prepare to understand and organize the provided taxi cab dataset and information.
# 
# **Part 2:** Understand the data
# 
# * Create a pandas dataframe for data learning, future exploratory data analysis (EDA), and statistical activities.
# 
# * Compile summary information about the data to inform next steps.
# 
# **Part 3:** Understand the variables
# 
# * Use insights from your examination of the summary data to guide deeper investigation into specific variables.
# 
# 
# <br/> 

# # **Identify data types and relevant variables using Python**
# 

# <img src="images/Pace.png" width="100" height="100" align=left>
# 
# # **PACE stages**
# 

# Throughout these project notebooks, you'll see references to the problem-solving framework PACE. The following notebook components are labeled with the respective PACE stage: Plan, Analyze, Construct, and Execute.

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## PACE: **Plan**
# 

# ### **Task 1. Understand the situation**
# 
# *   How can you best prepare to understand and organize the provided taxi cab information? 

# By exploring data and looking at the columns and understand how they are related

# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## PACE: **Analyze**
# 

# ### **Task 2a. Build dataframe**
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# Create a pandas dataframe for data learning, and future exploratory data analysis (EDA) and statistical activities.
# 
# **Code the following,**
# 
# *   import pandas as `pd`. pandas is used for buidling dataframes.
# 
# *   import numpy as `np`. numpy is imported with pandas
# 
# *   `df = pd.read_csv('Datasets\NYC taxi data.csv')`
# 
# **Note:** pair the data object name `df` with pandas functions to manipulate data, such as `df.groupby()`.
# 
# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[3]:


#Import libraries and packages listed above
import pandas as pd
import numpy as np

# Load dataset into dataframe
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')
print("done")


# ### **Task 2b. Understand the data - Inspect the data**
# 
# View and inspect summary information about the dataframe by coding the following:
# 
# 1. `df.head(10)`
# 2. `df.info()`
# 3. `df.describe()`
# 
# Consider the following two questions:
# 
# **Question 1:** When reviewing the `df.info()` output, what do you notice about the different variables? Are there any null values? Are all of the variables numeric? Does anything else stand out?
# 

# ==> ENTER YOUR RESPONSE TO QUESTIONS 1 HERE
# no null values are there, there are different data tyoes (object, int, float), noticed a column name "unnamed" which has no meaning and the title doesn't carry any valuable information

# In[3]:


#==> ENTER YOUR CODE HERE 
df.head(10)


# In[2]:


#==> ENTER YOUR CODE HERE
df.info()


# In[4]:


#==> ENTER YOUR CODE HERE
df.describe()


# ### **Task 2c. Understand the data - Investigate the variables**
# 
# Sort and interpret the data table for two variables:`trip_distance` and `total_amount`.
# 
# **Answer the following three questions:**
# 
# **Question 1:** Sort your first variable (`trip_distance`) from maximum to minimum value, do the values seem normal?
# 
# **Question 2:** Sort by your second variable (`total_amount`), are any values unusual?
# 

# for trip_distance, the min is 0 miles and yet there is charge for these trips.
# noticed negative amounts for total_amount.
# 

# In[10]:


# ==> ENTER YOUR CODE HERE
df_sort=df.sort_values(by=['trip_distance'], ascending= False)

# Sort the data by trip distance from maximum to minimum value

df_sort.head(10)
df_sort.tail(10)


# In[11]:


#==> ENTER YOUR CODE HERE
df_sort=df.sort_values(by=['total_amount'], ascending= False)

# Sort the data by total amount and print the top 20 values
df_sort.head(20)


# In[12]:


#==> ENTER YOUR CODE HERE

# Sort the data by total amount and print the bottom 20 values
df_sort.tail(20)


# In[4]:


#==> ENTER YOUR CODE HERE
df['payment_type'].value_counts()
# How many of each payment type are represented in the data?


# According to the data dictionary, the payment method was encoded as follows:
# 
# 1 = Credit card  
# 2 = Cash  
# 3 = No charge  
# 4 = Dispute  
# 5 = Unknown  
# 6 = Voided trip

# In[15]:



# What is the average tip for trips paid for with credit card?

#==> ENTER YOUR CODE HERE

credit_trips = df[df['payment_type'] == 1]
avg_tip_credit = credit_trips['tip_amount'].mean()
print(avg_tip_credit)

# What is the average tip for trips paid for with cash?

#==> ENTER YOUR CODE HERE

cash_trips = df[df['payment_type'] == 2]
avg_tip_cash = cash_trips['tip_amount'].mean()
print(avg_tip_cash)


# In[26]:


#==> ENTER YOUR CODE HERE

# How many times is each vendor ID represented in the data?

vendorID_counts = df['VendorID'].value_counts()
print(vendorID_counts)


# In[35]:


#==> ENTER YOUR CODE HERE

# What is the mean total amount for each vendor?

mean_total_vendor=df['total_amount'].groupby(df['VendorID']).mean()
print(mean_total_vendor)


# In[51]:


#==> ENTER YOUR CODE HERE

# Filter the data for credit card payments only

credit_data = df[df['payment_type']==1]
print(credit_data)

#==> ENTER YOUR CODE HERE

# Filter the data for passenger count only (ex: passenger_count>1)

passenger_count_data = df[df['passenger_count']>1]
print(passenger_count_data)


# In[49]:


#==> ENTER YOUR CODE HERE

# Calculate the average tip amount for each passenger count (credit card payments only)

credit_tip_passenger=credit_trips.groupby('passenger_count')['tip_amount'].mean()
print(credit_tip_passenger)


# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## PACE: **Construct**
# 
# **Note**: The Construct stage does not apply to this workflow. The PACE framework can be adapted to fit the specific requirements of any project. 
# 
# 
# 

# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## PACE: **Execute**
# 
# 
# 

# ### **What can you summarize for the data team?**
# 
# *Which two variables are most helpful for building a predictive model for the client: NYC TLC?*

# total_amount and trip_distance would be the most helpful variables for building a predective model for this client

# 

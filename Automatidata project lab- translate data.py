#!/usr/bin/env python
# coding: utf-8

# # ** Automatidata project**
# **Translate Data into Insights**

# You are the newest data professional in a fictional data consulting firm: Automatidata. The team is still early into the project, having only just completed an initial plan of action and some early Python coding work. 
# 
# The senior data analyst at Automatidata, is pleased with the work you have already completed and requests your assistance with some EDA and data visualization work for the New York City Taxi and Limousine Commission project (New York City TLC) to get a general understanding of what taxi ridership looks like. The management team is asking for a Python notebook showing data structuring and cleaning, as well as any matplotlib/seaborn visualizations plotted to help understand the data. At the very least, include a box plot of the ride durations and some time series plots, like a breakdown by quarter or month. 
# 
# Additionally, the management team has recently asked all EDA to include Tableau visualizations. For this taxi data, create a Tableau dashboard showing a New York City map of taxi/limo trips by month. Make sure it is easy to understand to someone who isn’t data savvy, and remember that the assistant director at the New York City TLC is a person with visual impairments.

# # Exploratory data analysis
# 
# **The purpose** of this project is to conduct exploratory data analysis on a provided data set. The mission is to continue the investigation began in C2 and perform further EDA on this data. 
#   
# **The goal** is to clean data set and create a visualization.
# <br/>  
# *This portion of the project has 4 parts:*
# 
# **Part 1:** Imports, links, and loading
# 
# **Part 2:** Data Exploration
# *   Data cleaning
# 
# 
# **Part 3:** Building visualizations
# 
# **Part 4:** Evaluate and share results
# 
# 

# # **Visualize a story in Tableau and Python**

# # **PACE stages** 
# 
# 
# <img src="images/Pace.png" width="100" height="100" align=left>
# 
#    *        [Plan](#scrollTo=psz51YkZVwtN&line=3&uniqifier=1)
#    *        [Analyze](#scrollTo=mA7Mz_SnI8km&line=4&uniqifier=1)
#    *        [Construct](#scrollTo=Lca9c8XON8lc&line=2&uniqifier=1)
#    *        [Execute](#scrollTo=401PgchTPr4E&line=2&uniqifier=1)

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## PACE: Plan 
# 
# 
# 

# ### Task 1. Imports, links, and loading

# In[2]:


# Import packages and libraries
#==> ENTER YOUR CODE HERE
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# Load dataset into dataframe
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')


# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## PACE: Analyze 
# 

# ### Task 2a. Data exploration and cleaning
# 

# Start by discovering, using head and size. 

# In[4]:


#==> ENTER YOUR CODE HERE
df.head(10)


# In[6]:


#==> ENTER YOUR CODE HERE
df.shape


# Use describe... 

# In[7]:


#==> ENTER YOUR CODE HERE
df.describe()


# And info. 

# In[8]:


#==> ENTER YOUR CODE HERE
df.info()


# ### Task 2b. Select visualization type(s)

# Select data visualization types that will help you understand and explain the data.
# 
# * Line graph
# * Bar chart
# * Box plot
# * Histogram
# * Heat map
# * Scatter plot
# * A geographic map
# 

# Considering this dataset, I believe that bar charts, histograms, scatter plots, and heat maps are the most useful. Bar charts and histograms effectively showcase the distribution of categorical variables such as payment types, trip distance, and fare amount. On the other hand, scatter plots and heat maps prove to be especially beneficial for uncovering correlations and patterns among variables like trip distance and tip amount.

# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## PACE: Construct 
# 

# ### Task 3. Data visualization
# 

# ### Boxplots

# Perform a check for outliers on relevant columns such as trip distance and trip duration.

# In[9]:


# Convert data columns to datetime
#==> ENTER YOUR CODE HERE

df['tpep_pickup_datetime']=pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime']=pd.to_datetime(df['tpep_dropoff_datetime'])


# **trip distance**

# In[10]:


# Create box plot of trip_distance
#==> ENTER YOUR CODE HERE
sns.boxplot(x="trip_distance", data=df)
plt.xlabel("Trip Distance")
plt.title("Box Plot of Trip Distance")
plt.show()


# In[11]:


# Create histogram of trip_distance
#==> ENTER YOUR CODE HERE
plt.figure(figsize = (10,5))
sns.histplot(df['trip_distance'], bins = range(0,26,1))
plt.title('Trip Distance Histogram')


# **total amount**

# In[12]:


# Create box plot of total_amount
#==> ENTER YOUR CODE HERE
sns.boxplot(x="total_amount", data=df)
plt.xlabel("Total Amount")
plt.title("Box Plot of Total Amount")
plt.show()


# In[14]:


# Create histogram of total_amount
#==> ENTER YOUR CODE HERE
plt.figure(figsize = (10,5))
sns.histplot(df['total_amount'],bins =range(-20, 120,5))
plt.title('Total Amount Histogram')


# **tip amount**

# In[15]:


# Create box plot of tip_amount
#==> ENTER YOUR CODE HERE
sns.boxplot(x="tip_amount", data=df)
plt.xlabel("Tip Amount")
plt.title("Tip Amount of Total Amount")
plt.show()


# In[16]:


# Create histogram of tip_amount
#==> ENTER YOUR CODE HERE
plt.figure(figsize = (10,5))
ax = sns.histplot(df['tip_amount'], bins = range(-5, 20, 1))
ax.set_xticks(range(0,21,2))
ax.set_xticklabels(range(0,21,2))
plt.title('TIp Amount histogram')


# **tip_amount by vendor**

# In[17]:


# Create histogram of tip_amount by vendor
#==> ENTER YOUR CODE HERE
plt.figure(figsize = (10,5))
ax = sns.histplot(data = df, x = df['tip_amount'], hue = df['VendorID'], bins = range(-5, 20, 1), multiple = 'stack',
            palette = 'pastel')
ax.set_xticks(range(-5, 20, 1))
plt.title('Tip Amount By Vendor')


# Next, zoom in on the upper end of the range of tips to check whether vendor one gets noticeably more of the most generous tips.

# In[18]:


# Create histogram of tip_amount by vendor for tips > $10 
#==> ENTER YOUR CODE HERE
tips_above_10 = df[df['tip_amount'] > 10]  
plt.figure(figsize = (10,5))
ax = sns.histplot(data = tips_above_10, x = 'tip_amount', hue = 'VendorID', multiple = 'stack',
                 bins = range(5, 60, 2), palette = 'pastel')
ax.set_xticks(range(5, 60, 5))
plt.title('Tip Amount more than $10')


# **Mean tips by passenger count**
# 
# Examine the unique values in the `passenger_count` column.

# In[19]:


#==> ENTER YOUR CODE HERE
df['passenger_count'].value_counts()


# In[20]:


# Calculate mean tips by passenger_count
#==> ENTER YOUR CODE HERE
mean_tips_by_passenger_count = df.groupby('passenger_count').mean()[['tip_amount']]
mean_tips_by_passenger_count


# In[22]:


# Create bar plot for mean tips by passenger count
#==> ENTER YOUR CODE HERE
data = mean_tips_by_passenger_count.tail(6)
plt.figure(figsize = (12,7))
ax = sns.barplot(data = data, x = data.index, y = 'tip_amount', palette = 'pastel')
ax.axhline(df['tip_amount'].mean(), ls = '--', color = 'red', label = 'Global Mean')
ax.legend()
plt.title('Mean tip amount by passenger count', fontsize=16);


# **Create month and day columns**

# In[23]:


# Create a month column
#==> ENTER YOUR CODE HERE
df['month'] = df['tpep_pickup_datetime'].dt.month_name()

# Create a day column
df['day'] = df['tpep_pickup_datetime'].dt.day_name()


# **Plot total ride count by month**
# 
# Begin by calculating total ride count by month.

# In[24]:


# Get total number of rides for each month
#==> ENTER YOUR CODE HERE
monthly_rides = df['month'].value_counts()


# Reorder the results to put the months in calendar order.

# In[25]:


# Reorder the monthly ride list so months go in order
#==> ENTER YOUR CODE HERE
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
monthly_rides = monthly_rides.reindex(index = month_order)


# In[26]:


# Show the index
#==> ENTER YOUR CODE HERE
monthly_rides.index


# In[27]:


# Create a bar plot of total rides per month
#==> ENTER YOUR CODE HERE
plt.figure(figsize = (12, 7))
ax = sns.barplot( x= monthly_rides.index, y = monthly_rides)
ax.set_xticklabels(month_order)
plt.title('Ride Count By Month', fontsize = 16);


# **Plot total ride count by day**
# 
# Repeat the above process, but now calculate the total rides by day of the week.

# In[28]:


# Repeat the above process, this time for rides by day
#==> ENTER YOUR CODE HERE
day_rides = df['day'].value_counts()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday']
day_rides = day_rides.reindex(index = day_order)


# In[29]:


# Create bar plot for ride count by day
#==> ENTER YOUR CODE HERE
plt.figure(figsize =(12, 7))
ax = sns.barplot(x = day_rides.index, y = day_rides)
ax.set_xticklabels(day_order)
plt.title('Ride Count By Day', fontsize = 16);


# **Plot total revenue by day of the week**
# 
# Repeat the above process, but now calculate the total revenue by day of the week.

# In[30]:


# Repeat the process, this time for total revenue by day
#==> ENTER YOUR CODE HERE
revenue_by_day = df.groupby('day').sum()[['total_amount']]
revenue_by_day = revenue_by_day.reindex(index = day_order)
revenue_by_day


# In[31]:


# Create bar plot of total revenue by day
#==> ENTER YOUR CODE HERE
plt.figure(figsize =(12, 7))
ax = sns.barplot(x = revenue_by_day.index, y = revenue_by_day['total_amount'])
ax.set_xticklabels(day_order)
ax.set_ylabel('Revenue(USD)')
plt.title('Total Revenue By Day', fontsize = 16);


# **Plot total revenue by month**

# In[32]:


# Repeat the process, this time for total revenue by month
#==> ENTER YOUR CODE HERE
revenue_by_month = df.groupby('month').sum()[['total_amount']].reindex(index = month_order)
revenue_by_month


# In[33]:


# Create a bar plot of total revenue by month
#==> ENTER YOUR CODE HERE
plt.figure(figsize = (12, 7))
ax = sns.barplot(x = revenue_by_month.index, y = revenue_by_month['total_amount'])
ax.set_xticklabels(month_order)
ax.set_ylabel('Revenue (USD)')
plt.title('Total Revenue By Month', fontsize = 16);


# #### Scatter plot

# You can create a scatterplot in Tableau Public, which can be easier to manipulate and present. If you'd like step by step instructions, you can review the following link. Those instructions create a scatterplot showing the relationship between total_amount and trip_distance. Consider adding the Tableau visualization to your executive summary, and adding key insights from your findings on those two variables.

# [Tableau visualization guidelines](https://docs.google.com/document/d/1pcfUlttD2Y_a9A4VrKPzikZWCAfFLsBAhuKuomjcUjA/template/preview)

# **Plot mean trip distance by drop-off location**

# In[34]:


# Get number of unique drop-off location IDs
#==> ENTER YOUR CODE HERE
df['DOLocationID'].nunique()


# In[36]:


# Calculate the mean trip distance for each drop-off location
#==> ENTER YOUR CODE HERE
distance_dropoff = df.groupby('DOLocationID').mean()[['trip_distance']]


# Sort the results in descending order by mean trip distance
#==> ENTER YOUR CODE HERE
distance_dropoff = distance_dropoff.sort_values(by = 'trip_distance', ascending = True)
distance_dropoff


# In[37]:


# Create a bar plot of mean trip distances by drop-off location in ascending order by distance
#==> ENTER YOUR CODE HERE
plt.figure(figsize = (12, 7))
ax = sns.barplot(x = distance_dropoff.index, y = distance_dropoff['trip_distance'], order=distance_dropoff.index)
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_ylabel('Trip Distance')
plt.title('Mean Trip distance by drop off location', fontsize = 16);


# **Histogram of rides by drop-off location**

# First, check to whether the drop-off locations IDs are consecutively numbered. For instance, does it go 1, 2, 3, 4..., or are some numbers missing (e.g., 1, 3, 4...). If numbers aren't all consecutive, the histogram will look like some locations have very few or no rides when in reality there's no bar because there's no location. 

# In[38]:


# Check if all drop-off locations are consecutively numbered
#==> ENTER YOUR CODE HERE
df['DOLocationID'].max() - len(set(df['DOLocationID']))


# In[41]:


# DOLocationID column is numeric, so sort in ascending order
#==> ENTER YOUR CODE HERE
dropoff_sorted = df['DOLocationID'].sort_values()

# Convert to string
#==> ENTER YOUR CODE HERE
dropoff_sorted = dropoff_sorted.astype('str')
# Plot
#==> ENTER YOUR CODE HERE
plt.figure(figsize = (15, 5))
sns.histplot(data = dropoff_sorted, bins = range(0, 270, 1))
plt.xticks([])
plt.xlabel('Dropoff Locations')
plt.title('Histogram of rides by drop-off location', fontsize=16);


# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## PACE: Execute 
# 

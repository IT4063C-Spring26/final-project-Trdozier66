#!/usr/bin/env python
# coding: utf-8

# # Vehicle Performance and Fuel Efficiency Analysis📝
# 
# ![Banner](./assets/banner.jpeg)
# 

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# 📝 <!-- Answer Below -->
# Vehicle Performance and Fuel Efficiency Analysis
# 
# This project explores how different vehicle characteristics influence fuel efficiency. Fuel efficiency, measured in miles per gallon (MPG), is an important factor for both consumers and manufacturers because it affects fuel costs, environmental impact, and overall vehicle performance. Understanding what factors contribute to higher or lower fuel efficiency can help identify trends in automotive design and performance.
# 
# The dataset used in this project contains information about various car models including their engine size, horsepower, weight, acceleration, number of cylinders, and year of production. These characteristics can significantly affect how efficiently a vehicle uses fuel.
# 
# Through exploratory data analysis (EDA) and data visualization, this project aims to 

# ## Project Question
# 
# The main question guiding this project is:
# 
# What vehicle characteristics most strongly influence fuel efficiency (miles per gallon)?
# 
# More specifically, this analysis will explore how variables such as horsepower, vehicle weight, number of cylinders, engine displacement, and acceleration relate to fuel efficiency. Many of these factors are known to impact how much fuel a vehicle consumes, but analyzing the dataset allows us to observe these relationships quantitatively.
# 
# This project will investigate whether vehicles with higher horsepower tend to have lower fuel efficiency, whether heavier vehicles consume more fuel, and how engine size and number of cylinders contribute to overall performance. By examining these relationships through statistical summaries and visualizations, the analysis aims to identify patterns that explain variations in MPG across different vehicles.
# 
# The results of this analysis can provide useful insights into how vehicle design influences fuel consumption and efficiency.features have the strongest influence on MPG and how these factors interact with one another.
# 

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 <!-- Answer Below -->
# 
# This project analyzes multiple automobile datasets in order to understand how different vehicle characteristics influence fuel efficiency. The primary goal is to examine the relationship between engine performance, vehicle design, and miles per gallon (MPG). The analysis focuses on identifying patterns that explain why some vehicles are more fuel efficient than others.
# 
# The analysis begins with loading the datasets and examining their structure. Exploratory Data Analysis (EDA) is used to understand the variables contained in each dataset, their data types, and the overall distribution of the data. Functions such as `info()` and `describe()` are used to generate summary statistics that provide insight into variables such as horsepower, vehicle weight, cylinders, engine displacement, and fuel efficiency.
# 
# After understanding the structure of the datasets, data quality checks are performed. These checks include identifying missing values, detecting duplicate rows, and verifying that each column is stored in the correct data type. Cleaning the data ensures that the analysis is performed on reliable and consistent information.
# 
# Once the data has been prepared, visualizations are created to explore patterns and relationships between variables. Histograms are used to examine the distribution of fuel efficiency across vehicles. Scatter plots help visualize relationships between variables such as horsepower and MPG or vehicle weight and MPG. Boxplots are used to identify outliers that may represent unusually efficient or inefficient vehicles.
# 
# Correlation analysis is also performed to understand how different numerical variables relate to each other. A correlation heatmap helps identify which vehicle characteristics have the strongest relationship with fuel efficiency.
# 
# By analyzing trends across the datasets, the project aims to determine which factors most strongly influence vehicle fuel efficiency. These insights may also support future predictive modeling, where machine learning techniques could be used to estimate MPG based on engine and vehicle characteristics.

# ## Data Sources
# 
# This project uses three datasets related to vehicle performance and fuel efficiency.
# 
# Dataset 1: Auto Dataset  
# https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv  
# This dataset includes vehicle characteristics such as miles per gallon (mpg), cylinders, horsepower, weight, and acceleration.
# 
# Dataset 2: MPG Dataset  
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv  
# This dataset provides fuel efficiency data along with information about engine displacement, horsepower, and vehicle origin.
# 
# Dataset 3: Cars Dataset  
# https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv  
# This dataset includes performance metrics such as mpg, cylinders, horsepower, weight, and acceleration for various vehicles.
# 
# Using multiple datasets helps provide broader insight into the factors that influence vehicle fuel efficiency and performance.

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->
# 
# 
# The analysis for this project begins by loading three vehicle-related datasets that contain information about automobile performance and fuel efficiency. These datasets include variables such as miles per gallon (mpg), horsepower, engine displacement, cylinders, vehicle weight, acceleration, and country of origin. These features provide useful indicators of how vehicle design and engine characteristics influence fuel efficiency.
# 
# The first step in the analysis is exploratory data analysis (EDA). During this stage, the structure of each dataset is examined using functions such as `info()` and `describe()` to understand the available variables, data types, and summary statistics. These summaries provide insight into the distribution of key variables and allow us to identify potential anomalies or unusual values.
# 
# Next, the datasets are checked for data quality issues. This includes identifying missing values, detecting duplicate rows, and verifying that each variable is stored in the correct data type. Addressing these issues ensures that the analysis is based on reliable and consistent data.
# 
# Data visualization techniques are then used to explore patterns and relationships within the datasets. Histograms are used to examine the distribution of fuel efficiency values, while scatter plots help visualize relationships between variables such as horsepower and miles per gallon. Boxplots are used to identify potential outliers in the data, and correlation heatmaps are used to examine relationships between numerical variables across the dataset.
# 
# By comparing trends across the three datasets, it becomes possible to identify consistent patterns in how engine characteristics and vehicle design influence fuel efficiency. These insights provide a foundation for further analysis and potential predictive modeling, where machine learning techniques could be used to estimate fuel efficiency based on vehicle specifications.
# 

# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->
# 
# 
# The following datasets and resources were used in this project to perform exploratory data analysis and visualization.
# 
# ### Datasets
# 
# Auto Dataset  
# https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv
# 
# MPG Dataset  
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv
# 
# Cars Dataset  
# https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv
# 
# These datasets contain information about vehicle performance including miles per gallon (mpg), horsepower, cylinders, displacement, vehicle weight, acceleration, and manufacturing origin. They were used to explore how different vehicle characteristics influence fuel efficiency.
# 
# ### Python Libraries
# 
# Pandas Documentation  
# https://pandas.pydata.org/docs/
# 
# Matplotlib Documentation  
# https://matplotlib.org/stable/contents.html
# 
# Seaborn Documentation  
# https://seaborn.pydata.org/
# 
# These libraries were used for data loading, data manipulation, statistical summaries, and creating visualizations during the exploratory data analysis process.
# 
# ### Additional Resources
# 
# Python Requests Library Documentation  
# https://docs.python-requests.org/
# 
# These resources were helpful for understanding how to load datasets and perform data analysis using Python.

# ## Exploratory Data Analysis (EDA)

# In[63]:


url2 = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"

df2 = pd.read_csv(url2)

df2.head()


# In[68]:


url3 = "https://raw.githubusercontent.com/vega/vega-datasets/main/data/cars.json"

df3 = pd.read_json(url3)

df3.head()


# In[44]:


import pandas as pd

url = "https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv"

df = pd.read_csv(url)

df.head()


# In[70]:


df.info()


# In[71]:


df.describe()


# In[47]:


df.isnull().sum()


# In[48]:


df.duplicated().sum()


# The dataset was explored to understand its structure, data types, and potential issues.
# The info() function shows column types and missing values. The describe() function
# provides statistical summaries such as mean, min, max, and standard deviation.
# Missing values and duplicates were also checked to determine whether data cleaning
# would be necessary before analysis.

# ## Data Visualization
# 

# In[73]:


import matplotlib.pyplot as plt

plt.hist(df["mpg"], bins=20)
plt.title("Distribution of Miles Per Gallon (MPG)")
plt.xlabel("MPG")
plt.ylabel("Frequency")
plt.show()


# This histogram shows the distribution of miles per gallon (MPG) across vehicles in the dataset. It helps identify the range of fuel efficiency and whether most cars fall within a certain efficiency range.

# In[74]:


plt.scatter(df2["horsepower"], df2["mpg"])
plt.title("Horsepower vs MPG")
plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.show()


# The scatter plot illustrates the relationship between horsepower and fuel efficiency. Vehicles with higher horsepower generally tend to have lower miles per gallon.

# In[75]:


import seaborn as sns

sns.boxplot(x=df3["Miles_per_Gallon"])
plt.title("Distribution of Miles Per Gallon")
plt.show()


# The boxplot summarizes the distribution of MPG values and highlights potential outliers that represent unusually efficient or inefficient vehicles.

# In[76]:


sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Between Vehicle Features")
plt.show()


# The correlation heatmap displays relationships between numerical variables in the dataset. Strong positive or negative correlations indicate variables that may influence vehicle fuel efficiency.

# In[77]:


## Data Cleaning and Transformation
df.isnull().sum()


# Missing values were checked to determine whether any columns contained incomplete data. Missing data can negatively affect statistical analysis and machine learning models, so identifying them early helps determine whether they should be removed or replaced.

# In[54]:


df = df.fillna(df.mean(numeric_only=True))


# Any missing numerical values were replaced using the mean of the corresponding column. This helps preserve the dataset while minimizing the impact of missing observations.

# In[55]:


df = df.drop_duplicates()


# Duplicate records were removed to prevent repeated observations from biasing the analysis. Ensuring that each row represents a unique observation improves the accuracy of the results.

# In[78]:


df.dtypes


# Data types were examined to ensure that variables are stored in appropriate formats. Correct data types are important for performing statistical analysis and creating visualizations.

# ## Machine Learning Plan
# Machine learning techniques can be used to further analyze patterns within the dataset. For this project, a supervised learning approach such as linear regression could be used to examine relationships between variables and predict academic performance outcomes.
# 
# Regression models are useful when trying to understand how one or more variables influence another variable. In this case, academic performance indicators such as test scores could potentially be predicted based on other factors in the dataset.
# 
# One challenge when applying machine learning models is ensuring the dataset is clean and properly structured. Missing values, inconsistent data types, or limited features may reduce model accuracy. Another challenge is making sure that the dataset contains enough relevant variables to build a meaningful predictive model.

# ## Prior Feedback and Updates
# Feedback from peers and the teaching team emphasized the importance of expanding the exploratory data analysis and including multiple visualizations to better understand the dataset. Based on this feedback, additional charts were created to analyze distributions and relationships between variables.
# 
# The dataset was also examined for missing values, duplicates, and potential anomalies to improve data quality. These updates helped strengthen the analysis and ensure the dataset is prepared for future modeling and deeper analysis.

# In[ ]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')


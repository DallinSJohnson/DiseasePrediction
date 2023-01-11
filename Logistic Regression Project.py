#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math


# In[7]:


#Original model that was deemed less accurate
#Create Function to input your data
def dengue_prediction_first_model(age, economic_status, sector, savings):
    
    #Economic status is recorded
    
    if economic_status == "Middle" or "middle":
        middle_status = 1
        upper_status = 0
    elif economic_status == "Upper" or "upper":
        middle_status = 0
        upper_status = 1
    elif economic_status == "Lower" or "lower":
        middle_status = 0
        upper_status = 0
    else:
        print("Socio-Economic class can only be lower, middle, or upper.")
    
    #Sector 
    
    if sector == 2:
        sector_answer = 1
    elif sector == 1:
        sector_answer = 0
    else: 
        print("Sector can only be 1 or 2")
    
    #Savings
    
    if savings == "Yes" or "yes":
        savings_answer = 1
    elif savings == "No"or "no":
        savings_answer = 0
    else:
        print("Yes or no answers only for savings")
    
    #Plug independent variables into the final equation
    #Answer will be in Log odds
    #Convert answer from log odds into probability
    
    equation_answer_log = 2.076617 - (0.02728 * age) + (0.202055 * middle_status) + (0.237633 * upper_status) - (1.249464 * sector_answer) - (0.040692 * savings_answer) 
    equation_answer_probability = math.exp(equation_answer_log) / (1 + math.exp(equation_answer_log))
    
    #Final Output
    
    probability_dengue = equation_answer_probability * 100
    print(f"The probability of this person having dengue is {round(equation_answer_probability, 4)} or {round(probability_dengue, 2)}%")


# In[8]:


#Input age, socio-economic class, sector, and whether they had a savings account or not
dengue_prediction_first_model(100, "upper", 1, "no")


# In[9]:


#Here is the more accurate second model that was produced

def dengue_prediction_second_model(age, sector):
    #Sector
    
    if sector == 2:
        sector_answer = 1
    elif sector == 1:
        sector_answer = 0
    else: 
        print("Sector can only be 1 or 2")
    
    #log odds answer and the probability
    
    equation_answer_log = 2.15966 - (0.02681 * age) + (1.18169 * sector)
    equation_answer_probability = math.exp(equation_answer_log) / (1 + math.exp(equation_answer_log))
    
    #Final Output
    
    probability_dengue = equation_answer_probability * 100
    print(f"The probability of this person having dengue is {round(equation_answer_probability, 4)} or {round(probability_dengue, 2)}%")


# In[14]:


# Inpyt only age and which sector they lived in 
dengue_prediction_second_model(29, 2)


# In[ ]:





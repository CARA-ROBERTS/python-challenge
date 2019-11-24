#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd


# In[52]:


# Reference the file where the CSV is located
budget_path_csv = "budget_data.csv"

# Import the data into a Pandas DataFrame
budget_df = pd.read_csv(budget_path_csv)
budget_df.head()


# In[53]:


budget_df.count()


# In[54]:


budget_df.columns


# In[55]:


budget_df.rename(columns= {'Date':'Month-Year'})


# In[56]:


budget_df["Date"].count()


# In[75]:


Total_Months_count = budget_df["Date"].count()
print(Total_Months_count)


# In[59]:


Total = budget_df["Profit/Losses"].sum()

Greatest_Decrease= budget_df["Profit/Losses"].min()
print("$",Total)


# In[60]:


Difference= budget_df["Profit/Losses"].diff(+1)
budget_df["Difference"]=Difference
budget_df.head()


# In[61]:


Greatest_Increase = budget_df["Difference"].max()
print("$",Greatest_Increase, budget_df.loc[budget_df["Difference"]==1926159,"Date"])


# In[62]:


Greatest_Decrease= budget_df["Difference"].min()
print("$",Greatest_Decrease, budget_df.loc[budget_df["Difference"]==-2196167,"Date"])


# In[71]:


Average_Change= budget_df["Difference"].mean()
Average_Change=round(int(Average_Change))
print("$",Average_Change)


# In[84]:


print("Financial_Analysis")
print("-------------------")
print(f"Total Months:{(Total_Months_count)}")
print(f"Average Change:{(Average_Change)}")
print(f"Greatest Increase:{(Greatest_Increase)}")
print(f"Greatest Decrease:{(Greatest_Decrease)}")


# In[ ]:





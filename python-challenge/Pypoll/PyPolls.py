#YASSS
#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[7]:


# Reference the file where the CSV is located
poll_path_csv = "election_data.csv"

# Import the data into a Pandas DataFrame
poll_df = pd.read_csv(poll_path_csv)
poll_df.head()


# In[8]:


poll_df["Voter ID"].count()


# In[9]:


voter_count= poll_df["Voter ID"].count()


# In[11]:


Election_Results= pd.DataFrame({"Total Votes":[voter_count]})
Election_Results


# In[13]:


candidate_count= poll_df["Candidate"].unique()
candidate_count


# In[15]:


Candidates_counts = poll_df["Candidate"].value_counts()
Candidates_counts


# In[21]:


Candidate_percentages= (poll_df["Candidate"].value_counts()/poll_df["Candidate"].count())*100

Candidate_percentages


# In[48]:


print("Election Results")
print("-------------------")
print(f"{(Candidate_percentages)}")

print(f"{(Candidates_counts)}")

print(f"Winner : Khan!!!")
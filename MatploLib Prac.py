#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install matplotlib


# In[25]:


import matplotlib.pyplot as plt
import pandas as pd
#using matplot only

Category: ["Category A","Category B", "Category C", "Category D"]
size:[18,20,53,6]
plt.pie(size,labels=labels,autopct='%1.2f%%',startangle=140)
plt.title("Data")
plt.show()


#using matplot and pandas
data={'Category': ["Category A","Category B", "Category C", "Category D"],
     'size':[18,20,53,6]}


df=pd.DataFrame(data)
df.set_index('Category', inplace=True)

ax=df.plot.pie(y='size',autopct='%1.2f%%',startangle=140, legend=False,figsize=(4,4))
ax.set_ylabel('')
ax.set_title("My Pie Chart")

plt.show()


# In[ ]:





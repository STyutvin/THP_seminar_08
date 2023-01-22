#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Известно, что рост футболистов в сборной распределен нормально
# с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,
# среднее выборочное составляет 174.2. Найдите доверительный интервал для математического
# ожидания с надежностью 0.95.


# In[2]:


import numpy as np
import scipy.stats as stats
m=174.2 # среднее выборочное
n=27    # объем выборки
D=25    # дисперсия генеральной совокупности


# In[7]:


# Z-критерий для двухстороннего теста с уровнем значимости 0,05
z=stats.norm.ppf(1-0.05/2)
z       # z=1.959963984540054


# In[8]:


# Определим нижнюю границу интервала L1
L1=m-z*np.sqrt(D/n)
L1      # L1=172.3140237765397


# In[10]:


# Определим верхнюю границу интервала L2
L2=m+z*np.sqrt(D/n)
L2      # L2=176.08597622346028


# In[ ]:


# Ответ: [172.31; 176.09]


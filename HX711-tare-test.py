#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time 
from hx711 import HX711
import statistics 
import numpy as np
hx711 = HX711(
        dout_pin=17,
        pd_sck_pin=8,  
        channel='A',
        gain=64
    )


hx711.reset()
measures = hx711.get_raW_data()
weights = []
c = 0
avgTare = 0
for i in(range(1000)):
    measures = hx711.get_raw_data(10)
    if (np.mean(measures) < 1100) : #not sure if needed
        c = c+1
        avgTare = (avgTare + statistics.mean(measures))/c
        measures = 0
        weights.append(measures)
    if measures != 0: 
        measures = np.mean(measures) - avgTare
        weights.append(np.mean(measures))
    print(measures)
    time.sleep(0.05)


# In[ ]:





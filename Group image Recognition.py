#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 ,os
import numpy as np
import math


# In[2]:


img = cv2.imread("C:/Users/gayat/Downloads/classmates.jpeg")


# In[3]:


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# In[4]:


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# In[5]:


faces = face_cascade.detectMultiScale(gray, 1.3, 5)


# In[ ]:


while 1:
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    cv2.imshow("Image",img)
    k = cv2.waitKey(30) & 0xff
if k == 27:
    break


# In[ ]:


cv2.destroyAllWindows()


# In[ ]:





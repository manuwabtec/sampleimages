import os as os
from scipy import ndimage, misc
import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
plt.style.use('seaborn')


def get_image(index, *argv):

  data_dir  = '//content//sampleimages//CSCV_Image//coupler_on_left'

  for arg in argv:
    if arg == 'R':
      data_dir  = '//content//sampleimages//CSCV_Image//coupler_on_right'    

  images    = os.listdir(data_dir )

  filename  = os.path.join(data_dir, images[index])

  if os.path.isfile(filename):
    
    img = cv2.imread(filename)
    return img
  
  return np.zeros((200, 200), dtype=int)
  
  
def get_image_trkv():

  data_dir  = '//content//sampleimages//TRKV_Image'
   
  images    = os.listdir(data_dir )

  filename  = os.path.join(data_dir, images[0])
  img_defect = cv2.imread(filename)
  filename  = os.path.join(data_dir, images[1])
  img_no_defect = cv2.imread(filename)
  
  return img_defect, img_no_defect  
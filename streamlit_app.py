import streamlit as st
import numpy as np
import pandas as pd
#import kornia
#from torch import nn
#import torch
#from torchvision.transforms import functional as F
#from torchvision.utils import make_grid
#from streamlit_ace import st_ace
from PIL import Image
import cv2
import tarfile
#import paddlehub as hub

# -- Set page config
apptitle = 'Cloud Classification'
st.set_page_config(page_title=apptitle, page_icon=":cloud:")

# Title the app
st.title('Cloud Classification :cloud:')

option = st.sidebar.selectbox(
    'Services you are interested',
    ('Introduction about this app','Choose the image you want to detect'))

if option == 'Introduction about this app':
    st.subheader('Introduction')
    '''
    
    Our cloud detection application can identify the type of cloud you upload and display it.
    
    The clouds it can identify include cirrus, cumulus, cumulonimbus
    
    :point_left:Please select **Choose the image you want to detect** in the sidebar to start.
    
    You can see more about this app in the [github](https://github.com/YUA1024/YUA1024).
    '''
    

else:
    st.subheader('Application')
    '''
    You can display the image in full size by hovering it and clicking the double arrow.
    '''
    # sidebar
    uploaded_file = st.sidebar.file_uploader("Choose a image you want to detect")
    if uploaded_file is not None:
        im = Image.open(uploaded_file)
    else:
        im = Image.open(r"./clouds/1111.jfif")
    st.sidebar.image(im, caption="Input Image", width=256)
    st.image(im, caption='the cloud you choose', width=512)


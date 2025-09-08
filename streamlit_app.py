## Library imports
import pandas as pd 
import numpy as np 
import streamlit as st
from streamlit import runtime
import pickle

## Local imports
from components import home_page
from components import image_enhancer
from components import new_image_enhancer
from components import about_us
from config import PAGES
from model import run_inference

@st.cache_data
def load_data():
    """ 
    Loads the required sample image paths into the session state

    Args:
        None

    Returns:
        None
    """

    ## Load some sample chest x-ray images
    with open('./data/val_images.pkl', 'rb') as f:
        val_data_list = pickle.load(f)

    ## Save the sample image paths into the session state
    st.session_state.val_images = val_data_list

    model = run_inference.init_model()

    return model

## Set the page tab title
st.set_page_config(page_title="Medical Image Enhancer", page_icon="🤖", layout="wide")

## Load the initial app data
model = load_data()

## Landing page UI
def run_UI():
    """
    The main UI function to display the UI for the webapp
    """

    ## Set the page title and navigation bar
    st.sidebar.title('选择菜单')
    if st.session_state["page"]:
        page=st.sidebar.radio('网站导航', PAGES, index=st.session_state["page"])
    else:
        page=st.sidebar.radio('网站导航', PAGES, index=0)
    st.experimental_set_query_params(page=page)


    ## Display the page selected on the navigation bar
    if page == '首页':
        st.sidebar.write("""
            ## 关于
            本项目旨在利用最先进的生成对抗网络（Generative Adversarial Networks）技术，提升医学X光图像的分辨率和质量。
            该项目采用了Swift-SRGAN模型架构，以增强低质量X光图像的分辨率。
        """)
        st.title("医学图像超分 ☠️")
        home_page.home_page_UI()

    elif page == '图像增强示例':
        st.sidebar.write("""
            ## 关于
            本项目旨在利用最先进的生成对抗网络（Generative Adversarial Networks）技术，提升医学X光图像的分辨率和质量。
            该项目采用了Swift-SRGAN模型架构，以增强低质量X光图像的分辨率。
        """)
        st.title("图像超分示例 ☠️")
        image_enhancer.image_enhancer_UI(model)
    
    elif page == '尝试使用您自己的图像':
        st.sidebar.write("""
            ## 关于
            本项目旨在利用最先进的生成对抗网络（Generative Adversarial Networks）技术，提升医学X光图像的分辨率和质量。
            该项目采用了Swift-SRGAN模型架构，以增强低质量X光图像的分辨率。
        """)
        st.title("尝试使用您自己的图像 ☠️")
        new_image_enhancer.new_image_enhancer_UI(model)

    else:
        st.sidebar.write("""
            ## 关于
            本项目旨在利用最先进的生成对抗网络（Generative Adversarial Networks）技术，提升医学X光图像的分辨率和质量。
            该项目采用了Swift-SRGAN模型架构，以增强低质量X光图像的分辨率。
        """)
        st.title("医学图像超分 ☠️")
        about_us.about_us_UI()


if __name__ == '__main__':
    ## Load the streamlit app with "Recipe Recommender" as default page
    if runtime.exists():

        ## Get the page name from the URL
        url_params = st.experimental_get_query_params()
        if len(url_params.keys()) == 0 or "page" not in st.session_state:
            st.session_state.page = 0

        if 'loaded' not in st.session_state:
            if len(url_params.keys()) == 0:
                ## Set the default page as "首页"
                st.experimental_set_query_params(page='首页')
                url_params = st.experimental_get_query_params()
                st.session_state.page = PAGES.index(url_params['page'][0])
        
        ## Call the main UI function
        run_UI()
import logging
import numpy as np
import pandas as pd
import streamlit as st

## Initiate logging
logger = logging.getLogger(__name__)

def home_page_UI():
    """
    The main UI function to display the Home page UI for webapp
    """
    
    ## Display details on super resolution
    st.divider()
    st.subheader("什么是超分？ 🩻")
    st.write("将含有噪声的低质量图像恢复并重建为高质量、高分辨率图像的过程被称为图像超分")
    
    ## Display details on project
    st.subheader("关于项目 ⭐")
    st.write("""
            本项目旨在利用最先进的生成对抗网络（Generative Adversarial Networks, GANs）技术，提升医学X光图像的分辨率和质量。项目采用了Swift-SRGAN模型架构，以增强低质量X光图像的分辨率。
            """)
    
    ## Display details on model performance
    st.divider()
    st.subheader("模型性能 🧨")
    st.write("""
            生成的GAN模型通过不同的指标（如PSNR和SSIM）与真实值进行了评估和比较。相比于PSNR，SSIM通常被认为是一种更具感知准确性的度量标准，因为它考虑了人类视觉系统对亮度、对比度和结构变化的敏感性。
            """)
    
    # Display PSNR
    row_1_col1, row_1_col2 = st.columns(2)
    with row_1_col1:
        st.success('峰值信噪比: 41.66 db', icon="👀")
        st.write("""
            - 一种用于衡量图像质量的指标。
            - 通过比较两个图像的像素值并计算最大像素值与均方误差之间的比率来衡量它们之间的差异。
            - PSNR越高表示两个图像之间的差异越小，表明图像质量越高。
        """)
    
    # Display SSIM
    with row_1_col2:
        st.info('结构相似性指数: 0.96', icon="🎯")
        st.write("""
            - 一种用于衡量两个图像之间相似性的指标。
            - 考虑了图像的结构信息，并基于结构因素计算两个图像之间的相似度得分。
            - 更高的SSIM分数表示两个图像之间的相似度更高。
        """)

    ## Display details on risks and limitations
    st.divider()
    st.subheader("风险和局限性 ⚠️")
    st.write("""
            - GANs可能难以准确捕捉极低分辨率医学X光图像（< 128 x 128）中的重要细节，这可能会对生成的高质量图像产生负面影响。 
            - GANs可能会生成不存在的特征。
            - GANs在医学成像中的使用引发了关于偏见、问责和透明度等问题的伦理担忧。
            """)
    st.caption("削减风险 ✅")
    st.write("""为了减少偏见的风险，模型在一个多样化的X光图像数据集上进行了训练。 
            此外，向模型中添加感知损失有助于确保生成的图像与原始图像相似，并在增强分辨率时不会生成新的特征。
            """)

    ## Display details on about me
    ## st.divider()
    ## st.subheader("About me")
    ## st.write("""
    ## I am doing this project as a part of our core curriculam at Duke University for Masters in Artificial Intelligence (Course: AIPI 540: Deep Learning Applications)
    ## """)
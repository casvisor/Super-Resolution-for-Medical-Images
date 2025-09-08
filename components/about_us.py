## Library imports
import streamlit as st
from PIL import Image

def about_us_UI():
    """
    The main UI function to display the About US page UI.
    """

    ## Display about the project section
    st.divider()
    st.subheader("关于项目")
    st.write("""
             本项目旨在利用最先进的生成对抗网络（Generative Adversarial Networks）技术，提升医学X光图像的分辨率和质量。
             该项目采用了Swift-SRGAN模型架构，以增强低质量X光图像的分辨率。
        """)
    
    ## Display dataset details
    st.subheader("数据集")
    st.write("""
             用于训练超分辨率模型的数据集是NIH胸部X光(https://www.kaggle.com/datasets/nih-chest-xrays/data)。
             该数据集包含112,120张X光图像。数据集中的图像为高分辨率图像（1024 x 1024）。
             尽管这个数据集主要用于肺部疾病识别，但我们剥离了每张图像的标签，并使用这些高分辨率的X光图像来训练超分GAN。
            """)
    ## Display Model Architecture
    st.divider()
    st.subheader("模型架构")
    st.image("./data/images/network_architecture.png", caption="Model Architecture")
    st.write("""
             采用了Swift-SRGAN模型架构(https://arxiv.org/pdf/2111.14320.pdf)以增强低质量X光图像的分辨率。
             生成网络在一个提出的胸部X光图像数据集上进行了训练。给定一张256 x 256大小的输入图像，生成器会生成一张1024 x 1024大小的高分辨率图像。
            """)
    
    # Details of Generator
    st.caption("生成器架构")
    st.write("""
             生成器由深度可分离卷积层组成，这些层用于减少网络中的参数数量和计算量。网络的主要部分由16个残差块构成。
             每个块包含一个深度卷积，随后是批量归一化、PReLU激活函数、另一个深度卷积和批量归一化，最后是一个跳过连接（skip connection）。经过残差块后，图像通过上采样块，最后通过一个卷积层以生成最终输出图像。
            """)
    
    # Details of Discriminator
    st.caption("判别器架构")
    st.write("""
            判别器由8个深度可分离卷积块组成。每个块包含一个深度卷积，随后是批量归一化和LeakyReLU激活函数。
             经过这8个块后，图像通过平均池化层（Avg Pooling）和一个全连接层以生成最终输出。
             判别器的目标是将生成器生成的超分辨率图像分类为假图像，并将原始高分辨率图像分类为真实图像。
            """)
    
    ## Display details on Loss functions used
    st.divider()
    st.subheader("Loss functions")
    st.write("""
            生成器的损失函数是多种损失的组合。主要的是感知损失，它由对抗损失和内容损失组合而成。
            """)
    code = '''Total_Loss = Image_Loss + Perception_Loss + TV_Loss

Perceptual_Loss = Adversarial_Loss + Content_Loss
    '''
    st.code(code, language='python')

    # Details of Image loss
    st.caption("图像损失")
    st.write("""
            这是一个简单的损失函数，它计算生成图像与原始高分辨率图像像素之间的均方误差（Mean Squared Error）。
            """)
    
    # Details of Perceptual loss
    st.caption("内容损失")
    st.write("""
            它表示在图像处理过程中丢失或扭曲的信息。
             生成器生成的图像和原始高分辨率图像通过MobileNetV2网络传递，以计算两者的特征向量。
             内容损失计算为原始图像和生成图像的特征向量之间的欧几里得距离。
            """)
    
    # Details of Adversarial loss
    st.caption("Adversarial loss")
    st.write("""
            对抗损失用于确保生成的图像与真实图像无法区分。它基于判别器网络的输出进行计算。生成器试图最小化这一损失，而判别器则试图最大化这一损失。
            """)
    
    # Details of Total Variation loss
    st.caption("全变分损失")
    st.write("""
             全变分损失测量图像中相邻像素之间的强度或颜色的变化。全变分损失定义为图像中水平和垂直方向上相邻像素之间绝对差异的总和。
            """)
    
    ## Display details on About me
    ## st.divider()
    ## st.subheader("About me")

    ## st.write("""
    ## I am doing this project as a part of our core curriculam at Duke University for Masters in Artificial Intelligence (Course: AIPI 540: Deep Learning Applications)
    ## """)
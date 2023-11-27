import streamlit as st 
#from PIL import image
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd 
import numpy as np
import pickle
import librosa  
from scipy.stats import skew, kurtosis
st.title('klasifikasi emosi')  
st.write('untuk mengetahui jenis emosi audio')
#img = image.open(.jpg)
#st.image(img)

audio =st.file_uploader('masukan file audio',['mp3','wav'])
if audio:
    st.audio(audio)
    y , sr= librosa.load(audio)
    #untuk menghitung nilai ZCR
    zcr_mean = np.mean(librosa.feature.zero_crossing_rate(y=y))
    zcr_median = np.median(librosa.feature.zero_crossing_rate(y=y))
    zcr_std_dev = np.std(librosa.feature.zero_crossing_rate(y=y))
    zcr_kurtosis = kurtosis(librosa.feature.zero_crossing_rate(y=y)[0])
    zcr_skew = skew(librosa.feature.zero_crossing_rate(y=y)[0])

    # UNTUK MENGHITUNG NILAI RMSE
    rmse = np.sum(y**2) / len(y)
    rmse_median = np.median(y**2)
    rmse_std_dev = np.std(y**2)
    rmse_kurtosis = kurtosis(y**2)
    rmse_skew = skew(y**2)

    fitur ={'ZCR Mean':zcr_mean,
            'ZCR Median':zcr_median,
            'ZCR Std Dev':zcr_std_dev,
            'ZCR Kurtosis':zcr_kurtosis,
            'ZCR Skew':zcr_skew,
            'RMSE':rmse,
            'RMSE Median':rmse_median,
            'RMSE Std Dev':rmse_std_dev,
            'RMSE Kurtosis':rmse_kurtosis,
            'RMSE Skew':rmse_skew,
    }
    data = pd.DataFrame(fitur,index=[0])
    st.write('--------------- Data Audio ------------')
    st.write(data)
    with open('skala.pkl','rb') as prepro:
        skala = pickle.load(prepro)
    data_norm = skala.transform(data)
    st.write('---------- Data Hasil Normalisasi ----------')
    st.write(data_norm)
    with open('PCA9.pkl', 'rb') as pca:
        loadpca= pickle.load(pca)
    pca_train = loadpca.transform(data_norm)
    st.write('---------- Data Hasil Ekstraksi Fitur dengan PCA ----------')
    st.write(pca_train)
    with open('pca_knn.pkl','rb') as pca_knn:
        pcaknn = pickle.load(pca_knn)
    predict_pca = pcaknn.predict(pca_train)
    #st.write(predict)
    for i in predict_pca:
        st.write('Jenis emosi dari file tersebut adalah :', i)
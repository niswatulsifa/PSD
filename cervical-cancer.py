import streamlit as st
import pandas as pd
import numpy as np
import tkinter as tk
from streamlit_option_menu import option_menu
from pycaret.classification import *
from PIL import Image

st.title("Cervical Cancer Behavior Risk")
st.write('Aplikasi ini dapat digunakan untuk memprediksi apakah terkena Kanker Serviks atau tidak')

selected = option_menu(
    menu_title=None,
    options=['Data','Implementasi','Profil'],
    orientation='horizontal',
    menu_icon=None,
    default_index=0,
    styles={
        "nav-link":{
        "font-size":"11.5px",
        "text-align":"center",
        "margin":"5px",
        "--hover-color":"#eee",},
        "nav-link-selected":{
        "background-color":"red"},
    }
)

if (selected == 'Data') :
    st.title("Dataset Cervical Cancer Behavior Risk")
    st.write("Kanker serviks adalah kanker yang tumbuh pada sel-sel di leher rahim. Kanker ini umumnya berkembang perlahan dan baru menunjukkan gejala ketika sudah memasuki stadium lanjut. Oleh sebab itu, penting untuk mendeteksi kanker serviks sejak dini sebelum timbul komplikasi serius.")
    st.write('Untuk mendeteksi apakah terkena Kanker Serviks atau tidak')
    st.write('Data yang saya gunakan disini saya dapatkan dari UCI pada link : https://archive.ics.uci.edu/dataset/537/cervical+cancer+behavior+risk')
    st.write('Data Cervical Cancer Behavior Risk merupakan Type Data Numerical.')
    st.write('Tentang Dataset : ')
    st.write('Dataset ini dikumpulkan untuk mendeteksi apakah terkena kanker serviks atau tidak.')
    st.write('Dataset ini terdiri dari 20 atribut/fitur, dengan 19 fitur dan 1 label (berasal dari 8 variabel, nama variabel merupakan kata pertama pada setiap atribut) diantaranya yaitu :')
    st.write('1. behavior_sexualRisk (Perilaku Seksual Resiko) = Perilaku seksual berisiko pada kanker serviks dapat mencakup praktek-praktek yang meningkatkan risiko terpapar human papillomavirus (HPV), yang merupakan penyebab utama kanker serviks. HPV adalah virus yang ditularkan secara seksual, dan beberapa tindakan seksual tertentu dapat meningkatkan risiko paparan virus ini.')
    st.write('2. behavior_eating (Perilaku Makan) = Perilaku makan pada kanker serviks dapat mencakup sejumlah faktor yang berkaitan dengan pola makan dan gaya hidup yang dapat memengaruhi risiko terjadinya atau perkembangan kanker serviks.')
    st.write('3. behavior_personalHygine (Perilaku Kebersihan Pribadi) = Perilaku kebersihan pribadi atau personal hygiene yang baik dapat memainkan peran dalam mencegah infeksi HPV (Human Papillomavirus), yang merupakan penyebab utama kanker serviks.')
    st.write('4. intention_aggregation (Agregasi Faktor Resiko) = Agregasi faktor risiko pada kanker serviks merujuk pada kecenderungan beberapa faktor risiko kanker serviks untuk terkumpul atau berkumpul pada individu tertentu. Ini berarti bahwa seseorang mungkin memiliki lebih dari satu faktor risiko yang dapat meningkatkan risiko mereka untuk mengembangkan kanker serviks.')
    st.write('5. intention_commitment (Komitmen Niat) = Komitmen untuk pencegahan kanker serviks mencakup sikap atau keputusan untuk aktif terlibat dalam langkah-langkah pencegahan kanker serviks. Pencegahan kanker serviks melibatkan serangkaian tindakan yang dapat diambil oleh individu untuk mengurangi risiko terkena kanker serviks atau untuk mendeteksi kondisi tersebut pada tahap awal.')
    st.write('6. attitude_consistency (Konsistensi Sikap) = Konsistensi sikap pada kanker serviks merujuk pada kesesuaian atau kecocokan antara sikap yang dimiliki oleh individu terhadap kanker serviks dan perilaku atau tindakan yang mereka tunjukkan sehubungan dengan pencegahan atau deteksi dini kanker serviks.')
    st.write('7. attitude_spontaneity (Spontanitas Sikap) = Spontanitas sikap terkait kanker serviks merujuk pada sejauh mana sikap atau reaksi seseorang terhadap masalah kanker serviks muncul secara alami atau tanpa rangsangan atau pengaruh eksternal yang signifikan.')
    st.write('8. norm_significantPerson (Norma Orang Penting) = Norma orang penting atau norma sosial pada kanker serviks merujuk pada harapan atau standar perilaku yang diterima oleh orang-orang di sekitar kita atau dalam kelompok sosial tertentu terkait dengan pencegahan atau deteksi dini kanker serviks.')
    st.write('9. norm_fulfillment (Pemenuhan Norma) = Istilah pemenuhan norma pada kanker serviks dapat merujuk pada sejauh mana seseorang atau suatu kelompok mematuhi atau memenuhi norma-norma sosial atau ekspektasi yang ada terkait dengan pencegahan, deteksi dini, atau tindakan lainnya terkait kanker serviks.')
    st.write('10. perception_vulnerability (Persepsi Kerentanan) = Persepsi kerentanan pada kanker serviks merujuk pada bagaimana seseorang menilai risiko atau rentan mereka terhadap pengembangan kanker serviks. Ini mencakup penilaian individu terhadap sejauh mana mereka merasa mungkin terpapar faktor risiko yang dapat menyebabkan kanker serviks.')
    st.write('11. perception_severity (Persepsi Keparahan) = Persepsi keparahan pada kanker serviks merujuk pada bagaimana seseorang menilai tingkat keparahan atau seriusnya konsekuensi yang dapat terjadi akibat kanker serviks.')
    st.write('12. motivation_strength (Kekuatan Motivasi) = Kekuatan motivasi pada kanker serviks merujuk pada intensitas atau tingkat dorongan internal yang mendorong individu untuk mengadopsi perilaku pencegahan atau deteksi dini terkait kanker serviks.')
    st.write('13. motivation_willingness (Kemauan Motivasi) = Kemauan dan motivasi pada kanker serviks merujuk pada keinginan dan dorongan seseorang untuk mengambil langkah-langkah pencegahan atau deteksi dini terkait dengan kanker serviks.')
    st.write('14. socialSupport_emotionality (Dukungan Sosial Emosionalitas) = Dukungan sosial emosionalitas pada kanker serviks merujuk pada bentuk dukungan sosial yang berkaitan dengan aspek emosional atau perasaan yang terlibat dalam menghadapi kanker serviks.')
    st.write('15. socialSupport_appreciation (Apresiasi Dukungan Sosial) = Apresiasi dukungan sosial untuk kanker serviks mengacu pada penghargaan dan pemahaman terhadap peran positif dan kontribusi dari dukungan sosial yang diterima oleh individu yang mengalami kanker serviks. ')
    st.write('16. socialSupport_instrumental (Dukungan Sosial Instrumental) = Dukungan sosial instrumental pada kanker serviks merujuk pada dukungan praktis atau tindakan nyata yang ditunjukkan oleh orang lain untuk membantu individu yang mengalami kanker serviks dalam situasi tertentu.')
    st.write('17. empowerment_knowledge (Pengetahuan Pemberdayaan) = Pengetahuan pemberdayaan untuk pencegahan kanker serviks merujuk pada pemahaman dan pengetahuan yang memberdayakan individu atau komunitas untuk mengambil langkah-langkah pencegahan yang efektif terhadap kanker serviks.')
    st.write('18. empowerment_abilities (Kemampuan Pemberdayaan) = Kemampuan pemberdayaan pada kanker serviks merujuk pada kapasitas individu atau komunitas untuk mengambil tindakan pencegahan atau mengelola risiko kanker serviks.')
    st.write('19. empowerment_desires (Keinginan Pemberdayaan) = Keinginan pemberdayaan pada kanker serviks merujuk pada dorongan atau motivasi individu untuk mencari pengetahuan, keterampilan, dan sumber daya yang dapat memberdayakan mereka untuk mengambil langkah-langkah pencegahan atau mengelola risiko kanker serviks.')
    st.write('20. ca_cervix (Deteksi Kanker Serviks) = ini adalah atribut kelas, yang dimana angka 1 adalah mengidap kanker serviks, dan angka 0 tidak ada kanker serviks')

if (selected == 'Implementasi') :
    st.title('Deteksi Kanker Serviks')
    st.write('Untuk mengetahui terdeteksi tidaknya Kanker Serviks mari isi kolom di bawah ini')
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        behavior_sexualRisk = st.number_input('Silahkan Masukkan Perilaku Seksual Resiko :')
        button = st.button('Detail', use_container_width = 500, type = 'primary')
        if button:
            if behavior_sexualRisk == 0:
                st.write('Perilaku seksual berisiko pada kanker serviks dapat mencakup praktek-praktek yang meningkatkan risiko terpapar human papillomavirus (HPV), yang merupakan penyebab utama kanker serviks. Kolom ini dapat diisi dengan rentang 1-10.')
            else:
                st.write('SILAHKAN BACA DESKRIPSI')
        behavior_eating = st.number_input('Silahkan Masukkan behavior_eating :')
        behavior_personalHygine = st.number_input('Silahkan Masukkan behavior_personalHygine :')
        intention_aggregation = st.number_input('Silahkan Masukkan intention_aggregation :')
        intention_commitment = st.number_input('Silahkan Masukkan intention_commitment :')
        attitude_consistency = st.number_input('Silahkan Masukkan attitude_consistency :')
        attitude_spontaneity = st.number_input('Silahkan Masukkan attitude_spontaneity :')
        norm_significantPerson = st.number_input('Silahkan Masukkan norm_significantPerson :')
        norm_fulfillment = st.number_input('Silahkan Masukkan norm_fulfillment :')
        perception_vulnerability = st.number_input('Silahkan Masukkan perception_vulnerability :')
    
    with col2:
        button = st.button('Detail', use_container_width = 500, type = 'primary')
        if button:
            if behavior_sexualRisk == 0:
                st.write('Perilaku seksual berisiko pada kanker serviks dapat mencakup praktek-praktek yang meningkatkan risiko terpapar human papillomavirus (HPV), yang merupakan penyebab utama kanker serviks. Kolom ini dapat diisi dengan rentang 1-10.')
            else:
                st.write('SILAHKAN BACA DESKRIPSI')

    with col3:
        perception_severity = st.number_input('Silahkan Masukkan perception_severity :')
        motivation_strength = st.number_input('Silahkan Masukkan motivation_strength :')
        motivation_willingness = st.number_input('Silahkan Masukkan motivation_willingness :')
        socialSupport_emotionality = st.number_input('Silahkan Masukkan socialSupport_emotionality :')
        socialSupport_appreciation = st.number_input('Silahkan Masukkan socialSupport_appreciation :')
        socialSupport_instrumental = st.number_input('Silahkan Masukkan socialSupport_instrumental :')
        empowerment_knowledge = st.number_input('Silahkan Masukkan empowerment_knowledge :')
        empowerment_abilities = st.number_input('Silahkan Masukkan empowerment_abilities :')
        empowerment_desires = st.number_input('Silahkan Masukkan empowerment_desires :')

    button = st.button('Cek Deteksi Cervical Cancer', use_container_width = 500, type = 'primary')

    if button:
        if behavior_sexualRisk !=0 and behavior_eating !=0 and behavior_personalHygine !=0 and intention_aggregation !=0 and intention_commitment !=0 and attitude_consistency !=0 and attitude_spontaneity !=0 and norm_significantPerson !=0 and norm_fulfillment !=0 and perception_vulnerability !=0 and perception_severity !=0 and motivation_strength !=0 and motivation_willingness !=0 and socialSupport_emotionality !=0 and socialSupport_appreciation !=0 and socialSupport_instrumental !=0 and empowerment_knowledge !=0 and empowerment_abilities !=0 and empowerment_desires !=0 :
            fitur = {"behavior_sexualRisk":behavior_sexualRisk,
                     "behavior_eating":behavior_eating,
                     "behavior_personalHygine":behavior_personalHygine,
                     "intention_aggregation":intention_aggregation,
                     "intention_commitment":intention_commitment,
                     "attitude_consistency":attitude_consistency,
                     "attitude_spontaneity":attitude_spontaneity,
                     "norm_significantPerson":norm_significantPerson,
                     "norm_fulfillment":norm_fulfillment,
                     "perception_vulnerability":perception_vulnerability,
                     "perception_severity":perception_severity,
                     "motivation_strength":motivation_strength,
                     "motivation_willingness":motivation_willingness,
                     "socialSupport_emotionality":socialSupport_emotionality,
                     "socialSupport_appreciation":socialSupport_appreciation,
                     "socialSupport_instrumental":socialSupport_instrumental,
                     "empowerment_knowledge":empowerment_knowledge,
                     "empowerment_abilities":empowerment_abilities,
                     "empowerment_desires":empowerment_desires,
                     }
            dt = pd.DataFrame(fitur,index=[0])
            import pickle
            with open('scaler.pkl','rb') as preprocessing:
                skala = pickle.load(preprocessing)
            data_normalisasi = skala.transform(dt) 
            st.write('---------- Data Hasil Normalisasi ----------')
            st.write(data_normalisasi)
            with open('PCA10.pkl','rb') as pca:
                pca =pickle.load(pca)
            data_pca = pca.transform(data_normalisasi)
            st.write('---------- Data Hasil Ekstraksi Fitur dengan PCA ----------')
            st.write(data_pca)
            with open('pca_knn.pkl','rb') as pcaknn :
                knn_pca = pickle.load(pcaknn)
            predict_pca = knn_pca.predict(data_pca)
            if predict_pca==0:
                st.write('Anda Tidak Terdeteksi Terkena Kanker Serviks')
            else:
                st.write('Anda Terdeteksi Terkena Kanker Serviks')
        else:
            st.write('SILAHKAN ISI KOLOM YANG KOSONG')
            
if (selected == 'Profil') :
    st.title('My Profile')
    st.write('Nama : Niswatul Sifa')
    st.write('NIM : 210411100145')
    st.write('Kelas : Proyek Sain Data (A)')
# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
from utils.phase_3_plot_df import get_cv_selected, get_branchs_linked_to_person, get_branchs_linked_to_many_persons, get_network_plot
from utils.c_similarity_between_cvs import tf_idf, tf_idf_list

data = pd.read_csv('utils/super_cleaned_df.csv')
data = data.drop(columns=['email', 'pdftext', 'location'])
pdf_list = data['id'].tolist()

st.set_page_config(layout='wide')

st.image('./images/logo_CV_matcher.png')
st.title('Extract and cluster information from a free-format resume')
st.markdown("Welcome to this dashboard for information extraction and matching of free-format resumes!")
st.write('\n ')
st.markdown("Data courtesy of [arefinnomi@github](https://github.com/arefinnomi/curriculum_vitae_data).")


st.markdown('---------')
st.header('CV selection')
cv_color = 1
st.write('\n')
st.write('\n')
col1, col_mid, col2 = st.beta_columns((3, 1, 3))
with col_mid:
    cv_color = st.text_input("Please input the CV_id number", cv_color)
    cv_color = int(cv_color)
st.markdown('---------')
st.header('Information extraction')
st.subheader('The table hereby shows the information extracted from the selected CV.')
st.write('\n')
st.write('\n')
st.write('\n')
col1, col_mid, col2 = st.beta_columns((1, 3, 1))
with col_mid:
    st.subheader('Information from cv_input:')    
    data_branch = get_cv_selected(data, [cv_color])
    st.dataframe(data_branch.T)
   
st.markdown('---------')
st.header('Results')
col1, col_mid, col2 = st.beta_columns((1, 1, 1))
with col_mid:
    refresh_plot = st.button('refresh', key='key0')    
    if refresh_plot:    
        plt_ten, ten_cv_selected= tf_idf(data, filenumber=cv_color, subsetoption=False, filteringsection='academic_titles', similaritysection='work_experience2', scattersection='hobbies')
        st.pyplot(plt_ten)

col_mid, col1, col_mid, col3, col_mid = st.beta_columns((0.7, 2, 0.1, 2, 0.7))
with col1:
    st.subheader('This is the network for the CV selected:')
    refresh_net_cv = st.button('refresh', key='key1')    
    if refresh_net_cv:
        cv_selected=[cv_color]
        academic_titles_cv_selected_list = []
        work_experience_cv_selected_list = []
        data_branch = get_cv_selected(data, [cv_color])
        data_nodes_cv_selected, academic_titles_cv_selected_list, work_experience_cv_selected_list = get_branchs_linked_to_person(data_branch, [cv_color])
        # data_nodes_cv_1_2, academic_titles_list_cv_1_2, work_experience_list_cv_1_2 = get_branchs_linked_to_many_persons(data, cv_selected=[cv_color, 32])    
        plot_cv_selected = get_network_plot([cv_color], data_nodes_cv_selected, academic_titles_cv_selected_list, work_experience_cv_selected_list)    
        st.pyplot(plot_cv_selected)
with col3:
    st.subheader('This is the network for the CV selected and the firts similar CV:')
    refresh_net_cv_1_2 = st.button('refresh', key='key2')    
    if refresh_net_cv_1_2:
        ten_cv_selected= tf_idf_list(data, filenumber=cv_color, subsetoption=False, filteringsection='academic_titles', similaritysection='work_experience2', scattersection='hobbies')
        data_nodes_cv_1_2, academic_titles_list_cv_1_2, work_experience_list_cv_1_2 = get_branchs_linked_to_many_persons(data, [cv_color, ten_cv_selected[0]])    
        plot_cv_1_2 = get_network_plot([cv_color, ten_cv_selected[0]], data_nodes_cv_1_2, academic_titles_list_cv_1_2, work_experience_list_cv_1_2)    
        st.pyplot(plot_cv_1_2)

st.markdown('---------')

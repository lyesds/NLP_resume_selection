# -*- coding: utf-8 -*-
"""
@author: HZU
"""

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('super_cleaned_df.csv')
cv_selected = [915, 295, 408, 2774]

def get_cv_selected(data, cv_selected):
    data_branch = data.loc[data['id'].isin(cv_selected)]
    data_branch = data_branch[['id','academic_titles', 'work_experience']]
    data_branch.reset_index(drop=True, inplace=True)
    data_branch['academic_titles'] = data_branch['academic_titles'].replace('this person do not have academic titles','no_acad')
    data_branch['work_experience'] = data_branch['work_experience'].replace('this person do not have listed work experience', 'no_worexp')
    return data_branch


def get_branchs_linked_to_person(data, cv_selected):
    """
    All the output is linked to the person
    Returns
    -------
    q : df with root and leaf.
    m : acad titles list.
    n : w. exp names list.
    """
    q = pd.DataFrame()
    q['root'] = 'root'
    q['leaf'] = 'leaf'
    for i in range(len(data)):
        m = data['academic_titles'][i].split(", ")
        n = data['work_experience'][i].split(", ")
        # for p in range(len(m)):
        #     for j in range(len(n)):
        #         q = q.append({'root':m[p], 'leaf':n[j]}, ignore_index=True )
    for p in range(len(cv_selected)):
        for j in range(len(m)):
            q = q.append({'root':int(cv_selected[p]), 'leaf':m[j]}, ignore_index=True )
    for p in range(len(cv_selected)):
        for j in range(len(n)):
            q = q.append({'root':int(cv_selected[p]), 'leaf':n[j]}, ignore_index=True )
    q['root'] = q['root'].astype(str)
    q['leaf'] = q['leaf'].astype(str)
    return q, m, n

def get_branchs_linked_to_many_persons(data, cv_selected):
    """
    All the output is linked to the person
    Returns
    -------
    data_nodes : df with root and leaf.
    m : acad titles list.
    n : w. exp names list.
    """
    data_nodes = pd.DataFrame()
    data_nodes['root'] = 'root'
    data_nodes['leaf'] = 'leaf'
    m_total =[]
    n_total =[]
    for i in range(len(cv_selected)):
        item = cv_selected[i]
        data_test = data.loc[data['id']== item]
        data_test.reset_index(drop=True, inplace=True)        
        m = data_test['academic_titles'][0].split(", ")
        n = data_test['work_experience'][0].split(", ")
        m_total.append(m)
        n_total.append(n)
        for j in range(len(m)):
            data_nodes = data_nodes.append({'root':int(item), 'leaf':m[j]}, ignore_index=True )
        for j in range(len(n)):
            data_nodes = data_nodes.append({'root':int(item), 'leaf':n[j]}, ignore_index=True )
        m = []
        n = []
    data_nodes['root'] = data_nodes['root'].astype(str)
    data_nodes['leaf'] = data_nodes['leaf'].astype(str)
    m_total = [item for sublist in m_total for item in sublist]
    n_total = [item for sublist in n_total for item in sublist]
    return data_nodes, m_total, n_total

def get_network_plot(cv_selected, data_nodes, academic_titles_list, work_experience_list):
    for i in range(len(cv_selected)):
        cv_selected[i]= str(cv_selected[i])

    G = nx.Graph()
    for i in range(len(data_nodes)):
        G.add_edge(data_nodes['root'][i],data_nodes['leaf'][i])

    color_map = []
    for node in G:
        if node in academic_titles_list:
            color_map.append('orange')
        elif node in cv_selected:
            color_map.append('red')
        else:
            color_map.append('blue')

    nx.draw(G, node_color=color_map, with_labels = True, verticalalignment='bottom', arrowsize=3)
    # nx.draw(G, node_color=color_map, with_labels = True, node_size=1000)
    plt.show()

data = get_cv_selected(data, cv_selected)
data_nodes, academic_titles_list, work_experience_list = get_branchs_linked_to_person(data, cv_selected=[915])
data_nodes, academic_titles_list, work_experience_list = get_branchs_linked_to_many_persons(data, cv_selected)
get_network_plot(cv_selected, data_nodes, academic_titles_list, work_experience_list)




















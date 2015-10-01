__author__ = 'yangxiaofeng'
from igraph import *

def regular_stat(G):
    dict_of_features = dict()
    dict_of_features["number_of_edges"] = G.ecount()
    dict_of_features["average_path_l"] = G.average_path_length(directed=False, unconn=True)
    dict_of_features["density"] = G.density()
    dict_of_features["diameter"] = G.diameter(directed=False, unconn=True, weights=None)
    dict_of_features["girth"] = G.girth()
    return dict_of_features
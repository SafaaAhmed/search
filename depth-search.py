#!/usr/bin/env python
# coding: utf-8

# In[1]:


adj_list ={'a':['b','c'],
           'b':['d','e'],
           'c':['b','f'],
           'd':[],
           'e':['f'],
           'f':[]
    
}

color={}
parent={}
traverse_time={}
dfs_traversal_output=[]
for node in adj_list.keys():
    color[node]='w'
    parent[node]=None
    traverse_time[node]=[-1,-1]

print(color)
print(parent)
print(traverse_time)
{'a': 'w', 'b': 'w', 'c': 'w', 'd': 'w', 'e': 'w', 'f': 'w'}
{'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None}
{'a': [-1, -1], 'b': [-1, -1], 'c': [-1, -1], 'd': [-1, -1], 'e': [-1, -1], 'f': [-1, -1]}
time=0
def dfs(u):
    global time 
    color[u]='g'
    traverse_time[u][0]=time
    dfs_traversal_output.append(u)
    for v in adj_list[u]:
        if color[v]=='w':
            parent[v]=u
            dfs(v)
    color[u]='b'
    traverse_time[u][1]=time
    time+=1
dfs('a')
print(parent)
print(traverse_time)
print(dfs_traversal_output)
for node in adj_list.keys():
    print(node,"->",traverse_time[node])


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[168]:


group=[[None]*4]*8
group_country_name=[[None]*4]*8

f=open("data.csv","r")
data=f.read()
data=data.split("\n")[1:]
data=data[:32]
k=0
for teams in data:
    x=teams.split(',')
    y=x[0].split('(')
    team_name=y[0].split('.')[-1][1:]
    country_name=y[-1][:3] 
    if x[-1]=='1':
        #print(team_name,country_name,k)
        z=group[k].copy()
        z1=group_country_name[k].copy()
        z[0]=team_name
        z1[0]=country_name
        group[k]=z
        group_country_name[k]=z1
        k+=1
#print(group)
#print(group_country_name)
for teams in data:
    x=teams.split(',')
    y=x[0].split('(')
    team_name=y[0].split('.')[-1][1:]
    country_name=y[-1][:3]
    f=0
    if x[-1]=='0':
        for i in range(8):
            if country_name not in group_country_name[i]:
                for j in range(4):
                    if group[i][j]==None:
                        #print(team_name,country_name,k)
                        z=group[i].copy()
                        z1=group_country_name[i].copy()
                        z[j]=team_name
                        z1[j]=country_name
                        group[i]=z
                        group_country_name[i]=z1
                        #print(group[i])
                        f=1
                        break
                if f==1:
                    break
                    

                        
                
            
for i in range(8):
    print("Group ",i+1)
    print()
    for j in range(4):
        print(group[i][j])
    print()
    print()


# In[59]:


if x[-1]=='1':
        #print(group)
        print(team_name,country_name)
        print()
        for i in range(8):
            if len(group[i][0][0])==0:
                group[i]['name']=team_name
                group[i]["country"]=country_name
                break


# In[138]:


l=[1,2,3,44,5]
for i in range(5):
    #print(i)
    if(44 not in l):
        print("f")
    


# In[ ]:


x=[3m]


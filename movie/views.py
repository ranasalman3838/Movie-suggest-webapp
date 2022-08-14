from django.shortcuts import render
from django.shortcuts import render,redirect
import  pandas as pd
import random

# Create your views here.

def start(request):
    return render(request,'initialPage.html')

def index(request):
    return render(request,'index.html')

def final(request):
    return render(request,'finalPage.html')

def movies(request):
    
    #romantic movies data 
    f=open('Romance.csv')
    data= f.read().split('\n')[1:-1]
    lines=[]    
    for line in data :
        token=line.split(',')        
        d={'title':token[1],'year':token[2],'time':token[3],'genre':token[4],'rating':token[5],'image':token[6]}
        
        d['image']=d['image'].replace('"','')
        lines.append(d)    
    lines=random.sample(lines, 5)

     #Comedy movies data 
    f=open('Comedy.csv')
    data= f.read().split('\n')[1:-1]
    lines2=[]
    
    for line in data :
        token=line.split(',')        
        d={'title':token[1],'year':token[2],'time':token[3],'genre':token[4],'rating':token[5],'image':token[6]}
        d['image']=d['image'].replace('"','')
        lines2.append(d)    
    lines2=random.sample(lines2, 5)

     #Thrilller movies data 
    f=open('Action.csv')
    data= f.read().split('\n')[1:-1]
    lines3=[]    
    for line in data :
        token=line.split(',')        
        d={'title':token[1],'year':token[2],'time':token[3],'genre':token[4],'rating':token[5],'image':token[6]}
        d['image']=d['image'].replace('"','')
        lines3.append(d)
    lines3=random.sample(lines3, 5)

     #Horror movies data 
    f=open('Horror.csv')
    data= f.read().split('\n')[1:-1]
    lines4=[]    
    for line in data :
        token=line.split(',')        
        d={'title':token[1],'year':token[2],'time':token[3],'genre':token[4],'rating':token[5],'image':token[6]}
        d['image']=d['image'].replace('"','')
        lines4.append(d)    
    lines4=random.sample(lines4, 5)   
     
    context={'lines':lines,'lines2':lines2,'lines3':lines3, 'lines4':lines4}
    return render(request,'movies.html',context)

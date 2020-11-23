import pandas as pd

a=[]
data=pd.read_csv('hotels.csv')



#please type exactly either Karnataka,Maharashtra,Tamilnadu,India for value of state 
s=input("What is the state:")

#please type exactly either cost or rating 
c=input("Cost/rating:")

#please type either highest,least or average for operation
o=input("Operation:")

if s=="India":
  if c=="cost":

    if o=="highest":
      m=data['Cost'].min()
      d=data[data['Cost']==m]
 
      print("Hotel with highest price in India is")
      for i in d['Hotel Code']:
        print("{} with price{}".format(i,m))
    
    if o=="cheapest":
      m=data['Cost'].min()
      d=data[data['Cost']==m]
 
      print("Hotel with highest price in India is")
      for i in d['Hotel Code']:
        print("{} with price{}".format(i,m))
    
    if o=="average":
      for i in data['Cost']:
        if i not in a:
          a.append(i)
        
      a.sort()
      l=len(a)
      m=a[int(l/2)]

      df=data[data['Cost']==m]
      print("Hotel with average cost in India is")
      for i in df['Hotel Code']:
        print("{} with price {}".format(i,m))

 


  elif c=='rating':
    if o=='highest':
      m=data['Ratings'].max()
      df=data[data['Ratings']==m]

      print("Hotel with highest rating in India is")
      for i in df['Hotel Code']:
        print("{} with rating {}".format(i,m))

    elif o=='least':
      m=data['Ratings'].min()
      df=data[data['Ratings']==m]

      print("Hotel with highest rating in India is")
      for i in df['Hotel Code']:
        print("{} with rating {}".format(i,m))

    elif o=='average':
      for i in data['Ratings']:
        a.append(i)
      
      a.sort()
      l=len(a)
      m=a[int(l/2)]

      df=data[data['Ratings']==m]
      print("Hotel with average rating in India is")
      for i in df['Hotel Code']:
        print("{} with rating {}".format(i,m))



  

      

     






elif s=="Karnataka" :
  if c=="cost":
    if o=="highest":
      df=data[data['State']=='Karnataka']
      m=df['Cost'].max()
      df=df[df['Cost']==m]
  

      print("Hotel with highest price in Karnataka is")
      for i in df['Hotel Code']:
        print("{} with price {}".format(i,m))
    
    elif o=="least":
      df=data[data['State']=='Karnataka']
      m=df['Cost'].min()
      df=df[df['Cost']==m]
  

      print("Hotel with average price in Karnataka is")
      for i in df['Hotel Code']:
        print("{} with price {}".format(i,m))

    elif o=="average":
      df=data[data['State']=='Karnataka']
      for i in df['Cost']:
        if i not in a:
          a.append(i)
      a.sort()
      l=len(a)
      m=a[int(l/2)]
      df=df[df['Cost']==m]

      
  

      print("Hotel with average price in Karnataka is")
      for i in df['Hotel Code']:
        print("{} with price {}".format(i,m))
  
  elif c=='rating':
    if o=='highest':
      df=data[data['State']=='Karnataka']
      m=df['Ratings'].max()
      df=df[df['Ratings']==m]

      print("Hotel with highest rating in Karnataka is")
      for i in df['Hotel Code']:
        print("{} with rating {}".format(i,m))  
    
    if o=="least":
      df=data[data['State']=='Karnataka']
      m=df['Ratings'].min()
      df=df[df['Ratings']==m]

      print("Hotel with lowest rating in Karnataka is")
      for i in df['Hotel Code']:
        print("{} with rating {}".format(i,m))  
    

    if o=="average":
      df=data[data['State']=='Karnataka']
      for i in df['Ratings']:
        if i not in(a):
          a.append(i)
      a.sort()
      l=len(a)
      m=a[int(l/2)]

      df=df[df['Ratings']==m]

      print("Hotel with average rating in Karnataka is")
      for i in df['Hotel Code']:
        print("{} with rating {}".format(i,m))  
    





elif s=="Tamilnadu" :
  if c=='cost':
    if o=='highest':
      df=data[data['State']=='Tamilnadu']
      m=df['Cost'].max()
      df=df[df['Cost']==m]
      print("Hotel with highest price in India is")
      for i in df['Hotel Code']:
        print("{} with price {}".format(i,m))
    
    elif o=='least':
      df=data[data['State']=='Tamilnadu']
      m=df['Cost'].min()
      df=df[df['Cost']==m]
      
      print("Hotel with lowest price in Tamilnadu is")
      for i in df['Hotel Code']:
        print("{} with price {}".format(i,m))
    
    elif o=='average':
      df=data[data['State']=='Tamilnadu']
      for i in df['Cost']:
        if i not in (a):
          a.append(i)
      a.sort()
      l=len(a)
      m=a[int(l/2)]
      df=df[df['Cost']==m]

      print("Hotel with average price in Tamilnadu is")
      for i in df['Hotel Code']:
        print("{} with price {}".format(i,m))

  elif c=="rating":
    if o=='highest':
      df=data[data['State']=='Tamilnadu']
      m=df['Ratings'].max()
      df=df[df['Ratings']==m]

      print("Hotel with highest rating in Tamilnadu is")
      for i in df['Hotel Code']:
        print("{} with rating {}".format(i,m))  
    
    elif o=='least':
      df=data[data['State']=='Tamilnadu']
      m=df['Ratings'].min()
      df=df[df['Ratings']==m]

      print("Hotel with least rating in Tamilnadu is")
      for i in df['Hotel Code']:
        print("{} with rating {}".format(i,m))  

    elif o=='average':
      df=data[data['State']=='Tamilnadu']

      for i in df['Ratings']:
        if i not in (a):
          a.append(i)
      a.sort()
      l=len(a)
      m=a[int(l/2)]
      df=df[df['Ratings']==m]

      print("Hotel with average rating in Tamilnadu is")
      for i in df['Hotel Code']:
        print("{} with rating {}".format(i,m))

    
    



  




elif s=="Maharashtra":
  if c=="cost":
    if o=="highest":
      df=data[data['State']=='Maharashtra']
      m=df['Cost'].max()
      df=df[df['Cost']==m]
  

      print("Hotel with highest price in Maharashtra is")
      for i in df['Hotel Code']:
        print("{} with price {}".format(i,m))
      
    elif o=="least":
      df=data[data['State']=='Maharashtra']
      m=df['Cost'].min()
      df=df[df['Cost']==m]
  

      print("Hotel with Cheapest price in Maharashtra is")
      for i in df['Hotel Code']:
        print("{} with  {}".format(i,m))

    elif o=="average":
      df=data[data['State']=='Maharashtra']
      for i in df['Cost']:
        if i not in a:
          a.append(i)
      a.sort()
      l=len(a)
      m=a[int(l/2)]
      df=df[df['Cost']==m]
  

      print("Hotel with average price in Maharashtra is")
      for i in df['Hotel Code']:
        print("{} with price {}".format(i,m))

  if c=="rating":
    if o=='highest':
      df=data[data['State']=='Maharashtra']
      m=df['Ratings'].max()
      df=df[df['Ratings']==m]

      
      print("Hotel with highest rating in Maharashtra is")
      for i in df['Hotel Code']:
        print("{} with price {}".format(i,m))
    
    if o=='least':
      df=data[data['State']=='Maharashtra']
      m=df['Ratings'].min()
      df=df[df['Ratings']==m]

      
      print("Hotel with least rating in Maharashtra is")
      for i in df['Hotel Code']:
        print("{} with rating {}".format(i,m))
  

    if o=='average':
      df=data[data['State']=='Maharashtra']
      for i in df['Ratings']:
        if i not in a:
          a.append(i)

      a.sort()
      print(a)
      l=len(a)

      m=a[int(l/2)]
      df=df[df['Ratings']==m]

      
      print("Hotel with average rating in Maharashtra is")
      for i in df['Hotel Code']:
        print("{} with rating {}".format(i,m))

  


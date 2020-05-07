import pandas as ps

#Example for slicing
'''
xyz_fram ={'Days':[1,2,3,4,5,6],"Visitors":[1000,700,300,4000,400,5000],"Bounce_rate":[20,30,25,15,30,50]}

df =ps.DataFrame(xyz_fram)
#Its prints total data frame
#print(df)

#Below command prints first few lines of dataframe
print(df.head(3))

#Below command prints last few lines of dataframe
print(df.tail(3))
'''

#Example for Merge
'''
df1 = ps.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,4],"Ind_GDP":[45,56,65,78]},index=[2001,2002,2003,2004])
df2 = ps.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,4],"Ind_GDP":[45,56,65,78]},index=[2005,2006,2007,2008])

mrg = ps.merge(df1,df1,on= 'HPI')
print(mrg)

'''
#Example for joining data
df1 = ps.DataFrame({"Int_rate1":[2,1,2,4],"Ind_GDP1":[45,56,65,78]},index=[2001,2002,2003,2004])
df2 = ps.DataFrame({"Int_rate2":[2,1,2,4],"Ind_GDP2":[45,56,65,78]},index=[2001,2003,2004,2005])

#joined = df1.join(df2)

joined = df2.join(df1)

print(joined)



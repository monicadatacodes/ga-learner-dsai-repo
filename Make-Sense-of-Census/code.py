# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]


#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print ("Reading the file \n")
print (data)
#Code starts here

c= np.array(new_record)

#Appending new record to data variable
census = np.concatenate((data,c),axis =0)

#After adding the new row into the data 
print('Census now is \n') 
print (census)
print('\n')
print (' Shape of the data file is' ,np.shape(data))
print('Shape of census is' , np.shape(census))


#Analysis of Age distribution

age = census[:,0]
print(age)
print(type(age))
max_age = age.max()
min_age = age.min()
print('Max age : ' , max_age)
print('Min age : ' , min_age)
age_mean = age.mean()
print('Mean age is ', age_mean)
age_std = np.std(age)
print(' Standard deviatin of age is ', age_std)


#Creating new subsets based on 'Age'
cen= census[:,2]
race_0 = cen[cen==0]
race_1 = cen[cen==1]
race_2 = cen[cen==2]
race_3 = cen[cen==3]
race_4 = cen[cen==4]

#Finding the length of the above created subsets
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)




#Printing the length of the above created subsets
print('Race_0: ', len_0)
print('Race_1: ', len_1)
print('Race_2: ', len_2)
print('Race_3: ', len_3)
print('Race_4: ', len_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]

#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))    


#Subsetting the array based on the age 
senior_citizens = census[census[:,0]>60]

#Calculating the sum of all the values of array
working_hours_sum = np.sum(senior_citizens[:,6], axis=0)
print(working_hours_sum)

#total senior citizens
senior_citizens_len = len(senior_citizens)
print('\n Total Senior citizens are ' , senior_citizens_len )

#Average working hours of senior citizens
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)

print(' The govt policy is not been followed for the senior citizens here as average working hours exceed 25')

#Finding whether the higher educated people have better pay
high = census[census[:,1]>10]
low = census[census[:,1]<10]

avg_pay_high = np.mean(high[:,7],axis =0)
avg_pay_low = np.mean(low[:,7])
avg_pay_low +=0.01
print('\n Average High Salary : ',round(avg_pay_high,2))
print('\n Average Low Salary : ',round(avg_pay_low,2))








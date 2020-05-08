# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here
#Creating a new variable to store the value counts
loan_status = data['Loan_Status'].value_counts()

print(loan_status)

#Plotting bar plot
plt.figure(figsize=[10,6])

# label the axes
plt.xlabel("Loan Status")
plt.ylabel("No of Loans")

# title the plot
plt.title("loans vs loan status ")

loan_status.plot(kind = 'bar')
# bar chart

plt.show()


# Step 2
#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area' ,'Loan_Status']).size().unstack()

property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
# Label X-axes and Y-axes
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
# Rotate X-axes labels
plt.xticks(rotation=45)
# Display plot
plt.show()


# Step 3
#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education' ,'Loan_Status']).size().unstack()

education_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))
# Label X-axes and Y-axes
plt.xlabel('Education')
plt.ylabel('Loan Status')
# Rotate X-axes labels
plt.xticks(rotation=45)
# Display



#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education'] == 'Graduate']

#Subsetting the dataframe based on 'Education' column
not_graduate= data[data['Education'] == 'Not Graduate']

#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind = "density", label = "Graduate")
not_graduate['LoanAmount'].plot(kind = "density", label = "Not Graduate")

#For automatic legend display


# Step 5
#Setting up the subplots
fig ,(ax_1,ax_2,ax_3) = plt.subplots(3,1, figsize=(15,8))

#Plotting scatter plot

data.plot.scatter(x='ApplicantIncome', y='LoanAmount')
ax_1.set_title('Applicant Income')
plt.show()
#Setting the subplot axis title
data.plot.scatter(x='CoapplicantIncome', y='LoanAmount')
ax_2.set_title('Coapplicant Income')
plt.show()

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
data.plot.scatter(x='TotalIncome', y='LoanAmount')
ax_3.set_title('Total Income')
plt.show()
#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title




# --------------
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:43:01 2020

@author: Dell
"""


# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
bank = pd.DataFrame(bank_data)
# print(bank.head())
# print(bank.columns)

categorical_var =bank.select_dtypes(include ='object')
print(" All non- numerical columns")
print('=========================================')
print(categorical_var)
print('=========================================')

print(" All Numerical columns")
numerical_var =bank.select_dtypes(include ='number')
print(numerical_var)

banks = bank.drop('Loan_ID', axis=1)
print(' After dropping Loan Id')
print(banks.head())

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #Checking for null values
print("Checking for null values")
print(banks.isnull().sum())

bank_mode = banks.mode()
print(' Bank mode')
print(bank_mode.head())

#banks = banks.fillna(bank_mode)   ##This code is not working
banks = banks.fillna(bank_mode.iloc[0]) ###This is working why?

print(banks.shape)  
c= banks.isnull().sum().values.sum()
print(c)



avg_loan_amount = banks.pivot_table(index = ['Gender', 'Married', 'Self_Employed'], values = 'LoanAmount', aggfunc ='mean')
print(avg_loan_amount)

loan_approval_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].count()
print(loan_approval_se)
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].count()
print(loan_approved_nse)
Loan_Status =614
percentage_se = (loan_approval_se/Loan_Status)*100
print(round(percentage_se,2))
percentage_nse = (loan_approved_nse/Loan_Status)*100
print(round(percentage_nse,2))

loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)
print(loan_term)

big_loan_term= loan_term[loan_term>=25].count()
print(big_loan_term)

loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]
mean_values =loan_groupby.mean()
print(round(mean_values,2))



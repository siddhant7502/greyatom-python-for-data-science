# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data)
print(data.shape)
#Code starts here
census=np.concatenate((new_record,data))
print(census.shape)

age=np.array(census[:,0])
max_age=np.max(age)
print(max_age)
min_age=np.min(age)
print(min_age)
age_mean=np.mean(age)
print(age_mean)
age_std=np.std(age)
print(age_std)

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

len_0=len(race_0)
print(len_0)
len_1=len(race_1)
print(len_1)
len_2=len(race_2)
print(len_2)
len_3=len(race_3)
print(len_3)
len_4=len(race_4)
print(len_4)

list_count=[len_0,len_1,len_2,len_3,len_4]
minority_race=list_count.index(min(list_count))
print(minority_race)

senior_citizen=census[census[:,0]>60]
working_hours_sum=senior_citizen.sum(axis=0)[6]
senior_citizen_len=len(senior_citizen)

avg_working_hours=working_hours_sum/senior_citizen_len
print(avg_working_hours)

high=census[census[:,1]>10]
low=census[census[:,1]<=10]

avg_pay_high=high.mean(axis=0)[7]
avg_pay_low=low.mean(axis=0)[7]
print(avg_pay_high)
print(avg_pay_low)




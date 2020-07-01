import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("store_report.csv")

df['Weekly_Sales'] =df['Weekly_Sales'].astype('int32')


df['month'] = df['Date'].str[3:5]
df['month'] = df['month'].astype("int32")
df.to_csv("sales.csv",index = False)
#print(df['month'])

#General Question : Which month is Good for Sales?

month =df.groupby('month').sum()
print(month)

months =range(1,13)
plt.bar(months,month['Weekly_Sales'])

plt.xlabel("Months")
plt.ylabel("Sales")
plt.xticks(months)
plt.title('Best Month For Sales')
plt.grid()
plt.show()
print("-------------------------------------")

#General Question : Maximum sales done in a month of the year?

print("Max Sales in a month of  year:",max(df.groupby('month').sum()['Weekly_Sales']))

print("-------------------------------------")

# General Question : Overall Sales in Non - Holiday weeks and Holiday Weeks?
holiday = df.groupby('IsHoliday').sum()
#print(holiday)

leave = df['IsHoliday'].unique()
plt.bar(leave , holiday['Weekly_Sales'],label =("not-Holiday"),color=("g","b"))
plt.xlabel("IsHoliday")
plt.ylabel('Sales')
plt.xticks(leave)
plt.legend()
plt.yticks(holiday['Weekly_Sales'])
plt.title("Sales vs Holiday(Weekly)")
plt.show()

#General Question : Which store is best among 45 Stores?

Store =range(1,46)
#print(Store)
store =df.groupby('Store').sum()
#print(store)

plt.bar(Store,store['Weekly_Sales'],)
plt.xlabel("Store")
plt.ylabel("Weekly_Sales")
plt.title("Best store")
plt.xticks(range(1,46),rotation ="vertical",size = 8)
plt.grid()
plt.show()

#General Question : Which Dept in the Store performs Good?

dept = df.groupby('Dept').sum()
#print(dept)
depts =df['Dept'].unique()
plt.bar(depts,dept['Weekly_Sales'])
plt.xlabel("Dept")
plt.title("Best_Dept")
plt.ylabel("Sales")
plt.grid()
plt.xticks(range(1,99),rotation='vertical',size =2)
plt.show()

#General Question : In which Month is worst?
print("min sale of month :", min(df.groupby('month').sum()['Weekly_Sales']))
print(" This Sales is not good as jan was the start of the year")
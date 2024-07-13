


#1.First we have to take input from user
#2.Then we have to know about the user per day expense 
#by entering the per day expense from users
#3.We have to calculate the per day total expense
#4.Then we will calculate the total expense.

#First we will take input number of days from user
numberOfDays=int(input("Enter number of days: "))

#input number of expense on each day
total_expense=0
each_day_expense=[]

for i in range(numberOfDays):
    day_expense=0
    price_list_per_day=input("Enter prices seperated by space : ").split(' ')
    #we will find how much expense has done by user 
    for expense in price_list_per_day:
        total_expense=total_expense+ int(expense)
        #Total_expense will store total money the user spend 
        #for shopping
        day_expense=day_expense+int(expense)
        #We will store per day expense in each_day_expense list
    each_day_expense.append(day_expense)
 
print(each_day_expense)
for day in range(len(each_day_expense)):
    print("Day",day+1,":",each_day_expense[day])
    #in above step we are printing each day total expense

print("Total: ",total_expense)

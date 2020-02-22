def monthcheck(month):
        if month > 0 and month <= 12:
            return True
        else:
            return False
def daycheck(month,day,year):
    monthlist1 = [1,3,5,7,8,10,12] 
    monthlist2 = [4,6,9,11] 
    monthlist3 = 2 
    for mon in monthlist1:
        if month == mon: 
            if day >=1 and day <= 31: 
                return True
            else:
                return False
    for mon in monthlist2:
        if month == mon:
            if day >= 1 and day <= 30: 
                return True
            else:
                return False
    if month == monthlist3: 
        if(year % 4)==0:
            if(year % 100)==0:
                if(year % 400)==0:
                    if day >=1 and day <= 29: 
                        return True
                    else:
                        return False
                else:
                    if day >=1 and day <= 28: 
                        return True
                    else:
                        return False
            else:
                if day >=1 and day <= 29: 
                    return True
                else:
                    return False
        else:
            if day >=1 and day <= 28: 
                return True
            else:
                return False
      
def yearcheck(year):
    if len(year) >= 1 and len(year) <= 4: 
        return True
    else:
        return False
def main():
    date = str(input("Enter the date in mm/dd/yyyy format: ")) ## Input date in the given format.
    month,day,year = date.split("/") 
    monthvalidity = monthcheck(int(month))
    dayvalidity = daycheck(int(month),int(day),int(year))
    yearvalidity = yearcheck(year)
   
    currentDate="02/22/2020" ##Hard code the date as built-in functions are prohibited
    currentMonth,currentDay,currentYear=currentDate.split("/")
    # print(currentDay)
    # print(currentMonth)
    # print(currentYear)
    # print(day)
    # print(month)
    # print(year)
    if monthvalidity == True and dayvalidity == True and yearvalidity == True :## check if all 3 variables are valid or True
        if((int(currentDay)<int(day) and int(currentMonth)==int(month) and int(currentYear)==int(year)) or
            (int(currentDay)>=int(day) and int(currentMonth)<int(month) and int(currentYear)<=int(year)) or
            (int(currentDay)>=int(day) and int(currentMonth)>=int(month) and int(currentYear)<int(year)) or
            (int(currentDay)<int(day) and int(currentMonth)>=int(month) and int(currentYear)<int(year)) or
            (int(currentDay)>=int(day) and int(currentMonth)<int(month) and int(currentYear)<int(year)) or
            (int(currentDay)<int(day) and int(currentMonth)<int(month) and int(currentYear)<int(year))):
                print("1.The date {0} is invalid.".format(date))
        else:
            print("The date {0} is valid.".format(date))
    else:
            print("2.The date {0} is invalid.".format(date))
main()

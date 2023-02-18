year = int(input("Введите год:"))
if(year%4==0):
    february=29
    months =["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    countdays=[31, february, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
    def Digits(n):
        Digit=0
        while n!=0:
            Digit += n%10
            n=n//10
        return Digit
    daysinyear = 0
    for i in range(12):
        alldays= 0
        for a in range(countdays[i]+1):
            alldays += Digits(a)
        daysinyear += alldays
    print(f"Количество дней в году:{daysinyear}")
else:
    february=28
    months =["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    countdays=[31, february, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
    def Digits(n):
        Digit=0
        while n!=0:
            Digit += n%10
            n=n//10
        return Digit
    daysinyear = 0
    for i in range(12):
        alldays= 0
        for a in range(countdays[i]+1):
            alldays += Digits(a)
        daysinyear += alldays
    print(f"Количество дней в году:{daysinyear}")

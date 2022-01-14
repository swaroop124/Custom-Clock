import datetime
import pyttsx3
from playsound import playsound
import time
import calendar
from datetime import date

speaker=pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id) #changing index changes voices but ony 0 and 1 are working here
#Changing the index from 0 or 1 changes the voice.0 is male voice and 1 is for female voice


def set_timer(n):#Here n is no of seconds
    while n>1:
      speaker.say(n)  
      speaker.runAndWait()
      print(n)
      n=n-1
    if n==1:
        playsound(r'C:\Users\Swaroop\Desktop\twirling-intime-lenovo-k8-note-alarm-tone-41440.mp3')#Plays sound 
        speaker.say("times up!")
        speaker.runAndWait()
        print(n)
        print("times up!")
      
def set_alram(h,m,form):
    if form=="pm" or form=="PM":
        h=h+12
    while(1==1):
      if(h==datetime.datetime.now().hour and m==datetime.datetime.now().minute):
        playsound(r'C:\Users\Swaroop\Desktop\music_box_ringtone.mp3')
        speaker.say("wake up boy")                                              
        speaker.runAndWait()
        print("Times Up")  
        break   #This plays the song only once 
        
def get_age(cd,cm,cy):
          dt = datetime.datetime.now()
          selfday1=dt.day
          selfmonth1=dt.month
          selfyr1=dt.year
          a=0
          b=0
          c=0
          dlp={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:30,9:31,10:30,11:31,12:30}#FOR Leap Year
          dnp={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:30,9:31,10:30,11:31,12:30}#FOR NON LEAP YEAR
          #We split into three conditions here ie. when current month is less than,equal to and greater than the given month
          #a is the no of years,b is the no of months and c indicates the days.
          if selfmonth1<cm:
               a=selfyr1-cy-1
               if selfday1>cd:
                 b=12-cm+selfmonth1
                 c=selfday1-cd
               else:
                 b=12-cm+selfmonth1-1
                 if( cy%4==0):
                    if selfmonth1==1:
                       c=31-cd+selfday1  
                    else:
                       c=dlp[selfmonth1-1]-cd+selfday1
                 else:
                     if selfmonth1==1:
                       c=31-cd+selfday1  
                     else:
                       c=dnp[selfmonth1-1]-cd+selfday1
               speaker.say(a)
               speaker.say("year")
               speaker.say(b)
               speaker.say("month")
               speaker.say(c)
               speaker.say("days")
               speaker.runAndWait()
               return(str(str(a)+" "+"year"+" "+str(b)+" "+"month"+" "+str(c)+" "+"days"))
          elif selfmonth1==cm:
              if(selfyr1==cy):
                  a=0
                  b=0
                  c=selfday1-cd
              else:
                  if(selfday1>=cd):
                   a=selfyr1-cy
                   b=0
                   c=selfday1-cd
                  else:
                   a=selfyr1-cy-1
                   b=11
                   if( cy%4==0):
                    if selfmonth1==1:
                       c=31-cd+selfday1  
                    else:
                       c=dlp[selfmonth1-1]-cd+selfday1
                   else:
                     if selfmonth1==1:
                       c=31-cd+selfday1  
                     else:
                       c=dnp[selfmonth1-1]-cd+selfday1
              speaker.say(a)
              speaker.say("year")
              speaker.say(b)
              speaker.say("month")
              speaker.say(c)
              speaker.say("days")
              speaker.runAndWait()
              return(str(str(a)+" "+"year"+" "+str(b)+" "+"month"+" "+str(c)+" "+"days"))
              
              
          else:
             a=selfyr1-cy
             if selfday1>=cd:
                 b=selfmonth1-cm
                 c=selfday1-cd
             else:
                b=selfmonth1-cm-1
                if( cy%4==0):
                    c=dlp[cm]-cd+selfday1
                else:
                    c=dnp[cm]-cd+selfday1
                    
             speaker.say(a)
             speaker.say("year")
             speaker.say(b)
             speaker.say("month")
             speaker.say(c)
             speaker.say("days")
             speaker.runAndWait()
             return(str(str(a)+" "+"year"+" "+str(b)+" "+"month"+" "+str(c)+" "+"days"))
        
def stopwatch():
    speaker.say("press enter to start the timer")
    speaker.runAndWait()
    print("Press enter to start the timer and Ctrl+C to stop the timer")
    while(1):
        try:
           input()
           speaker.say("started:")
           speaker.runAndWait()
           a=time.time()
           while(1):
               print(round(time.time()-a,0),'sec',end='\r')
               time.sleep(1)
        except KeyboardInterrupt:#KeyBoard Interrupt means Ctrl+C
            t=round(time.time()-a,0)
            speaker.say("totaltime taken:")
            speaker.say(t)
            speaker.say("second")
            speaker.runAndWait()
            print(t)
            break

def length_converter():
  unit1 = input('Which unit do you want it converted from:  ')
  unit2 = input('Which unit do you want it converted to: ')
  num1 = input('Enter the value: ')

  if unit1 == "cm" and unit2 == "m":
    ans = float(num1)/100
    print(ans)
  elif unit1 == "mm" and unit2 == "cm":
    ans = float(num1)/10
    print(ans)
  elif unit1 == "m" and unit2 == "cm":
    ans = float(num1)*100
    print(ans)
  elif unit1 == "cm" and unit2 == "mm":
    ans = float(num1)*10
    print(ans)
  elif unit1 == "mm" and unit2 == "m":
    ans = float(num1)/1000
    print(ans)
  elif unit1 == "m" and unit2 == "mm":
    ans = float(num1)*1000
    print(ans)
  elif unit1 == "km" and unit2 == "m":
    ans = float(num1)*1000
    print(ans)
  elif unit1 == "m" and unit2 == "km":
    ans = float(num1)/1000
    print(ans)
  elif unit1 == "mm" and unit2 == "km":
    ans = float(num1)/1000000
    print(ans)
  elif unit1 == "ft" and unit2 == "cm":
    ans = float(num1)*30.48
    print(ans)
  elif unit1 == "ft" and unit2 == "mm":
    ans = float(num1)*304.8
    print(ans)
  elif unit1 == "ft" and unit2 == "inch":
    ans = float(num1)*12
    print(ans)
  elif unit1 == "inch" and unit2 == "cm":
    ans = float(num1)*2.54
  elif unit1 == "inch" and unit2 == "mm":
    ans = float(num1)*25.4    
  else:
    print("Sorry!This units are not available.")      

def weight_converter():
  unit1 = input('Which unit do you want it converted from:  ')
  unit2 = input('Which unit do you want it converted to: ')
  num1 = input('Enter the value: ')

  if unit1 == "g" and unit2 == "kg":
    ans = float(num1)/1000
    print(ans)
  elif unit1 == "kg" and unit2 == "g":
    ans = float(num1)*1000
    print(ans)
  elif unit1 == "t" and unit2 == "kg":
    ans = float(num1)*1000
    print(ans)
  elif unit1 == "kg" and unit2 == "t":
    ans = float(num1)/1000
    print(ans)
  elif unit1 == "t" and unit2 == "g":
    ans = float(num1)*1000000
    print(ans)
  elif unit1 == "g" and unit2 == "t":
    ans = float(num1)/1000000
    print(ans)
  elif unit1 == "lb" and unit2 == "g":
    ans = float(num1)*453.59
    print(ans)
  elif unit1 == "g" and unit2 == "lb":
    ans = float(num1)/453.59
    print(ans)
  elif unit1 == "lb" and unit2 == "kg":
    ans = float(num1)/2.205
    print(ans)
  elif unit1 == "kg" and unit2 == "lb":
    ans = float(num1)*2.205
    print(ans)
  else:
    print("Sorry!We don't have these units.")
  
speaker.say("enter 1 for timer,2 for alarm,3 for Age Calculator,4 for calendar,5 for World Clock,6 for Stopwatch,7 for Reminder and 8 for Converter ")                                                
speaker.runAndWait()
print("Hello!")
opt=int(input("Enter\n1 Timer\n2 Alarm\n3 Age Calculator\n4 Calendar\n5 World Clock\n6 Stopwatch\n7 Reminder\n8 Converter\n"))

if opt==1:
    speaker.say("enter seconds:")
    speaker.runAndWait()
    sec=int(input("enter seconds:"))
    set_timer(sec)
    
if opt==2:
    speaker.say("enter hour:")
    speaker.runAndWait()
    hour=int(input("enter hour:"))
    speaker.say("enter min:")
    speaker.runAndWait()
    min=int(input("enter min:"))
    speaker.say("enter am or pm:")
    speaker.runAndWait()
    format=str(input("enter am or pm:"))
    speaker.runAndWait()
    set_alram(hour,min,format)
    
if opt==3:
    speaker.say("enter date of birth:")
    speaker.runAndWait()
    date=int(input("enter date of birth:"))
    speaker.say("enter month of birth:")
    speaker.runAndWait()
    month=int(input("enter month of birth:"))
    speaker.say("enter year of birth:")
    speaker.runAndWait()
    year=int(input("enter year of birth:"))
    a=str(get_age(date,month,year))
    print(a)
    
    l=a.split()
    if int(l[4])==0 and int(l[2])==0:
      print("Happy Birthday!!")
      playsound(r'C:\Users\Swaroop\Desktop\Happy-Birthday-To-You.mp3')
      speaker.say("Happy Birthday")
      speaker.runAndWait()

if opt==4:
   
    print(calendar.month(datetime.datetime.now().year,datetime.datetime.now().month))
    speaker.say("Do you want the calendar for any specific month of a year?")
    speaker.runAndWait()
    sel=input("Do you want the calendar for any specific month of a year?\nEnter Y for yes ")
    if sel=='Y' or sel=='y':
      speaker.say("enter month")
      speaker.runAndWait()
      month=int(input("enter month "))
      speaker.say("enter year")
      speaker.runAndWait()
      year=int(input("enter year "))
      mycla=calendar.month(year,month)
      speaker.say("your calendar is:")
      speaker.runAndWait()
      print(mycla)

if opt==5:
  currentDT = datetime.datetime.now()
  print("Select the country:")
  speaker.say("Select the country")
  speaker.runAndWait()
  country=int(input("1.India\n2.USA\n3.Australia\n4.United Kingdom\n5.Japan\n6.France\n7.Dubai\n"))
  if country==1:
    print("Current Date and Time in India:",currentDT)
  elif country==2:
    X=(9*60*60)+(30*60)
    usa = datetime.datetime.now() - datetime.timedelta(seconds=X)
    print("Current Date and Time in USA:",usa)
  elif country==3:
    X=(5*60*60)+(30*60)
    australia=datetime.datetime.now() + datetime.timedelta(seconds=X)
    print("Current Date and Time in Australia:",australia)
  elif country==4:
    X=(4*60*60)+(30*60)
    uk=datetime.datetime.now() - datetime.timedelta(seconds=X)
    print("Current Date and Time in UK:",uk)
  elif country==5:
    X=(3*60*60)+(30*60)
    japan=datetime.datetime.now() + datetime.timedelta(seconds=X)
    print("Current Date and Time in Japan:",japan)
  elif country==6:
    X=(4*60*60)+(30*60)
    france=datetime.datetime.now() - datetime.timedelta(seconds=X)
    print("Current Date and Time in France:",france)
  elif country==7:
    X=(1*60*60)+(30*60)
    dubai=datetime.datetime.now() - datetime.timedelta(seconds=X)
    print("Current Date and Time in UK:",dubai)
  else:
    print("Invalid Input")
  
if opt==6:
  stopwatch()

if opt==7:
  today_date = datetime.datetime.now()
  today_day = today_date.day
  today_month = today_date.month
  today_year = today_date.year

  events = open(r"event", "a+")
  day_file = open(r"day", "a+")
  month_file = open(r"month", "a+")
  year_file = open(r"year", "a+")

  events.close()
  day_file.close()
  month_file.close()
  year_file.close()

  events = open("event", "r")
  day_file = open("day", "r")
  month_file = open("month", "r")
  year_file = open("year", "r")


  a = day_file.readline()

  b = month_file.readline()

  if  a == str(today_day) :
    if b == str(today_month):
      print("Today's event is : ") 
      # playsound(r'C:\Users\Swaroop\Desktop\outlook_reminder.mp3')
      print(events.readline())
      

  events.close()
  day_file.close()
  month_file.close()
  year_file.close()

  conferm = input("Do you want to set a remainder \n Type Y for Yes \n Type N for No ")
  if conferm == 'Y' or conferm=='y':
    print("Enter the date, month, year and the event of which you want remainder")

    day = (input("Enter the day: "))
    month = (input("Enter the month: "))
    year  = (input("Enter the year: "))
    event_str = input("Enter the event details: ")

    events = open(r"event", "w")
    day_file = open(r"day", "w")
    month_file = open(r"month", "w")
    year_file = open(r"year", "w")

    day_file.write(day)
    month_file.write(month)
    year_file.write(year)
    events.write(event_str)

    events.close()
    day_file.close()
    month_file.close()
    year_file.close()

 
  else:
    events = open("event", "r")
    day_file = open("day", "r")
    month_file = open("month", "r")
    year_file = open("year", "r")

  if  a == str(today_day) :
    if b == str(today_month):
      print("Today's event is : ") 
      print(events.readline()) 
  events.close()
  day_file.close()
  month_file.close()
  year_file.close()

if opt==8:
  speaker.say("Select the Converter")                                                
  speaker.runAndWait()
  sel=int(input("1.Length Converter\n2.Weight Converter\n"))

  if sel==1:
    length_converter()
  elif sel==2:
    weight_converter()
  else:
    print("Invalid Input")
  

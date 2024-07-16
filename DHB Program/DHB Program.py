#Created on 18/05/2021
#DHB Program

a_dictionary={}
my_file=open("NHIdata2.csv", "r")

for line in my_file:
    data=[]
    key, value = line.split(":")
    data=value.split(",")
    a_dictionary[key]=data
    
    name=line[0]
    address=line[1]
    d_o_b=line[2]
    first_dose=line[3]
    second_dose=line[4]
    injected=line[5]    
    
#print(a_dictionary)

def welcome(): #create a welcome module
    print("")
    print("******************************************")
    print("*****Welcome to Covid Vaccinations!*****")
    print("******************************************")
    print("")

def data():   
    def nhi_not_found(): #function for is the nhi number cannot be found
        print("Please call the Ministry in Wellington. Then enter the data below: ") 
        temp=[]
        n_nhi_num=input("NHI Number: ")
        n_name=input("Name: ")
        n_address=input("Address: ")
        
        d_o_b=""
        while d_o_b=="":
            d_o_b=input("DOB (dd/mm/yyyy): ")
            
            if d_o_b=="":
                d_o_b=input("Please enter your date of birth (dd/mm/yyyy): ")
            else:
                continue
            
        #checking date inputted is valid
        import datetime
        day,month,year=d_o_b.split("/")
        format="%d/%m/%Y"
        
        try:
            datetime.datetime.strptime(d_o_b, format)
        
        except ValueError:
            print("This is the incorrect date  format. It should be DD-MM-YYYY")    
            d_o_b=input("Please enter your date of birth (dd/mm/yyyy): ")
        
        first=""
        second=""
        complete="N"
        
        new_data=n_nhi_num + ":" +n_name+","+ n_address+"," +d_o_b+"," +first+"," +second+","+complete
        print(new_data)
        print("")
        
        with open("NHIdata2.csv", "a") as f:
            f.write("\n"+new_data) #adding new data to dictionary
        
        print("Please restart the program.") 
        print("")
        
    nhi_num=input("NHI Number: ") 
    if nhi_num=="": #tell the user what to do if NHI number cannot be found
        nhi_not_found()
        
    else: 
        info=a_dictionary.get(nhi_num) #search dictionary for NHI number inputted
        print("Name: ", info[0])
        print("Address: ", info[1])
        print("DOB: ", info[2])
        print("First Dose: ", info[3])
        print("Second Dose: ", info[4])
        print("Injected?: ", info[5])
        

    #ADDRESS CHANGE
    
    def address_change():
        old_address=address
        change_address="t"
            
        while change_address!="Y" or change_address!="N":
            change_address=input("Do you want to change the address? (Y/N) ")
                
            if change_address=="Y":
                new_address=input("Please enter the new address: ")
                
                for value in a_dictionary:
                    if key==old_address:
                        a_dictionary[old_address]=new_address
                        with open("NHIdata2.csv", "a") as f:
                            f.write(old_address==new_address)                 
                
                print("The new address is: ", new_address)
                print("")
                break
            elif change_address=="N":
                print("")
                break
            else:
                continue
    address_change() 
        
    #AGE CHECK
    
    from datetime import date
    from datetime import datetime
    
    info=a_dictionary.get(nhi_num)
    d_o_b=info[2]
        
    d_o_b=datetime.strptime(info[2], '%d/%m/%Y')
    today=datetime.today()
    age_user=today.year-d_o_b.year-((today.month, today.day)<(d_o_b.month, d_o_b.day))
    
    
    if age_user<16: 
        print("Age Check: The patient is too young.")
        
    else: 
        print("Age Check: The patient is okay to get the vaccine.")    
        
        
    #BOTH DOSES AND INJECTED
    
    print("")
    
    first_dose=info[3]
        
    while first_dose!="Y" or first_dose!="N":
        import datetime
        today=datetime.date.today()
            
        if first_dose=="Y": #if the patient has gotten the first dose
            info[3]=today
            print("Today's date is: ", today)
            second_dd = today + datetime.timedelta(21) #add 21 days to current date for second dose date
            print("")
            print("The date for the second dose is: ", second_dd)
            print("Please ask the patient to return on this date.")
            second_dd=info[4]
            
            #with open("NHIdata2.csv", "a") as f:
                #f.write(info[3]==today)
                #f.write(info[4]==second_dd)
            
            break
            
        elif first_dose=="N": #if the patient hasn't gotten the first dose
            info[3]=""
            info[4]=""
            info[5]="N"
            print("The patient is elligible for two doses.") 
            print("")
            break
            
        else:
            if age_user<16: #if the user is not over 16 years old, the program will stop
                data()
            else:
                first_dose=input("Did the patient get their first dose? (Y/N) ") 
    
    
        second_dd=info[4]
        
    while second_dose=="":
        if second_dd==today:
            print("The patient has already gotten both doses. Please send them home.")
            data()
                
        elif second_dd!=today:
            info[4]=second_dd
            info[5]="N"
            break

welcome()
data()
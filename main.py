import pandas as pd
import matplotlib.pyplot as plt
#def logon():
#    Id=input('Enter Id:')


def menu(): #This menu is a wrapper for the functions of the application with a simple Tui
    selector=input("""
    [1] View Performace per Person
    [2] View Performance per Reigon NOT IMPLIMENTED
    [3] Show Best Performing Person of all Time

    """)
    if selector=='1':
        Id=input('Please Enter the Id of the person you would like to view the sales of ')
        try: Id=int(Id)
        except(ValueError):
            print('Please input a valid Id')
        else:
            GetSalesPersonData(Id)
    elif selector=='2':
        GetBestReigon()
    elif selector=='3':
        GetGoat()
    else:
        print(f'{selector} is not a valid option please try again.')


def findId(Id,df): #This function Loads the csv interates through it until the given id is located,the row it resides on is returned as index
    for index in range(len(df)):#declares the amount of iterations by the amount of rows within the dataframe
        currentValue=df.iloc[index,0]#declares current value as the selected value index (row) at position 0 which in this cas is Id
        if currentValue==Id:
            print(f'id found at row {index}')
            return index


def lookupSalesInfo(Idlocation,df):#Simple Function to wrap the lookup of Sales info
    return df.iloc[Idlocation,4:]#Selects columns at row Idlocation past row 4 and returns the value
    
def GetSalesPersonData(Id):
    df=pd.read_csv('data.csv')
    Idlocation=findId(Id,df)
    if Idlocation==None:
        print('An error occured while finding the Id please try again and ensure the id is valid')
    else:
        currentdata=lookupSalesInfo(Idlocation,df) #plots the sales data where x is the date when a sale is perfomed and y is the amount
        currentdata.plot()
        plt.show()

def GetGoat():#This function reads the csv and determines the highest value (number of sales) a person has
    df=pd.read_csv('data.csv')
    data=[]#initalises the data list
    for index in range(len(df)):#loops through dataframe in order to create a list with the summed values of each persons sales
        data.append( df.iloc[index,4:].sum())
    win=max(data)#this retrives the highest value in the list
    for index in range(len(df)): #This loop is needed to search through the data frame to find which row the greatest value is on to present the best salesperson
        if df.iloc[index,4:].sum() == win: 
            #print(f'Best Salesperson is at row {index}')
            Fname=df.loc[index,"Forename"]
            Lname=df.loc[index,"Surname"]
            print(f'The best Sales Person of all time is {Fname} {Lname} with {win} Sales.')

    
    
def GetBestReigon():
    df=pd.read_csv('data.csv')
    data=[]#initalises the data list
    London=0
    Wales=0
    SouthWest=0
    SouthEast=0
    WestMidlands=0
    for index in range(len(df)):
        data.append( df.iloc[index,4:].sum())
        for index in range(len(df)): 
            currentValue=data[index]#funky stuff is happening here....
            if df.iloc[index,4:].sum() == currentValue: 
                if df.loc[index,"Region"]=='London':
                    London+=currentValue
                elif df.loc[index,"Region"]=='Wales':
                    Wales+=currentValue
                elif df.loc[index,"Region"]=='South-West':
                    SouthWest+=currentValue
                elif df.loc[index,"Region"]=='South-East':
                    SouthEast+=currentValue
                elif df.loc[index,"Region"]=='West-Midlands':
                    WestMidlands+=currentValue
                print(London,Wales,SouthEast,SouthWest,WestMidlands)
                





while True:
    menu()

class TravelRecord:
    # This is class TravelRecorder, provide the constructor, getter and setter for the CSV file
# author: Jianchao Jia
# Date 2023, September 20th





    # constructor of the TravelRecoeder class
    def __init__(self, Ref_Number,Disclosure_Group, Title_en ,Title_fr, Name, Purpose_en, Purpose_fr,Start_Date, End_Date,Destination_en, 
        Destination_fr, Airfare, Other_Transport , Lodging, Meals, Other_Expenses, Total, Additional_Comments_en,Additional_Comments_fr,Owner_Org, Owner_Org_Title):
      
         self.Ref_Number = Ref_Number
         self.Disclosure_Group = Disclosure_Group
         self.Title_en = Title_en
         self.Title_fr = Title_fr
         self.Name = Name
         self.Purpose_en = Purpose_en
         self.Purpose_fr = Purpose_fr
         self.Destination_en= Destination_en
         self.Destination_fr = Destination_fr
         self.Start_Date = Start_Date
         self.End_Date  = End_Date 
         self.Airfare = Airfare
         self.Other_Transport = Other_Transport
         self.Lodging = Lodging
         self.Meals = Meals
         self.Other_Expenses = Other_Expenses
         self.Total = Total 
         self.Additional_Comments_en= Additional_Comments_en
         self.Additional_Comments_fr = Additional_Comments_fr
         self.Owner_Org = Owner_Org
         self.Owner_Org_Title= Owner_Org_Title
    # getter of Number
    def get_Ref_Number(self):
        
        return self.Ref_Number

    # Setter of number
    def set_Ref_Number(self, value):
        
        self.Ref_Number = value
    # getter of group
    def get_Disclosure_Group(self):
        
        return self.Disclosure_Group
    # setter of group
    def set_Disclosure_Group(self, value):
        
        self.Disclosure_Group = value
    # getter of Title
    def get_Title_en(self):
        
        return self.Title_en
    # setter of Title
    def set_Title_en(self, value):
        
        self.Title_en = value
    # getter of Title French
    def get_Title_fr(self):
        
        return self.Title_fr
    # setter of Title Franch
    def set_Title_fr(self, value):
        
        self.Title_fr = value

    # getter of Name
    def get_Name(self):
        
        return self.Name
    # setter of Name
    def set_Name(self, value):
        
        self.Name = value
    # getter of Purpose_en
    def get_Purpose_en(self):
        
        return self.Purpose_en

    #Setter of Purpose_en
    def set_Purpose_en(self, value):
        
        self.Purpose_en = value
    # getter of Purpose French
    def get_Purpose_fr(self):
        
        return self.Purpose_fr
    # setter of Purpose French
    def set_Purpose_fr(self, value):
        
        self.Purpose_fr = value

    #getter of Destination English
    def get_Destination_en(self):
        
        return self.Destination_en
    # setter of Destination English
    def set_Destination_en(self, value):
        
        self.Destination_en = value

    # getter of Destination French
    def get_Destination_fr(self):
        
        return self.Destination_fr

    # setter of Destination French
    def set_Destination_fr(self, value):
        
        self.Destination_fr = value


    # getter of Start date    
    def get_Start_Date(self):
        
        return self.Start_Date
    
# setter of start date
    def set_Start_Date(self, value):
        
        self.Start_Date = value

# getter of end date
    def get_End_Date(self):
        
        return self.End_Date
# setter of end date
    def set_End_Date(self, value):
        
        self.End_Date= value
# getter of Airfare
    def get_Airfare(self):
        
        return self.Airfare
#setter of airfare
    def set_Airfare(self, value):
        
        self.Airfare = value


    # getter of other transport
    def get_Other_Transport(self):
        
        return self.Other_Transport
    # setter of other transport
    def set_Other_Transport(self, value):
        
        self.Other_Transport = value
    
    # getter of lodging
    def get_Lodging(self):
        
        return self.Lodging
    # setter of lodging
    def set_Lodging(self, value):
        
        self.Lodging = value
   
    # getter of Meals
    def get_Meals(self):
       
        return self.Meals

    # setter of Meals
    def set_Meals(self, value):
        
        self.Meals = value
    
    # getter of other expense
    def get_Other_Expenses(self):
        
        return self.Other_Expenses
    # setter of other expense
    def set_Other_Expenses(self, value):
        
        self.Other_Expenses = value


    # getter of total
    def get_Total(self):
        
        return self.Total
    # setter of total
    def set_Total(self, value):
        
        self.Total = value
   # getter of addition comments english
    def get_Additional_Comments_en(self):
        
        return self.Additional_Comments_en

    # setter of Additional comments english
    def set_Additional_Comments_en(self, value):
        
        self.Additional_Comments_en = value
    
    # getter of additional comments French
    def get_Additional_Comments_fr(self):
        
        return self.Additional_Comments_fr
    # setter of Additional comments French
    def set_Additional_Comments_fr(self, value):
        
        self.Additional_Comments_fr = value

    # getter of Owner orgnization
    def get_Owner_Org(self):
        
        return self.Owner_Org
    
    # setter of Owner orgnization
    def set_Owner_Org(self, value):
        
        self.Owner_Org = value

    # getter of owner Orgnization title
    def get_Owner_Org_Title(self):
        
        return self.Owner_Org_Title
    
    # setter of Owner orgnazation title
    def set_Owner_Org_Title(self, value):
        
        self.Owner_Org_Title = value

    def __str__(self):
        return f"Ref_Number: {self.Ref_Number}\n" \
               f"Disclosure_Group: {self.Disclosure_Group}\n" \
               f"Title (English): {self.Title_en}\n" \
               f"Title (French): {self.Title_fr}\n" \
               f"Name: {self.Name}\n" \
               f"Purpose (English): {self.Purpose_en}\n" \
               f"Purpose (French): {self.Purpose_fr}\n" \
               f"Start Date: {self.Start_Date}\n" \
               f"End Date: {self.End_Date}\n" \
               f"Destination (English): {self.Destination_en}\n" \
               f"Destination (French): {self.Destination_fr}\n" \
               f"Airfare: {self.Airfare}\n" \
               f"Other Transport: {self.Other_Transport}\n" \
               f"Lodging: {self.Lodging}\n" \
               f"Meals: {self.Meals}\n" \
               f"Other Expenses: {self.Other_Expenses}\n" \
               f"Total: {self.Total}\n" \
               f"Additional Comments (English): {self.Additional_Comments_en}\n" \
               f"Additional Comments (French): {self.Additional_Comments_fr}\n" \
               f"Owner Org: {self.Owner_Org}\n" \
               f"Owner Org Title: {self.Owner_Org_Title}"
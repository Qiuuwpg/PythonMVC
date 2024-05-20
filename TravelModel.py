import csv
import os

from TravelRecord import TravelRecord

INPUT_FILE = "Travelq.csv"
OUTPUT_FILE = "Travelrecord.csv"

class TravelModel:
    """ Model class to handle data operations."""
    def __init__(self):
        """Initialize the header and Travel attributes."""
        
        self.travels = []

    def load_data(self):
        """load the file of Travelq."""
        try:
            with open(INPUT_FILE, "r", encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                header = [col.replace('"', '') for col in next(reader)]
                for i, row in enumerate(reader):
                    if i == 100:
                        break
                    self.travels.append(TravelRecord(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                                   row[8], row[9],row[10], row[11], row[12], row[13],row[14],row[15],row[16],row[17], row[18], row[19], row[20]))
            return header, self.travels
        except FileNotFoundError:
            print("File is not in the correct location.")


    def save_data(self):
        # Save the data to TravelRecord.CSV
        with open(OUTPUT_FILE, "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                ["Ref_Number", "Disclosure_Group", "Title_en", "Title_fr", "Name", "Purpose_en", "Purpose_fr", "Start_Date",
                 "End_Date", "Destination_en", "Destination_fr", "Airfare", "Other_Transport", "Lodging", "Meals" , "Other_Expenses", "Total", "Additional_Comments_en", "Additional_Comments_fr", "Owner_Org", "Owner_Org_Title" ])
            for travel in self.travels:
                writer.writerow(
                    [travel.Ref_Number, travel.Disclosure_Group,travel.Title_en, travel.Title_fr, travel.Name, travel.Purpose_en, travel.Purpose_fr, travel.Start_Date, travel.End_Date , travel. Destination_en, travel.Destination_fr, 
                     travel.Airfare, travel.Other_Transport , travel. Lodging, travel.Meals , travel.Other_Expenses ,travel.Total, travel.Additional_Comments_en, travel.Additional_Comments_fr , travel.Owner_Org , travel.Owner_Org_Title])
            # Check if data has been written to the csv file
            if os.path.getsize(OUTPUT_FILE) > 0:
                print("Data has been saved to", OUTPUT_FILE)
            else:
                print("cannot save data to", OUTPUT_FILE)


    def display_record(self, index):
        """
        Display one record of the Travel list by index.
       
        """
        return self.travels[index]


    def display_all_records(self):
        """
        Display all records 
        """
        counter = 1
        for record in self.travels:
            print(record)
            if counter % 10 == 0:
                print("Program by Jianchao Jia")
            counter += 1
        return self.travels


    def get_record(self, index):
        """
        Return the record at the specified index from the list of travels
        
        """
        try:
            index = int(index)
            if 0 <= index < len(self.travels):
                return self.travels[index]
            else:
                return None
        except ValueError:
            return False


    def insert_record(self, record):
        """
        Insert a new record into the list of Travel and display all records 
        
        """
        self.travels.append(record)
        self.display_all_records()


    def update_record(self, index, record):
        """
         Update the record at the specified index in the list of Travel 
        
         """
        index = int(index)
        if 0 <= index < len(self.travels):
            self.travels[index] = record
            self.display_all_records()
        else:
            print("record was not updated and save")


    def delete_record(self, index):
        """
         Delete the record at the specified index in the list of travel
         
         """
        index = int(index)
        if 0 <= index < len(self.travels):
            del self.travels[index]
            self.display_all_records()
        else:
            print("Invalid index, record was not deleted")


from TravelModel import TravelModel
from TravelView import TravelView
from TravelRecord import TravelRecord

class TravelController:
    """
    This PotatoesController class controls the flow of data between the PotatoesModel and PotatoesView classes.
    """
    def __init__(self):
        """
        Initializes instances of the PotatoesModel and PotatoesView classes.
        """
        self.model = TravelModel()
        self.view = TravelView()

    def get_record_index(self):
        """
        Gets the index of a record from the user and returns it if it's within the range of the potatoes list.
        """
        index = int(input("Enter the index of the record: "))
        if 0 <= index < len(self.model.travels):
            return index
        else:
            print("Invalid index, index must be between 0~99")


    def run(self):
        """
        Controls the flow of the program by calling appropriate methods based on the user's choice.
        """
        while True:
            option = self.view.display_menu_get_input()
            if option == 1:
                header, travels = self.model.load_data()
                if header is not None and travels is not None:
                    self.view.display_message("Data has been loaded from Travelrecord.csv\nProgram by Jianchao Jia")

            elif option == 2:
                self.model.save_data()
                self.view.display_message("Program by Jianchao Jia")

            elif option == 3:
                self.view.display_message("Enter the index of the record you want to display: 0 ~ 99")
                index = self.get_record_index()
                record = self.model.get_record(index)
                self.view.display_record(record)
                self.view.display_message("Program by Jianchao Jia")

            elif option == 4:
                self.model.display_all_records()
                self.view.display_all_records()

            elif option == 5:
                self.view.display_message("Enter the new record:")
                record = self.view.get_user_inputRecord().strip()
                new_record_values = record.split(",")
                new_record = TravelRecord(*new_record_values)
                self.model.insert_record(new_record)
                self.view.display_message("New Record has been inserted")
                self.view.display_message("Program by Jianchao Jia")

            elif option == 6:
                self.view.display_message("Enter the index of the record you want to update:")
                index = self.get_record_index()
                self.view.display_message("Enter the updated record:")
                record = self.view.get_user_inputRecord()
                self.model.update_record(index, record)
                self.view.display_message("one Record has been updated")
                self.view.display_message("Program by Jianchao Jia")

            elif option == 7:
                self.view.display_message("Enter the index of the record you want to delete:")
                index = self.view.get_user_inputRecord()
                self.model.delete_record(index)
                self.view.display_message("one Record has been deleted")
                self.view.display_message("Program by Jianchao Jia")

            elif option == 8:
                self.view.display_message("Program quitting...\nProgram by Jianchao Jia")
                break

            else:
                print("Invalid option. Try again.\nProgram by Jianchao Jia")

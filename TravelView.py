from TravelRecord import TravelRecord

class TravelView:
    """
    This view class implements the display methods for the menu and other interactions with the user.
    """
    @staticmethod
    def display_menu_get_input():
        """
        This method displays the menu of options for the user and takes an integer input as the user's choice.
        """
        try:
            print("Enter your option (1-8): \n"
                  "1. Load data from dataset   2. Save data to disk\n"
                  "3. Display a record         4. Display all records\n"
                  "5. Insert a new record      6. Update a record\n"
                  "7. Delete a record          8. Quit the program")
            return int(input())
        except ValueError:
            print("Please input a number")


    @staticmethod
    def display_message(message):
        """
        This method displays a message passed as argument.
        :param message: Message to be displayed
        """
        print(message)


    def display_record(self, record):
        """
        This method displays a potato record.
        :param record: Record of potatoes to be displayed
        """
        print(record)

    def display_all_records(self):
        """
        This method displays all potato records.
        """
        return

    def get_new_record(self):
        """
        This method takes a new potato record as input from the user.
        :return: a list of values representing the new potato record
        """
        return input("Enter the new record: ").split(",")


    @staticmethod
    def get_user_inputRecord():
        """
        This method takes a string input from the user.
        :return: a string input from the user.
        """
        return input()


    @staticmethod
    def insert_record(model):
        """
        This method takes the potato record from the user and inserts it into the potatoes model.
        :param model: PotatoesModel object to which the new record is to be added
        """
        try:
            new_record_str = input("Enter the new record: ")
            new_record_values = new_record_str.split(",")
            new_record = TravelRecord(*new_record_values)
            model.insert_record(new_record)
            print("Record inserted successfully!")
        except TypeError:
            print( "Please provide a valid record.")


    @staticmethod
    def quit():
        """
        This method displays a message indicating that the program is quitting.
        """
        print("Quitting program...")
class CSVReader:
    def __init__(self, obj):
        self.obj = obj

    def csv_reader(self):
        """
        counts record in csv file
        :return: return number of records

        """
        return len(self.obj.csv_loader())


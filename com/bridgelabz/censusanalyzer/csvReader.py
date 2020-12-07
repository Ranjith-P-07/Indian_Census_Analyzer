import json


class CSVReader:
    def __init__(self, obj):
        self.obj = obj

    def csv_reader(self):
        """
        counts record in csv file
        :return: return number of records

        """
        return len(self.obj.csv_loader())

    def sort_csv_data(self, colm_name):
        """
        sorts csv data  by State code
        :return:sorted data in json format
        """
        value_Dict = {}
        data = self.obj.csv_loader().sort_values(colm_name)
        for x in data.values:
            data_list = list(x)
            value_Dict[data_list[0]] = data_list
        return json.dumps(value_Dict)

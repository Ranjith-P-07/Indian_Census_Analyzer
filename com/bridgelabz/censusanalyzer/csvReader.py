import json

from com.bridgelabz.censusanalyzer.IndiaCensusCSV import IndiaCensusCSV
from com.bridgelabz.censusanalyzer.censusanalyzer import CSVLoader


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
        cod = True
        if colm_name == "Population" or colm_name == "DensityPerSqKm" or colm_name == "AreaInSqKm":
            cod = False
        data = self.obj.csv_loader().sort_values(colm_name, ascending=cod)
        for x in data.values:
            data_list = list(x)
            value_Dict[data_list[0]] = data_list
        return json.dumps(value_Dict)


# if __name__ == "__main__":
#     census_csv = CSVLoader(
#         "/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCensusData.csv",
#         IndiaCensusCSV())
#     csv = CSVReader(census_csv)
#     print(csv.sort_csv_data("State"))

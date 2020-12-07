import pandas as pd
from com.bridgelabz.censusanalyzer.CensusAnalyzerError import CensusAnalyserError
from com.bridgelabz.censusanalyzer.IndiaCensusCSV import IndiaCensusCSV


class CSVLoader:

    def __init__(self, path, header):
        self.path = path
        self.header = header

    def csv_loader(self):
        """
        Loads csv file
        :return: Data of CSV  file
        """
        try:
            col_names = repr(self.header).split(",")
            data = pd.read_csv(self.path, usecols=col_names)
            return data
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")


# if __name__ == "__main__":
#     csv = CSVLoader("/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCensusData.csv",
#                     IndiaCensusCSV())
#     print(csv.csv_loader())

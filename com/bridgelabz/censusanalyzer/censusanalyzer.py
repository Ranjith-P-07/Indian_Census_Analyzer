import pandas as pd
from com.bridgelabz.censusanalyzer.CensusAnalyzerError import CensusAnalyserError


class CSVLoader:

    def __init__(self, path, header):
        self.path = path
        self.header = header

    def csv_loader(self):
        """
        Count record in file
        :return: number of records in file
        """
        try:
            col_names = repr(self.header).split(",")
            data = pd.read_csv(self.path, usecols=col_names)
            return data
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")


import pandas as pd
from com.bridgelabz.censusanalyzer.CensusAnalyzerError import CensusAnalyserError
from com.bridgelabz.censusanalyzer.IndiaCensusCSV import IndiaCensusCSV


class CSVLoader:

    def __init__(self, path):
        self.path = path

    def record_counter(self):
        """
        Count record in file
        :return: number of records in file
        """
        try:
            col_names = repr(IndiaCensusCSV()).split(",")
            data = pd.read_csv(self.path, usecols=col_names)
            return len(data)
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong Delimiter or Invalid Columns Name")

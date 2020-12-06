from com.bridgelabz.censusanalyzer.CensusAnalyzerError import CensusAnalyserError
from com.bridgelabz.censusanalyzer.StatecodeAnalyzer import Statecodeanalyzer
from com.bridgelabz.censusanalyzer.censusanalyzer import CSVLoader
from com.bridgelabz.censusanalyzer.IndiaCensusCSV import IndiaCensusCSV
import pytest

from com.bridgelabz.censusanalyzer.csvReader import CSVReader

CENSUS_CSV_FILE_PATH = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = "IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = r"home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCensusData.xls"

# NOTE - Change delimiter of the file and save it
CENSUS_CSV_FILE_WRONG_DELIMITER = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/USCensusDataDelimiter.csv"
CENSUS_CSV_WRONG_HEADER_FILE_PATH = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCensusData1.csv"
CENSUS_CSV_FILE_PATH_STATE = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCode.csv"


@pytest.mark.parametrize("header, path, result",
                         [
                             (IndiaCensusCSV(), CENSUS_CSV_FILE_PATH, 29),
                             (Statecodeanalyzer(), CENSUS_CSV_FILE_PATH_STATE, 37)
                         ])
# This is a Happy test Case Where records are checked
def test_Happy_Test_Case_where_the_records_are_checked_TC_1_and_2(header, path, result):
    csv = CSVLoader(path, header)
    csv_file = CSVReader(csv)
    assert csv_file.csv_reader() == result


@pytest.mark.parametrize("header, path, result", [
    (IndiaCensusCSV(), CENSUS_CSV_FILE_WRONG_PATH, CensusAnalyserError),
    (IndiaCensusCSV(), CENSUS_CSV_FILE_WRONG_TYPE, CensusAnalyserError),
    (IndiaCensusCSV(), CENSUS_CSV_FILE_WRONG_DELIMITER, CensusAnalyserError),
    (IndiaCensusCSV(), CENSUS_CSV_WRONG_HEADER_FILE_PATH, CensusAnalyserError),
    (Statecodeanalyzer(), CENSUS_CSV_FILE_WRONG_PATH, CensusAnalyserError),
    (Statecodeanalyzer(), CENSUS_CSV_FILE_WRONG_TYPE, CensusAnalyserError),
    (Statecodeanalyzer(), CENSUS_CSV_FILE_WRONG_DELIMITER, CensusAnalyserError),
    (Statecodeanalyzer(), CENSUS_CSV_WRONG_HEADER_FILE_PATH, CensusAnalyserError)
                                                ])
# This is a Sad Test Cases to verify if exception gets raised or not
def test_Given_the_CSV_File_if_incorrect_Returns_a_custom_Exception_TC_1_and_2(header, path, result):
    with pytest.raises(result):
        csv = CSVLoader(path, header)
        csv.csv_loader()

from com.bridgelabz.censusanalyzer.CensusAnalyzerError import CensusAnalyserError
from com.bridgelabz.censusanalyzer.censusanalyzer import CSVLoader
import pytest

CENSUS_CSV_FILE_PATH = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = "IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = r"home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCensusData.xls"

# NOTE - Change delimiter of the file and save it
CENSUS_CSV_FILE_WRONG_DELIMITER = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/USCensusDataDelimiter.csv"
CENSUS_CSV_WRONG_HEADER_FILE_PATH = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCensusData1.csv"


# This is a Happy test Case Where records are checked
def test_record_counter():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_PATH)
    assert csv_loader.record_counter() == 29


# This is a Sad Test Case to verify if exception gets raised or not
def test_record_counter_for_wrong_file_path():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_PATH)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


# This is a Sad Test Case to verify if the type is incorrect then exception gets raised
def test_record_counter_for_wrong_file_type():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_TYPE)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


# This is a Sad Test Case to verify if the file delimiter is incorrect then exception gets raised
# NOTE - Change delimiter of the file and save it
def test_record_counter_for_wrong_delimiter():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_DELIMITER)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


# This is a Sad Test Case to verify if the Header is incorrect then exception gets raised
def test_record_counter_for_wrong_Header_File():
    csv_loader = CSVLoader(CENSUS_CSV_WRONG_HEADER_FILE_PATH)
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()
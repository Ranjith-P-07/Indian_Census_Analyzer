from com.bridgelabz.censusanalyzer.CensusAnalyzerError import CensusAnalyserError
from com.bridgelabz.censusanalyzer.StatecodeAnalyzer import Statecodeanalyzer
from com.bridgelabz.censusanalyzer.censusanalyzer import CSVLoader
from com.bridgelabz.censusanalyzer.IndiaCensusCSV import IndiaCensusCSV
import pytest

CENSUS_CSV_FILE_PATH = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = "IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = r"home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCensusData.xls"

# NOTE - Change delimiter of the file and save it
CENSUS_CSV_FILE_WRONG_DELIMITER = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/USCensusDataDelimiter.csv"
CENSUS_CSV_WRONG_HEADER_FILE_PATH = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCensusData1.csv"
CENSUS_CSV_FILE_PATH_STATE = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCode.csv"


# This is a Happy test Case Where records are checked
def test_Happy_Test_Case_where_the_records_are_checked_TC_1_1():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_PATH, IndiaCensusCSV())
    assert csv_loader.record_counter() == 29


# This is a Sad Test Case to verify if exception gets raised or not
def test_Given_the_Indian_Census_CSV_File_if_incorrect_Returns_a_custom_Exception_TC_1_2():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_PATH, IndiaCensusCSV())
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


# This is a Sad Test Case to verify if the type is incorrect then exception gets raised
def test_Given_the_Indian_Census_CSV_File_when_correct_but_type_incorrect_Returns_a_custom_Exception_TC_1_3():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_TYPE, IndiaCensusCSV())
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


# This is a Sad Test Case to verify if the file delimiter is incorrect then exception gets raised
# NOTE - Change delimiter of the file and save it
def test_Given_the_Indian_Census_CSV_File_when_correct_but_wrong_delimiter_incorrect_Returns_a_custom_Exception_TC_1_4():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_DELIMITER, IndiaCensusCSV())
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


# This is a Sad Test Case to verify if the Header is incorrect then exception gets raised
def test_Given_the_Indian_Census_CSV_File_when_correct_but_wrong_Header_Returns_a_custom_Exception_TC_1_5():
    csv_loader = CSVLoader(CENSUS_CSV_WRONG_HEADER_FILE_PATH, IndiaCensusCSV())
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


# This is a Happy test Case Where records are checked
def test_Happy_Test_Case_where_the_records_are_checked_TC_2_1():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_PATH_STATE, Statecodeanalyzer())
    assert csv_loader.record_counter() == 37


# This is a Sad Test Case to verify if exception gets raised or not
def test_Given_the_State_Census_CSV_File_if_incorrect_Returns_a_custom_Exception_TC_2_2():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_PATH, Statecodeanalyzer())
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


# This is a Sad Test Case to verify if the type is incorrect then exception gets raised
def test_Given_the_State_Census_CSV_File_when_correct_but_type_incorrect_Returns_a_custom_Exception_TC_2_3():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_TYPE, Statecodeanalyzer())
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


# This is a Sad Test Case to verify if the file delimiter is incorrect then exception gets raised
# NOTE - Change delimiter of the file and save it
def test_Given_the_State_Census_CSV_File_when_correct_but_wrong_delimiter_incorrect_Returns_a_custom_Exception_TC_2_4():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_DELIMITER, Statecodeanalyzer())
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()


# This is a Sad Test Case to verify if the Header is incorrect then exception gets raised
def test_Given_the_State_Census_CSV_File_when_correct_but_wrong_Header_Returns_a_custom_Exception_TC_2_5():
    csv_loader = CSVLoader(CENSUS_CSV_WRONG_HEADER_FILE_PATH, Statecodeanalyzer())
    with pytest.raises(CensusAnalyserError):
        csv_loader.record_counter()

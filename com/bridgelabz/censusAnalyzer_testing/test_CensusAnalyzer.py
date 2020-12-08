from com.bridgelabz.censusanalyzer.CensusAnalyzerError import CensusAnalyserError
from com.bridgelabz.censusanalyzer.StatecodeAnalyzer import Statecodeanalyzer
from com.bridgelabz.censusanalyzer.censusanalyzer import CSVLoader
from com.bridgelabz.censusanalyzer.IndiaCensusCSV import IndiaCensusCSV
from com.bridgelabz.censusanalyzer.csvReader import CSVReader
import pytest
import json

CENSUS_CSV_FILE_PATH = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = "IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = r"home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCensusData.xls"

# NOTE - Change delimiter of the file and save it
CENSUS_CSV_FILE_WRONG_DELIMITER = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/USCensusDataDelimiter.csv"
CENSUS_CSV_WRONG_HEADER_FILE_PATH = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCensusData1.csv"
CENSUS_CSV_FILE_PATH_STATE = r"/home/ubuntu/PycharmProjects/IndiaCensusAnalyzer/com/bridgelabz/Data/IndiaStateCode.csv"


@pytest.fixture
def census_csv_file():
    csv_file = CSVLoader(CENSUS_CSV_FILE_PATH, IndiaCensusCSV())
    csv = CSVReader(csv_file)
    return csv


@pytest.fixture
def state_csv_file():
    csv_file = CSVLoader(CENSUS_CSV_FILE_PATH_STATE, Statecodeanalyzer())
    state_csv_file = CSVReader(csv_file)
    return state_csv_file


@pytest.mark.parametrize("header, path, result",
                         [
                             (IndiaCensusCSV(), CENSUS_CSV_FILE_PATH, 29),
                             (Statecodeanalyzer(), CENSUS_CSV_FILE_PATH_STATE, 37)
                         ])
# This is a Happy test Case Where records are checked
def test_Given_Test_Case_where_the_records_are_checked_UC_1_and_2(header, path, result):
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


def test_Given_the_CSV_File_When_Sorted_If_incorrect_Should_Raise_Custom_Exception(census_csv_file):
    data = json.loads(census_csv_file.sort_csv_data("State"))
    if list(data.keys())[0] != "Andhra Pradesh":
        raise CensusAnalyserError("File is not sorted!!!")
    if list(data.keys())[len(data) - 1] != "West Bengal":
        raise CensusAnalyserError("File is not sorted!!!")


def test_Given_CSV_File_When_Sorted_If_incorrect_Should_Raise_Custom_Exception(state_csv_file):
    data = json.loads(state_csv_file.sort_csv_data("StateCode"))
    if list(data.get(list(data.keys())[0]))[3] != "AD":
        raise CensusAnalyserError("File is not sorted")
    if list(data.get(list(data.keys())[len(data) - 1]))[3] != "WB":
        raise CensusAnalyserError("File is not sorted")


def test_given_IndianCensusCSV_When_SortedAccordingToPopulation_IfNot_ShouldRaiseCustomException(census_csv_file):
    data = json.loads(census_csv_file.sort_csv_data("Population"))
    if list(data.keys())[0] != "Uttar Pradesh":
        raise CensusAnalyserError("File is not sorted")
    if list(data.keys())[len(data) - 1] != "Sikkim":
        raise CensusAnalyserError("File is not sorted")


def test_given_IndianCensusCSV_When_SortedAccordingToDensityPerSqKm_IfNot_ShouldRaiseCustomException(census_csv_file):
    data = json.loads(census_csv_file.sort_csv_data("DensityPerSqKm"))
    if list(data.keys())[0] != "Bihar":
        raise CensusAnalyserError("File is not sorted")
    if list(data.keys())[len(data) - 1] != "Arunachal Pradesh":
        raise CensusAnalyserError("File is not sorted")


def test_given_IndianCensusCSV_When_SortedAccordingToAreaInSqKm_IfNot_ShouldRaiseCustomException(census_csv_file):
    data = json.loads(census_csv_file.sort_csv_data("AreaInSqKm"))
    if list(data.keys())[0] != "Rajasthan":
        raise CensusAnalyserError("File is not sorted")
    if list(data.keys())[len(data) - 1] != "Goa":
        raise CensusAnalyserError("File is not sorted")

# Introduction to elementary analysis using Python 3

This repo presents all basic tasks for starting analysis using Python.

## Projects

Projects covering intro to data analysis in **Python3.7**
- using basic types: list, tuple, set
- basics of datetime module
- basics of matplotlib module
- basics of pandas module

## [Text Analysis](https://github.com/LSIND/intro-to-python3-analysis/tree/master/TextAnalysis)

The code:
 - reads all text from .txt file (incl. unicode) 
 - deletes all punctuations from the text
 - breaks all text into independent words. In case of complex word containing hyphen it should be divided into two different words (f.e., *ninety-nine = ninety nine*).
 - prints word(s) with maximum length
 - writes cleaned text to a new .txt file (one word per row).

The folder also includes .txt file with chapter 6 of Dostoevsky's "Crime and Punishment" with English and Russian text.

## [Temperatures Analysis](https://github.com/LSIND/intro-to-python3-analysis/tree/master/TemperaturesAnalysis)

The code:
 - reads all text from .txt file containing list of tempreratures
 - prints maximum, minimum and average temperatures
 - prints number of values
 - prints number of unique values
 - prints number of occurrences for every value in the form of: *temperature : occurrences* sorted by occurrences in ascending order
 - asks a user to input the value interval of temperatures *[a; b]* and prints temperatures and their occurrences sorted by temperature from *a* to *b* in ascending order

The folder also includes 1tempdata.txt file with a set of temperature data (the monthly high temperatures at Heathrow Airport 1948 - 2016).

## [Train Departure Analysis](https://github.com/LSIND/intro-to-python3-analysis/tree/master/TrainDepAnalysis)
The code:
- reads .txt file with data of scheduled and actual departures of trains with the help of module *datetime*

| Train # | Sch Dp                    | Act Dp |
|---------|---------------------------|--------|
| 505     | 09/01/2019 7:11   PM (Su) | 7:39PM |
| 508     | 09/01/2019   5:41 PM (Su) | 5:47PM |
| 505     | 08/10/2019 7:11   PM (Sa) |        |
| ...     | ...                       | ...    |

- counts the number of not operated trains (column *Act Dp* is empty) and prints the number of not operated trains by day of the week using the module *collections*;

   `from collections import Counter`
- counts the number of departed trains, on time departures, late departures and next day departures.

The folder also includes [depsalem.txt](https://github.com/LSIND/intro-to-python3-analysis/blob/master/TrainDepAnalysis/depsalem.txt) file with a set of [train departures](https://juckins.net/amtrak_status/archive/html/history.php) from Salem in period 09/01/2018 - 09/01/2019.

## [Plot Currency Rates](https://github.com/LSIND/intro-to-python3-analysis/tree/master/PlotCurrencyRates "PlotCurrencyRates")
The code (module **readxml**):
 - reads data from [Central Bank of Russia](http://www.cbr.ru/development/SXML/) containing currency information in XML-format:
    * [XML with currency names and codes (ids)](http://www.cbr.ru/scripts/XML_val.asp?d=0). The code should retrieve the code from the provided name, f.e. Euro = R01239;
    * [XML with currency rates](http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=05/09/2019&date_req2=30/09/2019&VAL_NM_RQ=R01239) depending on currency code and two dates. Element < Value >  contains ratio to Russian ruble at a specific date, f.e. 1 Euro = 73,0638 Rub at 05/09/2019 (dd/mm/YY);
    * uses modules *urllib.request* and *xml.etree.ElementTree* to retrieve and parse XML data:
    
     `from urllib.request import urlopen`    
     `from xml.etree.ElementTree import parse`
    
The code (**main. py**)
- provides initial variables: currency name and two dates (period). You can change it or ask user for input.

     `cur = "Euro"`    
     `startdate = "05.09.2019"`    
     `enddate = "30.09.2019"`
- plots graph of currency rates Currency/Russian ruble using *matplotlib*, f.e:

![currency rates](https://uc0afe30445d92bfd3bc7605b774.previews.dropboxusercontent.com/p/thumb/AAlLidPOsM_erUTqBRmTITGfKwUhv8Gd7wg-COelHMwNlnCRsSarN-qwlGzX-AB44kJnz3Qnwh3Twr7KUwgwfWJqEFOPnqVYHRxohCcrw_VT9iNlSYGMeakvvzu4ueSLYkzH4ADONbTfmZjGsA8vxaKGKoDxqP1Q4ns7WNd-B0ks9oaqV-SjmGGyYxsw3rTtU3o6QCfkPRLcNmGAOV9hSxHjoDIA8yiZJ2N6-pMT5CrhKxiy2xgUgIGUlyRujiGMFgAuihZu6q0-ok_2MxVxDHH42SCSHbb8biv77nUJQQJiGgx3VH3y6miCz5fgw7aOZYYei4dCnVCTpf9H2Ut3f4G1mP5IeG8Q2YP8GcCtf_xXtGTeeZkJmPHX8Y8N8TIZ8nHDGQYAUPIVPcmXiAfFaMZ_/p.png?fv_content=true&size_mode=5)

## [Employees Counts](https://github.com/LSIND/intro-to-python3-analysis/tree/master/EmployeesCounts)

The code:
 - reads all data from .csv file containing employees names and hire dates and time using *pandas* module into dataframe
     `import pandas as pd`
    
| ID  | LastName | FirstName | HireDate  | HireTime |
|-----|----------|-----------|-----------|----------|
| 1   | Newell   | Pamella   | 9/9/2018  | 14:57:00 |
| 2   | Green    | Edna      | 8/28/2018 | 7:27:00  |
| ... | ...      |  ...      | ...       | ...      |

 - converts column 'HireDate' to date format *%Y-%m-%d*
 - creates series of column 'HireDate' and applies a condition to it within a period
 - prints number of occurrences in the series (hired people per date)
 - plots a bar graph of occurrences, f.e.:
 
![employees counts](https://lh5.googleusercontent.com/5U4NL8lajRtgTPb4SRXb3EeQ9wSUJJAFJ0MjXzjELPFwLNmcjjIxp3LPh4vCYG3o_b3mp4TDQEgjNg=w1365-h937)
 
The folder also includes empl.csv file with a set of employees names and hire dates and time.

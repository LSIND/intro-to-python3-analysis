# Introduction to elementary analysis using Python 3

This repository presents all basic tasks as an introduction to analysis using Python.

## Projects

Projects covering intro to data analysis using **Python3.7**
- using basic types: list, tuple, set
- basics of datetime module
- basics of matplotlib module
- basics of numpy arrays and pandas module
- read/write text data and XML

## [Text Analysis](https://github.com/LSIND/intro-to-python3-analysis/tree/master/TextAnalysis)
> *Using built-in capabilities for string data processing*

Read .txt file, delete all punctuations, break all text into independent words and write them to a new .txt file. Print word(s) with maximum length on console.

The code:
 - reads all text from .txt file (incl. unicode) 
 - deletes all punctuations from the text
 - breaks all text into independent words. In case of complex word containing hyphen it should be divided into two different words (f.e., *ninety-nine = ninety nine*).
 - prints word(s) with maximum length
 - writes cleaned text to a new .txt file (one word per row).

The folder also includes .txt file with chapter 6 of Dostoevsky's "Crime and Punishment" with English and Russian text.

## [Temperatures Analysis](https://github.com/LSIND/intro-to-python3-analysis/tree/master/TemperaturesAnalysis)
> *Using built-in capabilities for elementary analysis*

Read .txt file, which contains a list of decimal numbers (temperatures), find and print maximum, minimum and average temperatures, print number of elements and unique elements, print number of occurances for every value in the form of: *temperature : occurrences*. Ask user to input an interval and print temperatures and occurences in this interval.

The code:
 - reads all text from .txt file containing list of tempreratures
 - prints maximum, minimum and average temperatures
 - prints number of values
 - prints number of unique values
 - prints number of occurrences for every value in the form of: *temperature : occurrences* sorted by occurrences in ascending order
 - asks a user to input the value interval of temperatures *[a; b]* and prints temperatures and their occurrences sorted by temperature from *a* to *b* in ascending order

The folder also includes 1tempdata.txt file with a set of temperature data (the monthly high temperatures at Heathrow Airport 1948 - 2016).

## [Train Departure Analysis](https://github.com/LSIND/intro-to-python3-analysis/tree/master/TrainDepAnalysis)
> *Using datetime module*

Read .txt file, which contains data with train departures (train no, datetime of scheduled department, datetime of actual department), find and print number of not operated trains, departures on time, late departures and next day departures.

| Train # | Sch Dp                    | Act Dp |
|---------|---------------------------|--------|
| 505     | 09/01/2019 7:11   PM (Su) | 7:39PM |
| 508     | 09/01/2019   5:41 PM (Su) | 5:47PM |
| 505     | 08/10/2019 7:11   PM (Sa) |        |
| ...     | ...                       | ...    |

The code:
- reads .txt file with data of scheduled and actual departures of trains with the help of module *datetime*
    ```python
    import datetime
    ```

- counts the number of not operated trains (column *Act Dp* is empty) and prints the number of not operated trains by day of the week using the module *collections*;
    ```python
   from collections import Counter
   ```

- counts the number of departed trains, on time departures, late departures and next day departures.

The folder also includes [depsalem.txt](https://github.com/LSIND/intro-to-python3-analysis/blob/master/TrainDepAnalysis/depsalem.txt) file with a set of [train departures](https://juckins.net/amtrak_status/archive/html/history.php) from Salem in period 09/01/2018 - 09/01/2019.

## [Plot Currency Rates](https://github.com/LSIND/intro-to-python3-analysis/tree/master/PlotCurrencyRates "PlotCurrencyRates")
> *Using xml module to parse XML-data and matplotlib to plot it*

Read XML-data from [Central Bank of Russia](http://www.cbr.ru/development/SXML/) with currency information depending on period with ratio to Russian ruble. Plot the currency rates.

The code (module **readxml**):
 - reads data from [Central Bank of Russia](http://www.cbr.ru/development/SXML/) containing currency information in XML-format:
    * [XML with currency names and codes (ids)](http://www.cbr.ru/scripts/XML_val.asp?d=0). The code should retrieve the code from the provided name, f.e. Euro = R01239;
    * [XML with currency rates](http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=05/09/2019&date_req2=30/09/2019&VAL_NM_RQ=R01239) depending on currency code and two dates. Element < Value >  contains ratio to Russian ruble at a specific date, f.e. 1 Euro = 73,0638 Rub at 05/09/2019 (dd/mm/YY);
    * uses modules *urllib.request* and *xml.etree.ElementTree* to retrieve and parse XML data:
     ```python
     from urllib.request import urlopen
     from xml.etree.ElementTree import parse
     ```
    
The code (**main. py**)
- provides initial variables: currency name and two dates (period). You can change it or ask user for input.
     ```python
     cur = "Euro"    
     startdate = "05.09.2019"    
     enddate = "30.09.2019"
     ```
- plots a graph of currency rates Currency/Russian ruble using *matplotlib*, f.e:

![currency rates](https://www.dropbox.com/s/d2b03ndlok87q9j/ploteurotorub.PNG?raw=1)


## [Numpy Array vs. List](https://github.com/LSIND/intro-to-python3-analysis/tree/master/NPArrayVSList)
> *Using numpy module*

Compare working time of numpy arrays and built-in lists.
```python
import numpy as np
```

Python built-in list without any elements (`l1 = []`) consumes 64 bytes. For every new element, it needs another 8 bytes for the reference to the new object. The new int object itself consumes 28 bytes. The size of a list `l1 = [5, 10, 15]` can be calculated with:

`64 + 8 * len(l1) + 28 * len(l1) = 88 b (list) + 84 b (int elements) = 172 bytes`

NumPy array without any elements (`n1 = np.array([])`) consumes 96 bytes. For every new element, it also needs another 8 bytes for the reference to the new object. The size of a numpy array `n1 = np.array([5, 10, 15])`, where elements are of int64 type, can be calculated with:

`96 + 8 * len(n1) = 120 bytes`

NumPy arrays have smaller memory consumption and better runtime. 

The code:
- creates two identical built-in lists L1 and L2 and numpy arrays N1 and N2
- counts the time (in sec.) of merging two lists and two numpy arrays
- prints in the ratio t1/t2 - how much faster merging numpy array is in comparison to built-in list

## [Employees Counts](https://github.com/LSIND/intro-to-python3-analysis/tree/master/EmployeesCounts)
> *Using pandas module*

Create a dataframe from .csv file containing information about Employee and his hire datetime. Plot a graph with quantity of hired people by days of specified month.
    
| ID  | LastName | FirstName | HireDate  | HireTime |
|-----|----------|-----------|-----------|----------|
| 1   | Newell   | Pamella   | 9/9/2018  | 14:57:00 |
| 2   | Green    | Edna      | 8/28/2018 | 7:27:00  |
| ... | ...      |  ...      | ...       | ...      |

The code:
 - reads all data from .csv file containing employees names and hire dates/time using *pandas* module into dataframe
     ```python
     import pandas as pd
     ```

 - converts column 'HireDate' to date format *%Y-%m-%d*
 - creates series of column 'HireDate' and applies a condition to it within a period
 - prints number of occurrences in the series (hired people per date)
 - plots a bar graph of occurrences, f.e.:
 
![employees counts](https://www.dropbox.com/s/zplryx10b7o7iqr/plotemplcount.PNG?raw=1)
 
The folder also includes empl.csv file with a set of employees names and hire dates and time.

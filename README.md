# Introduction to elementary analysis using Python 3

This repo presents all basic tasks for starting analysis using Python.

## Projects

Projects covering intro to data analysis in **Python3.7**

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
 - reads all text from .txt file
 - prints maximum, minimum and average temperatures
 - prints number of values
 - prints number of unique values
 - prints number of occurrences for every value in the form of: *temperature : occurrences* sorted by occurrences in ascending order
 - asks a user to input the value interval of temperatures *[a; b]* and prints temperatures and their occurrences sorted by temperature from *a* to *b* in ascending order

The folder also includes 1tempdata.txt file with a set of temperature data (the monthly high temperatures at Heathrow Airport 1948 - 2016).

## [Plot Currency Rates](https://github.com/LSIND/intro-to-python3-analysis/tree/master/PlotCurrencyRates "PlotCurrencyRates")
The code (module **readxml**):
 - reads data from [Central Bank of Russia](http://www.cbr.ru/development/SXML/) containing currency information in XML-format:
 
 --  [XML with currency names and codes (ids)](http://www.cbr.ru/scripts/XML_val.asp?d=0). The code should retrieve the code from the provided name, f.e. Euro = R01239;
 -- [XML with currency rates](http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=02/03/2019&date_req2=05/10/2019&VAL_NM_RQ=R01239) depending on currency code and two dates. Element < Value >  contains ratio to Russian ruble at a specific date, f.e. 1 Euro = 71,3509 Rub at 05/10/2019 (dd/mm/YY);
 -- uses modules *urllib.request* and *xml.etree.ElementTree* to retrieve and parse XML data: 
     `from urllib.request import urlopen`
    `from xml.etree.ElementTree import parse`
    
The code (**main. py**)
- provides initial variables: currency name and two dates (period). You can change it or ask user for input.

     `cur = "Euro"`
     
     `startdate = "02.03.2019"`
     
     `enddate = "05.10.2019"`
- plots graph of currency rates Currency/Russian ruble using *matplotlib*, f.e 

![currency rates](https://lh3.googleusercontent.com/4iAVD73I8TtrtYFmqb-Ik8AeBDvDwoyPPZGvz-HO9mXstUMs7AJYPpma6xCzMgueMr9SHO4JFgIBYg=w1365-h937-rw | width=250)

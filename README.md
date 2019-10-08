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

The folder also includes 1tempdata.txt file with a set of temperature data (the monthly high temperatures at Heathrow Airport for 1948 through 2016).

## [Plot Currency Rates](https://github.com/LSIND/intro-to-python3-analysis/tree/master/PlotCurrencyRates "PlotCurrencyRates")
The code:
 - reads xml from [Central Bank of Russia](www.cbr.tu) containing currency [rates](http://www.cbr.ru/development/SXML/)
 

    from urllib.request import urlopen
    from xml.etree.ElementTree import parse
    
![alt text](https://uce0b41a9ce15d899c869ad3c691.previews.dropboxusercontent.com/p/thumb/AAmKM2Ig7gsQHqa4sCwXDjQ-7VHNF6tG_Q5he9AVHMkvoJFUhacjz_4tGB7jYurlEa5KV_GDK__eAXW5Zr9slSHNPpDVIALh8zdlq7j9HDEvr9P4zeT8RoVPdGvlhQAZOsXDP-KlaJR0_QwjbrHEyvToJ7Ko6r7fcZvBEX-FhThJkuTOLdTZcr0qBTNKq2lDKMpmMw-LII-5slsyzTjgDkdvX3Q_2j2zbEqL-7dbZvZXLkbI6BPGET-QSv6ihSutGmUyzT4nCYWdA2OpiodX4_kgfq44E8b5JnwjDs2o4_4ZZgWiMVSB-8WqgjImANx6Ib2Ji0Ah9t4-g7rw97Pep7AnSpVyP_BKnHl7BY9qILDtrX0iGHQL6coHYaB_og13D0A/p.jpeg?fv_content=true&size_mode=5)

# Weather forecasts accuracy

Gets forecasts made on different days, by several sources, for a city's weather (here we use Niterói, RJ, Brazil) and compares them with the actual temperatures, again using multiple sources, measured at that city.


## Motivation
_How often are weather forecasts wrong?_

Niterói is a mostly sunny city located on the coastline of Brazil, with many beaches by the Atlantic Ocean. Seasonal and monthly forecasts are, of course, vital for agricultural centered cites. For Niterói, shorter (a week or a few days long) forecasts are also invaluable, and dictate it's services (how much cold beverages should we have in stock?), leisure (are the beaches going to be overwhelmed by tourists?) and traffic conditions. 
And yet, it seems like the often predicted "This weekend, the weather is gonna change" is a phrase people tend to complete with "..well, maybe... It's just the forecast, so you never know."


## Questions

- Are aggregated forecasts more accurate then individual forecasts?, or...
- ...is there a single forecasts source that predicts the weather more accurately (at least for this city)?
- Does the forecasts change a lot on a day to day basis? (Do they update? If i checked the weekend forecasts on Monday, do I need to check them again on Friday? Are 5 days forecasts useless?)
- Do forecasts work only when the weather changes are small incremental changes, but fail when the weather really turns?


## Goals for the project's future

1) (TODO) Analyze the accuracy of probabilities of precipitation.
2) (TODO) Be used reliably by/at other cities.


## Methods

Extraction: runs, from a server, daily forecast **API** requests, and hourly temperature API requests, to international and national (Brazilian) weather services, and keeps the json responses. Those are **shell/bash scripts** on **cronjobs**, with one brief **php** xml to json conversion. They can be run locally without any changes to the files. Each weather forecast or temperature source has it's own .sh file, so as to be easy to choose and schedule the ones wanted.

Transformation: using **Object Oriented Python** running locally, fetchs the **json** data from the _local dirs_ (/Previsoes for forecasts and /Temperaturas for temperatures) and stores only the useful temperature objects on **Pandas** Dataframes and (TODO) in **CSVs**.

Analysis: (TODO) 


## Tech stack

You must be familiar with **Python's Pandas** library OR how to handle information in CSV (OR convert it to a preferred format) to use the weather data for analysis. 
You must be familiar with **shell/bash scripts** AND **Object Oriented Python** AND **json** files to add new weather forecasts sources to the work-flow.
You must be familiar with **cronjobs** OR other work-flow automation tools (such as Airflow or even GitHub actions) to set up the automated API requests on servers or locally). 


## Setup

Mandatory: You must use your own API keys for the weather forecasts sources (to use the project "right out of the box"), use a .API_keys folder on the parent directory of the bash/shell scripts). Each .sh comes with instructions on where to acquire said keys (if they are needed). Alternatively, just eliminate all .sh files that require API keys (useful for testing).

Optional: __If you wish to request your own city's weather information__, each .sh file also comes with instructions on where to acquire the code/name convention you need to assign to the variable city.

Semi-mandatory: It's recommended that the temperatures are retrieved once every hour to use the project "right out of the box". To change that would imply in changes in the python files.

Optional: You may simply ignore the failed conversion of the xmls file to json using php, as it's not critical, specially if you are not running the bash/shell scripts from a server OR if you don't have php locally. Alternatively, just convert the xml to json using your preferred tools.

Mandatory: Requirements for python environment are on the /Ferramentas (Tools) folder. Install with the usual `pip install -r "requirements.txt"`

## Licensing notes

The sources for weather forecasts and temperatures are API calls to providers, each with their own Licenses. They are of free use for non-commercial purpose (such as this investigation) and often offer subscriptions (and prices) for commercial use through their web sites. The author of this project has no commercial use intent of the information extracted form the sources. The included LICENSE applies to the code, but not the information on the API responses.


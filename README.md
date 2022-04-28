# Weather forecasts accuracy

Gets forecasts made on different days, by several sources, for a city's weather (here we use Niterói, RJ, Brazil) and compares them with the actual temperatures, again using multiple sources, measured at that city.


## Motivation
_How often are weather forecasts wrong?_

Niterói is a mostly sunny city located on the coastline of Brazil, with many beaches by the Atlantic Ocean. Seasonal and monthly forecasts are, of course, vital for aggricultural centered citys. For Niterói, shorter (a week or a few days long) forecasts are also invaluable, and dictate it's services (how much cold beaverages should we have in stock?), leisure (are the beaches going to be overwhelmed by tourists?) and traffic conditions. 
And yet, it seems like the often predicted "This weekend, the weather is gonna change" is a phrase people tend to complete with "..well, maybe... It's just the forecast, so you never know."


## Questions

- Are aggregated forecasts more accurated then individual forecasts?, or...
- ...is there a single forecasts source that predicts the weather more accuratly (at least for this city)?
- Does the forecasts change a lot on a day to day basis? (Do they update? If i checked the weekend forecasts on monday, do I need to check them again on friday? Are 5 days forecasts useless?)
- Do forecasts work only when the weather changes are small incremental changes, but fail when the weather really turns?


## Goals for the project's future

(TODO) Analyse the accuracy of probabilities of precipitation.
(TODO) Be used reliably by/at other cities.


## Methods

Extraction: runs, from a server, daily forecast **API** requests, and hourly temperature API requests, to international and national (Brazilian) weather services, and keeps the json responses. Those are **shell/bash scripts** on **cronjobs**, with one brief **php** xml to json conversion. They can be run locally without any changes to the files. Each weather forecast or temperature source has it's own .sh file, so as to be easy to choose and schedulle the ones wanted.
Transformation: using **Object Oriented Python** running localy, fetchs the **json** data from the _local dirs_ (Previsoes for forecasts and Temperaturas for temperatures) and stores only the useful temperature objects on **Pandas** Dataframes and (TODO) in **CSVs**.
Analysis: (TODO) 


## Licensing notes

The sources for weather forecasts and temperatures are API calls to providers, each with their own Lincenses. They are of free use for non-commercial purpose (such as this investigation) and often offer subscriptions (and prices) for commercial use through their web sites. The author of this project has no commercial use intent of the information extracted form the sources. The included LICENSE applyes to the code, but not the information on the API responses.

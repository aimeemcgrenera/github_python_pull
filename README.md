# Github API Python Repository Pull

## Description
This program retrieves the top 25 starred public Python repositories in Github via the Github API. Once the program retrieves the data, it pushes the following schema to Google Cloud BigQuery.

![alt text](https://i.imgur.com/r97X6bG.png)

The stored data includes the repository ID, name, URL, created date, last push date, description, and number of stars.
Each time this code is run, it will pull the most up to date data.


## Architecture
    ├── config                                    # folder to add additional conifguration files to
    |    ├── config_top_python_repos.json         # mock config  
    ├── env                                       # virtual enviornment
    |    ├── Include
    |    ├── Lib
    |    ├── Scripts
    |    ├──pyenv.cfg 
    ├── test 
        ├──test.py                                # unit tests  
    ├── main.py                                   # main python script
    ├── README.md                                                                
    ├── requirements.txt 
    └── ...

## Configuration 
To alter the API request or the BigQuery Project and/or Dataset you would like to push the data to, create a new configuration file. 
```
[
  {
    "jobs": [
        {
        "api": "Github",
        "api_url": "https://api.github.com/search/repositories",
        "api_query": "language:python",
        "api_sort": "stars",
        "api_order": "desc",
        "bq_project_id": "aerobic-ward-248616",
        "dataset_name": "outside_data",
        "datatable_name": "top_github_python_repos",
        "replace_table": true
        }
    ]
  }
]
```
    
## Installation Guide
* fork and clone this repository
* in terminal run `cd github_python_pull` to change directory and access the application
* run `.\env\Scripts\activate` to activate virtual environment
* run `pip install -r requirements.tx` to install the required packages
* create a config file based off the exisiting, replace the "bq_project_id" object with the BigQuery Project ID associated with your Gmail account.
* run `python main.py config/XXXX.json` replace XXXX with your new config file
* when running the code you will be prompted to give pandas_gbq access. Signin and give access, paste key provided in terminal
* once complete you will receive a logging message that the API pull has been pushed to BigQuery

## Contributions
Please contact me or open an issue before submitting any pull requests.

## License
This project has been licensed under the MIT open source license.

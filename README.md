# Github API Python Repository Pull

## Description
This program retrieves the top 25 starred public Python repositories in Github via the Github API. Once the program retrieves the data, it pushes the following schema to Google Cloud BigQuery.

![alt text](https://i.imgur.com/r97X6bG.png)

The stored data includes the repository ID, name, URL, created date, last push date, description, and number of stars.
Each time this code is run, it will pull the most up to date data.


## Architecture
    ├── config                                    # folder to add additional conifguration files to
    |    ├── config_top_python_repos.json         # mock config  
    ├── main.py                                   # main python script
    ├── README.md                                                                
    ├── requirements.txt                          # code dependencies
    ├── test.py                                   # unit tests  
    └── ...

## Configuration 
To alter the API request or the Google BigQuery destination you would like to push the data to, create a new configuration file. 
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
    `git clone https://github.com/aimeemcgrenera/github_python_pull.git`
* in terminal run `cd github_python_pull` to change directory and access the application
* install virtual environment to run code in 
    * Windows: `py -m pip install --user virtualenv`
    * MacOS & Linux: `python3 -m pip install --user virtualenv`
* create a virtual environment
    * Windows: `py -m venv env`
    * MacOS & Linux: `python3 -m venv env`
 * activate virtual environment
    * Windows: `.\env\Scripts\activate`
    * MacOS & Linux: `source env/bin/activate`
* run `pip install -r requirements.txt` to install the required packages
* create a config file based off the existing, replace the "bq_project_id" object with the BigQuery Project ID associated with your Gmail account; Also update the dataset and datatable you would like to push this data to in BigQuery
* run `python main.py config/XXXX.json` replace XXXX with your new config file
* when running the code you will be prompted to give pandas_gbq access; sign in to the Gmail account associated with your BigQuery account and give access, paste authorization code provided in terminal
* once complete you will receive a logging message that the API pull has been pushed to BigQuery
    `Successfully updated outside_data.top_github_python_repos in BigQuery`

## Contributions
Please contact me or open an issue before submitting any pull requests.

## License
This project has been licensed under the MIT open source license.

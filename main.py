import requests
import json
import pandas as pd
import logging
import sys


class GithubApiData():

    def __init__(self):
        """
         Initialize api Process
        """

        self.__log = logging.getLogger("github_API")
        self.__log.info('Initializing Github API call')

        # Read config file
        configfile = 'config/config_top_python_repos.json'  # default to original config file if config parameter isn't passed
        if len(sys.argv) > 1:
            configfile = sys.argv[1]

        self.__log.info('Reading Config Information')
        try:
            with open(configfile) as file:
                configs = file.read()
                config = json.loads(configs)
                self.__process_config(config)
        except:
            self.__log.error('Error Reading config file: ', sys.exc_info()[0])
            raise


    def __process_config(self, config):
        """

        Read info from config file and set variables

        :param: config

        """
        for item in config:
            for job in item['jobs']:
                self.__api = job['api']
                self.__api_url = job['api_url']
                self.__api_sort = job['api_sort']
                self.__api_order = job['api_order']
                self.__api_query = job['api_query']
                self.__bq_project_id = job["bq_project_id"]
                self.__data_set = job['dataset_name']
                self.__data_table = job['datatable_name']
                self.__replace = job['replace_table']


    def main(self):
       columns = ['repository_id', 'name', 'url', 'created_date', 'last_push_date', 'description', 'stars']
       response = self.api_call()
       rows = self.process_response(response)
       df = self.create_df(rows, columns)
       self.push_to_bq(df, self.__bq_project_id, self.__data_set, self.__data_table)

    def api_call(self):
        response = requests.request("GET", self.__api_url, params={"q": self.__api_query, "sort": self.__api_sort, "order": self.__api_order})
        return response

    def process_response(self, response):
        # json response to dictionary
        parsed_json = json.loads(response.text)
        # get items from dictionary
        repos = parsed_json['items']

        # limit to only top 25
        limit = 25
        i = 0
        rows = []

        # loop through repos and append data required for columns and create rows
        while (i < limit):
            rows.append([repos[i]['id'], repos[i]['name'], repos[i]['html_url'], repos[i]['created_at'], repos[i]['pushed_at'], repos[i]['description'], repos[i]['stargazers_count']])
            i += 1
        return rows

    def create_df(self, rows, columns):
        # using pandas library to create DataFrame
        try:
            df = pd.DataFrame(rows, columns=columns)
            print('Created dataframe to push to BQ')
        except:
            self.__log.error('Error creating data frame: ', sys.exc_info()[0])
            raise
        return (df)

    def push_to_bq(self, df, project_id, data_set, data_table):
        print('Updating ' + data_set + ' in BigQuery')
        destination_table = (data_set + "." + data_table)

        # added function_state for unittesting purposes
        function_state = True

        ifexists = 'append'
        if self.__replace is True:
            ifexists = 'replace'

        # using method .to_gbq in pandas library to push the dataframe to BQ
        # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_gbq.html
        try:
            df.to_gbq(destination_table, project_id, if_exists=ifexists)
        except:
            self.__log.error('Error pushing data frame to Big Query: ', sys.exc_info()[0])
            function_state = False
            return function_state
            raise

        print('Successfully updated ' + destination_table + ' in BigQuery')
        return function_state


processed_config = GithubApiData()
processed_config.main()

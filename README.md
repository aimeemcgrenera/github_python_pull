# Github API pull

## Description
This program retrieves the top 25 most starred public Python projects in Github via the Github API. Once it retrieves the data it pushes the following columns to Google Cloud BigQuery.
The stored data includes the repository ID, name, URL, created date, last push date, description, and number of stars.
Each time this code is run, it will pull the most up to date data.
You can denote the following by creating a config file.
To alter the API request or the BigQuery Project and/or Dataset you would like to push the data to, create a new configuration file. 


## Architecture


## Installation Guide
* Fork and clone this repository
* Make sure that the 
* `cd spotcheck` to change directory and access the application
* `bundle install` to install the required gems
* `rake db:migrate` to migrate the database
* `cd client` to move over to the client side of the application
* `npm install` to install dependencies
* `rake start` will start both the client and server side and run the application on your local server

## Contributions
Please contact me or open an issue before submitting any pull requests.

## License
This project has been licensed under the MIT open source license.

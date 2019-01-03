#### Dashboard for deployment on Heroku
This is basically a copy of the data_dashboard but with some changes for the deployment of heroku:
* app.run removed in *worldbank.py*
* *requirements.txt* added (Remember to create a virtual conda environment with --no-default-packages)
* *Profile* added with start command for unicorn
* *runtime.txt* added with python version

#### Run the app locally with
* python worldbank_local.py
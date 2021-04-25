The blocks of code are to be run in this order:
(1) web_scrape.py
(2) Clean_data.ipynb
(3) Explore_Data.ipynb
(4) Analysis_base.ipynb

web_scrape.py creates the data science job descriptions from scraping data off of LinkedIn.

Clean_data.ipynb takes the meta data, cleans it, adds additional information and saves the files back out.

Explore_Data.ipynb looks through the meta data and looks at the top results.

Analysis_base.ipynb takes the job descriptions, does some basic explotory analysis and trains a RNN to generate text.
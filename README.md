#Tehran house price

## What is this?
This is an scrapper that collects Tehran house prices from [divar.ir](https://divar.ir).
You can download the data from https://www.kaggle.com/amiralitaheri/tehranrealestateprices.

## How to run the spider?
1. Clone the repository.  
``git clone https://github.com/amiralitaheri/tehran-house-price.git``  
2. Go to project directory  
``cd tehran-house-price``  
3. Install requirements  
``pip install -r requirements.txt``
4. Run the scrapper  
``scrapy crawl divar-tehran-real-estate -o output.json``  
Depending on your network connection it may take 3 to 6 hours.

## What can I do with this data?
You can download the crawled data from https://www.kaggle.com/amiralitaheri/tehranrealestateprices  
I have created two notebooks that gives yo a place to start.
1. `data-statistics.ipynb`:  
Goes over the dataset and extract some basic statistic.
2. `clustering.ipynb`:
We create a simple cluster using K-means algorithm .

## Warning

Crawling can cause some unwanted pressure on websites and 
it may be illegal in some countries, use this crawler at your own responsibility. 
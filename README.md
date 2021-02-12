#Tehran house price

## What is this?
This is an scrapper that collects Tehran house prices from [divar.ir](https://divar.ir).
The sample output is in `/data/21-2-12/output.json`.

## How to run the spider?
1. Clone the repository.  
``git clone ``  
2. Go to project directory  
``cd tehran-house-price``  
3. Install requirements  
``pip install -r requirements.txt``
4. Run the scrapper  
``scrapy crawl divar-tehran-real-estate -o output.json``  
Depending on your network connection it may take 3 to 6 hours.

## What can I do with this data?
The sample data is in `/data/21-2-12/output.json`.
I have created two notebooks that gives yo a place to start.
1. `data-statistics.ipynb`:  
Goes over the dataset and extract some basic statistic.
2. `clustering.ipynb`:
We create a simple cluster using K-means algorithm .

## Warning

Crawling can cause some unwanted pressure on websites and 
it may be illegal in some countries, use this crawler at your own responsibility. 
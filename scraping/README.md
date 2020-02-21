# Data scraper for Facebook marketplace using Selenium Webdriver

**Requirements:** 
* Selenium Webdriver for your browser (Chrome in this case)
* Pandas

Data to be scraped : Rent, Number of bathrooms and Number of bedrooms, Area, Location.

1. Browse the facebook marketplace and click on "Rentals". Specify the Area in the filters and click apply.
2. Once the page loads, scroll down to load a good amount of rental listings, depending on your need. Let the page load completely for all the rentals listed on facebook marketplace for the particular area.
3. Copy the url of the page and paste it in the Jupyter notebook:

```wd.get("https://www.facebook.com/marketplace/xxxxxxxxx")```

Run jupyter notebook and the data will be saved in a csv file in the parent directory. Use the data to train machine learning models. :)

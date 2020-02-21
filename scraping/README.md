# Data scraper for Facebook marketplace using Selenium Webdriver

**Requirements:** 
* [Selenium Webdriver](https://www.selenium.dev/documentation/en/) for your browser (Chrome in this case)
* Pandas
<br>

**Data to be scraped:** Rent, Number of bathrooms and Number of bedrooms, Area, Location.

1. Browse the [facebook marketplace](https://www.facebook.com/marketplace/) and click on "Rentals". Specify the Area in the filters and click apply.
2. Once the page loads, scroll down to load a good amount of rental listings, depending on your need. Let the page load completely for all the rentals listed on facebook marketplace for the particular area.
3. Copy the url of the page and paste it in the Jupyter notebook:

```wd.get("https://www.facebook.com/marketplace/xxxxxxxxx")```

4. Change the for loop index to the number of listings you wish to scrape, make sure that sufficient entries are loaded on the Webdriver browser. 
5. It may so happen that the facebook XPath of the element may be changed, in that case *Inspect* the element in the browser and paste the *XPath* of the div that consists of the Rent and bedrooms/bathrooms details. 
6. This is a naive approach to scraping data, I will work on more robust approach in future.

Run jupyter notebook and the data will be saved in a .csv file in the parent directory. Use the data to train machine learning models. :)

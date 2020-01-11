<h1> Rent Estimate </h1>


__API Information__
* Parameters:
  * bedrooms [int][Number of bedrooms]
  * bathrooms [int][Number of bedrooms]
  * area [str][Location of the apartment from the ones in the Areas supported list]

* Return:
  * bedrooms
  * bathrooms
  * area
  * Rent Estimate


__url__ : /api/bedrooms=NO_OF_BEDROOMS&bathrooms=NO_OF_BATHROOMS&area=AREA

__Areas supported__ : 'Granite Bay', 'Loomis', 'Roseville', 'Sacramento', 'Carmichael',<br> 'Lincoln', 'West Sacramento', 'Davis', 'Citrus Heights', 'Orangevale', 'Rancho Cordova',<br> 'Antelope', 'Fair Oaks', 'McClellan', 'Placerville', 'Isleton', 'Vacaville', 'Lodi', 'Olivehurst', <br>'Applegate', 'Rio Linda', 'Acampo', 'Folsom', 'Shingle Springs', 'Canoga Park', 'Galt', 'Rio Vista',<br> 'El Dorado Hills', 'Auburn', 'Elk Grove', 'Woodland', 'Dixon', 'Rocklin', 'Esparto', 'Elverta', 'Sloughhouse', 'North Highlands'

__Instructions__ :
1. Run the `Flask_app.py` file.
2. The development server will start on the localhost.
3. Use the url mentioned above or on the homepage (localhost) to make a request.
4. Set the parameters, bathrooms,bedrooms,area(location) properly in the url and make the request.
5. It should return the response with the Rent Estimate.

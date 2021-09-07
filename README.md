## Task Description

Used Sqlalchemy orm to create models, Created models(tables) i.e continent,country,city with the required fields.
Used FastAPI to create api's.The Created api's interacts with database models and returns the respective result.

Application can perform Create,Read,Update,Delete operation on Continent,Country and City.

Some of the Api's:

get_continents: It will return the list of all the continents.

add_continent: It will add the continent.

delete_country:This api will delete the country according to the id passed.

Application also has some validation like if there are 2 cities in one country, the sum of the population of the 2 cities cannot be greater than the population of the country.

For example:
if total_population + country population is greater then parentcontinent population then it will raise a HTTPException that Population exceeds the total population of continent, update population of continent or reduce the population of the country. Well the database won't allow you for the create operation until you update population of continent or reduce the population of the countrySo this how one of the validation work's.

Steps to run the application:

1. open terminal in application root folder i.e wiki2
2. Run the below given command

```
docker-compose up
```

You'll find the root page with json response {"status":"running"}.This means your application is running successfully.
To check and implement all other api's: http://127.0.0.1:8000/docs#/ .Here you will find more then 15 api's that can be tested there itself. Here you can add, delete,read and delete the information(country,city,continent).

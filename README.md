# Bike_vs_Taxi_NYC
Comparing the efficiency of bikes versus taxis in New York City

This code was written for a school project. The goal is to compare the efficiency of riding a bike versus riding a taxi in New York City. The repository contains three datasets: data of the trip duration of taxis, data on the fares for taxi trips, and bike trip data. 

The two datasets with information regarding taxi trips in NYC were merged into a unified dataset based upon a trip ID number. Plots regarding the distribution of distance and trip times for both bikes and taxis are available in the repository. To compare the efficiency of the two modes of transportation in the city, a geographical box based upon latitude and longitude was created, and only trips that started and ended in this box were used for analysis. This method allows for fair comparisons, as all the trips start and end in roughly the same area.

A density plot of bike and taxi trip duration showed that they roughly had similar average trip lengths. Taxi trips appeared to be more normally distributed, while bike trips displayed a slight left skew. Bike trips had a slightly lower median duration than taxi trips (427.5 minutes for bikes vs 454.5 minutes for taxis). Bikes had a lower minimum trip duration, while also having a larger maximum trip duration, when compared to taxi trips. However, taxi trips had an average fare of $6.50, while this fee does not apply to bike trips, so this monetary factor should also be taken into account. 

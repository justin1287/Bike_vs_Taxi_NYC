
# Stat 5430
# Python Project

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

######## Make sure to run all previous code before starting new code

### Part 1: Taxi Data

trip_data=pd.read_csv("trip_data_10_subset.csv")

fare_data=pd.read_csv("trip_fare_10_subset.csv")

trip_and_fare_data=pd.merge(trip_data,fare_data)
any_dropped=False

earliest_start=min(trip_and_fare_data['_pickup_datetime'])
latest_start=max(trip_and_fare_data['_pickup_datetime'])
earliest_end=min(trip_and_fare_data['_dropoff_datetime'])
latest_end=max(trip_and_fare_data['_dropoff_datetime'])

trip_and_fare_data.groupby('medallion')['_hack_license'].apply(lambda x: x.nunique() == 1).all()
trip_and_fare_data[trip_and_fare_data['medallion'] == '0305D9CCDEECC106EE7BC4FD453986C9']['_hack_license']
tis_bijective=False

too_speedy=True

### Can be off by  a few seconds:
duration_is_consistent=False

plt.plot(trip_and_fare_data['_trip_time_in_secs'],trip_and_fare_data['_trip_distance'],'o')
plt.xlabel('Trip Time in Seconds')
plt.ylabel('Trip Distance in Miles')
plt.title('NYC Taxi Trip Time vs Distance ')


### Part 2: Bike Data

bike=pd.read_csv('2013-10_Citi_Bike_trip_data_20K.csv')

# There are a few large values that make the histogram skewed
plt.hist(bike['tripduration'],bins='auto',range=[0, 9000])
plt.xlabel('Trip Duration in Seconds')
plt.ylabel('Frequency')
plt.title('Distribution of Bike Trip Duration')

earliest_bike_start=min(bike['starttime'])
earliest_bike_end=min(bike['stoptime'])
latest_bike_start=max(bike['starttime'])
latest_bike_end=max(bike['stoptime'])

bike1=bike[bike['starttime']>='2013-10-01 07:00:00']
bike=bike1[bike1['stoptime']<='2013-10-01 12:52:19']


### Part 3: Comparisons

## 1)

lat=0.00362
lon=0.00476
start_lat_LB=bike[bike['start station id']==417]['start station latitude'][1773]-(lat/2)
start_lat_UB=bike[bike['start station id']==417]['start station latitude'][1773]+(lat/2)
start_lon_LB=bike[bike['start station id']==417]['start station longitude'][1773]-(lon/2)
start_lon_UB=bike[bike['start station id']==417]['start station longitude'][1773]+(lon/2)

a=np.where(trip_and_fare_data['_pickup_latitude']>start_lat_LB , 1, 0)
b=np.where(trip_and_fare_data['_pickup_latitude']<start_lat_UB , 1, 0)
c=np.where(trip_and_fare_data['_pickup_longitude']>start_lon_LB , 1, 0)
d=np.where(trip_and_fare_data['_pickup_longitude']<start_lon_UB , 1, 0)
trip_and_fare_data['start_in_region']= a+b+c+d==4

end_lat_LB=bike[bike['end station id']==534]['end station latitude'][1795]-(lat/2)
end_lat_UB=bike[bike['end station id']==534]['end station latitude'][1795]+(lat/2)
end_lon_LB=bike[bike['end station id']==534]['end station longitude'][1795]-(lon/2)
end_lon_UB=bike[bike['end station id']==534]['end station longitude'][1795]+(lon/2)

a2=np.where(trip_and_fare_data['_dropoff_latitude']>end_lat_LB , 1, 0)
b2=np.where(trip_and_fare_data['_dropoff_latitude']<end_lat_UB , 1, 0)
c2=np.where(trip_and_fare_data['_dropoff_longitude']>end_lon_LB , 1, 0)
d2=np.where(trip_and_fare_data['_dropoff_longitude']<end_lon_UB , 1, 0)
trip_and_fare_data['end_in_region']= a2+b2+c2+d2==4

## 2)

bike_target=bike[(bike['start station id']==417)&(bike['end station id']==534)]
taxi_target=trip_and_fare_data[(trip_and_fare_data['start_in_region']==True)&(trip_and_fare_data['end_in_region']==True)]
bike_target=pd.DataFrame(bike_target['tripduration'])
bike_target['travel_mode']='bike'
taxi_target=pd.DataFrame(taxi_target[['_trip_time_in_secs','_fare_amount']])
taxi_target['travel_mode']='taxi'
taxi_target=taxi_target.rename({'_trip_time_in_secs':'tripduration',},axis=1)

hola=pd.concat([bike_target,taxi_target])
target_trips=hola.rename({'tripduration':'dur_in_seconds','_fare_amount':'fare'},axis=1)

## 3)

bike_stats=pd.Series([min(bike_target['tripduration']),np.average(bike_target['tripduration']),statistics.median(bike_target['tripduration']),max(bike_target['tripduration'])])
taxi_stats=pd.Series([min(taxi_target['tripduration']),np.average(taxi_target['tripduration']),statistics.median(taxi_target['tripduration']),max(taxi_target['tripduration']),statistics.median(taxi_target['_fare_amount'])])

by_mode_stats=pd.concat([bike_stats,taxi_stats],axis=1)
by_mode_stats.columns=['Bike','Taxi']
by_mode_stats.index=['Minimum Duration','Mean Duration','Median Duration','Maximum Duration','Median Fare']
by_mode_stats=by_mode_stats.transpose()

## 4)

data_wide = target_trips.pivot(columns = 'travel_mode', values='dur_in_seconds')
data_wide.plot.density()
plt.xlabel('Trip Duration in Seconds')
plt.title('Density of Bike and Taxi Trip Duration')







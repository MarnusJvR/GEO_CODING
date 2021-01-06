import pandas
import geopy
from geopy.geocoders import ArcGIS

df1 = pandas.read_csv ('supermarket.txt')
print (df1)
nom = ArcGIS()
nom2 = nom.geocode('3995 23rd Street, San Francisco, CA 94114')
print (nom2)
print (nom2.longitude)
assert isinstance(nom2.latitude)
print (nom2.latitude)
df1['GPS Address']= df1['Address']+', '+ [] + df1['City']+ ', ' + df1['State'] + ', ' + df1['Country']
print (df1)

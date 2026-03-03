import geopandas as gpd
import matplotlib.pyplot as plt

# Put the FULL path to your .shp file here
world = gpd.read_file(r"C:\Users\sher khan\Downloads\ne_110m_admin_0_countries")

# Ethiopia Is Projected
ethiopia = world[world["ADMIN"] == "Ethiopia"]
ethiopia = ethiopia.to_crs(epsg=3857)

# Create Random Points (Fake Bus Stops)
import numpy as np
from shapely.geometry import Point

# Get Ethiopia boundary box
minx, miny, maxx, maxy = ethiopia.total_bounds

# Create 50 random points
points = []
for i in range(50):
    x = np.random.uniform(minx, maxx)
    y = np.random.uniform(miny, maxy)
    points.append(Point(x, y))

import geopandas as gpd

bus_stops = gpd.GeoDataFrame(geometry=points, crs=ethiopia.crs)
bus_stops = bus_stops[bus_stops.within(ethiopia.geometry.iloc[0])]

# Make Sure Everything Is Projected
ethiopia = ethiopia.to_crs(epsg=3857)
bus_stops = bus_stops.to_crs(epsg=3857)

# Create 50km Buffer (Large So You Can See It)
buffers = bus_stops.buffer(50000)

# Convert Buffers to GeoDataFrame
buffer_gdf = gpd.GeoDataFrame(geometry=buffers, crs=bus_stops.crs)

import geopandas as gpd
bus_stops = gpd.GeoDataFrame(geometry=points, crs=ethiopia.crs)

# Keep Only Points Inside Ethiopia
bus_stops = bus_stops[bus_stops.within(ethiopia.geometry.iloc[0])]

# Plot Everything Together
ax = ethiopia.plot(color="lightgray")

buffer_gdf.plot(ax=ax, color="blue", alpha=0.3)

bus_stops.plot(ax=ax, color="red", markersize=10)

plt.show()
import geopandas as gpd
import matplotlib.pyplot as plt

# Put the FULL path to your .shp file here
world = gpd.read_file(r"C:\Users\sher khan\Downloads\ne_110m_admin_0_countries")

# Ethiopia Is Projected
ethiopia = world[world["ADMIN"] == "Ethiopia"]
ethiopia = ethiopia.to_crs(epsg=3857)

# Create Random Points (Fake Bus Stops) / Split Ethiopia Into Grid (Simulated Regions)
import numpy as np
from shapely.geometry import box
from shapely.geometry import Point

# Get Ethiopia bounds
minx, miny, maxx, maxy = ethiopia.total_bounds

# Create 50 random points
points = []
for i in range(50):
    x = np.random.uniform(minx, maxx)
    y = np.random.uniform(miny, maxy)
    points.append(Point(x, y))

# Create grid size
rows = 4
cols = 4

width = (maxx - minx) / cols
height = (maxy - miny) / rows

grid_cells = []

for i in range(cols):
    for j in range(rows):
        x1 = minx + i * width
        y1 = miny + j * height
        x2 = x1 + width
        y2 = y1 + height
        grid_cells.append(box(x1, y1, x2, y2))
grid = gpd.GeoDataFrame(geometry=grid_cells, crs=ethiopia.crs)

bus_stops = gpd.GeoDataFrame(geometry=points, crs=ethiopia.crs)
# Keep Only Points Inside Ethiopia
bus_stops = bus_stops[bus_stops.within(ethiopia.geometry.iloc[0])]

# Make Sure Everything Is Projected
ethiopia = ethiopia.to_crs(epsg=3857)
bus_stops = bus_stops.to_crs(epsg=3857)

# Create 50km Buffer (Large So You Can See It)
buffers = bus_stops.buffer(50000)

# Convert Buffers to GeoDataFrame
buffer_gdf = gpd.GeoDataFrame(geometry=buffers, crs=bus_stops.crs)

# Clip Grid To Ethiopia
regions = gpd.overlay(grid, ethiopia, how="intersection")

# Count Bus Stops Per Region (Spatial Join)
joined = gpd.sjoin(bus_stops, regions, how="left", predicate="within")

counts = joined.groupby("index_right").size()

regions["bus_stop_count"] = counts
regions["bus_stop_count"] = regions["bus_stop_count"].fillna(0)

# Visualize Regional Inequality
ax = regions.plot(column="bus_stop_count", cmap="Reds", legend=True)
ax.set_title("Bus Stops per Region (Simulated)")
bus_stops.plot(ax=ax, color="red", markersize=10)
plt.show()
import geopandas as gpd
import matplotlib.pyplot as plt

# Put the FULL path to your .shp file here
world = gpd.read_file(r"C:\Users\sher khan\Downloads\ne_110m_admin_0_countries")

ethiopia = world[world["ADMIN"] == "Ethiopia"]

ethiopia_projected = ethiopia.to_crs("ESRI:102022")
area_km2 = ethiopia_projected.area / 1_000_000
print(area_km2)

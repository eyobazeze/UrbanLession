import geopandas as gpd
import matplotlib.pyplot as plt

# Put the FULL path to your .shp file here
world = gpd.read_file(r"C:\Users\sher khan\Downloads\ne_110m_admin_0_countries")

ethiopia = world[world["ADMIN"] == "Ethiopia"]

ethiopia.plot()
plt.show()
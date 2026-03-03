# Load in GeoPandas
import geopandas as gpd
import matplotlib.pyplot as plt

# Load regional boundaries (ADM1)
ethiopia = gpd.read_file("data/ethiopia/eth_admin1.shp")

# Plot Regions
ethiopia.plot()
plt.title("Ethiopia Regions (ADM1)")
plt.show()
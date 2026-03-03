# Load in GeoPandas
import geopandas as gpd
import matplotlib.pyplot as plt

# Load regional boundaries (ADM1)
ethiopia = gpd.read_file("data/ethiopia/eth_admin1.shp")

# Reproject to Meter-Based CRS
ethiopia_proj = ethiopia.to_crs(epsg=32637)

# Calculate Area Properly
ethiopia_proj["area_sqkm"] = ethiopia_proj.area / 1_000_000
# See Result
print(ethiopia_proj[["adm1_name", "area_sqkm"]])

# Plot Area Map (Choropleth)
ethiopia_proj.plot(
    column="area_sqkm",
    legend=True,
    cmap="OrRd"
)

plt.title("Area of Ethiopia Regions (sq km)")
plt.show()
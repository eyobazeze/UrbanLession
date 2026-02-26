import geopandas as gpd
import matplotlib.pyplot as plt

# Put the FULL path to your .shp file here
world = gpd.read_file(r"C:\Users\sher khan\Downloads\ne_110m_admin_0_countries")

#print(world.columns)
world_equal = world.to_crs("ESRI:102022")
world_equal["area_km2"] = world_equal.area / 1_000_000
world_equal["density"] = world_equal["POP_EST"] / world_equal["area_km2"]

ax = world_equal.plot(
    column="density",
    cmap="viridis",
    legend=True
)

ax.set_title("Population Density (People per km²)")

plt.show()

ethiopia = world_equal[world_equal["ADMIN"] == "Ethiopia"]

print(ethiopia[["ADMIN", "POP_EST", "area_km2", "density"]])
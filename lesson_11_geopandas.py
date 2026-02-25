import geopandas as gpd
import matplotlib.pyplot as plt

# Put the FULL path to your .shp file here
world = gpd.read_file(r"C:\Users\sher khan\Downloads\ne_110m_admin_0_countries")

#print(world.columns)
ethiopia = world[world["ADMIN"] == "Ethiopia"]
ax = world.plot(column="POP_EST", cmap="Blues", legend=True, edgecolor="black", linewidth=0.3)
ax.set_title("World Population Distribution")
plt.show()
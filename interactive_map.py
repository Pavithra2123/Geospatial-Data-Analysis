
import pandas as pd
import folium

# Load dataset
data = pd.read_csv("geospatial_data.csv")

# Create map centered on India
india_map = folium.Map(
    location=[22.5, 80.0],
    zoom_start=5
)

# Add city markers
for index, row in data.iterrows():

    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f'{row["Location"]} - Population: {row["Population"]}',
        tooltip=row["Location"],
        icon=folium.Icon(color="blue")
    ).add_to(india_map)

# Save interactive map
india_map.save("india_geospatial_map.html")

print("Interactive map created successfully!")

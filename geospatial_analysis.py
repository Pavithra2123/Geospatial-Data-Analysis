
import pandas as pd
import matplotlib.pyplot as plt

# Load geospatial dataset
data = pd.read_csv("geospatial_data.csv")

# Display dataset
print("GEOSPATIAL DATA")
print(data)

# Basic information
print("\nDATASET INFORMATION")
print(data.info())

# Statistical analysis
print("\nSTATISTICAL SUMMARY")
print(data.describe())

# Population by location
print("\nPOPULATION BY CITY")
print(data[["Location", "Population"]])

# Bar chart
plt.figure(figsize=(10, 6))
plt.bar(data["Location"], data["Population"])

plt.title("Population Distribution by City")
plt.xlabel("City")
plt.ylabel("Population")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("population_chart.png")
plt.show()

# Latitude and Longitude visualization
plt.figure(figsize=(10, 6))
plt.scatter(
    data["Longitude"],
    data["Latitude"],
    s=data["Population"] / 10000,
    alpha=0.6
)

for i in range(len(data)):
    plt.text(
        data["Longitude"][i],
        data["Latitude"][i],
        data["Location"][i]
    )

plt.title("Geographical Distribution of Indian Cities")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.tight_layout()
plt.savefig("geographical_distribution.png")
plt.show()

print("\nGEOSPATIAL DATA ANALYSIS COMPLETED!")

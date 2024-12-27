import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
data = pd.read_csv("final.csv")

# Create a new DataFrame with the desired structure
result = pd.DataFrame(columns=["Profession", "Emu", "Emu %", "SC", "SC %", "SDXL", "SDXL %", "DALLE", "DALLE %"])

# Populate the new DataFrame
for index, row in data.iterrows():
    profession = row["Profession"]
    emu_gender = "Male" if row["Emu_M%"] > row["Emu_F%"] else "Female"
    emu_value = row["Emu_M%"] if row["Emu_M%"] > row["Emu_F%"] else row["Emu_F%"]
    
    sc_gender = "Male" if row["SC_M%"] > row["SC_F%"] else "Female"
    sc_value = row["SC_M%"] if row["SC_M%"] > row["SC_F%"] else row["SC_F%"]
    
    sdxl_gender = "Male" if row["SDXL_M%"] > row["SDXL_F%"] else "Female"
    sdxl_value = row["SDXL_M%"] if row["SDXL_M%"] > row["SDXL_F%"] else row["SDXL_F%"]
    
    dalle_gender = "Male" if row["DALLE_M%"] > row["DALLE_F%"] else "Female"
    dalle_value = row["DALLE_M%"] if row["DALLE_M%"] > row["DALLE_F%"] else row["DALLE_F%"]
    
    # Append the results
    result = pd.concat([result, pd.DataFrame({
        "Profession": [profession],
        "Emu": [emu_gender], "Emu %": [emu_value],
        "SC": [sc_gender], "SC %": [sc_value],
        "SDXL": [sdxl_gender], "SDXL %": [sdxl_value],
        "DALLE": [dalle_gender], "DALLE %": [dalle_value]
    })], ignore_index=True)

# Update SC value for the profession "architect" to "-"
result.loc[result["Profession"] == "architect", "SC"] = "-"
result.loc[result["Profession"] == "architect", "SC %"] = "-"  # Optionally update the percentage column as well

# Plot the table with improved styling
fig, ax = plt.subplots(figsize=(12, len(result) * 0.6))  # Adjust figure size for better readability
ax.axis("off")

# Create the table
mpl_table = ax.table(
    cellText=result.values,
    colLabels=result.columns,
    loc="center",
    cellLoc="center",
    bbox=[0, 0, 1, 1]  # Scale the table to fill the axes
)

# Apply styling
mpl_table.auto_set_font_size(False)
mpl_table.set_fontsize(10)

# Set column widths: Manually adjust the first column width
for i, column in enumerate(result.columns):
    if column == "Profession":
        mpl_table.auto_set_column_width([i])  # Reduce width of the first column
        for row in range(len(result) + 1):  # Include header
            mpl_table[(row, i)].set_width(0.2)  # Set smaller width for the first column
    else:
        mpl_table.auto_set_column_width([i])  # Adjust other columns dynamically

# Apply cell colors for better visuals
for (row, col), cell in mpl_table.get_celld().items():
    if row == 0:  # Header row
        cell.set_facecolor("lightblue")  # Green header background
        cell.set_text_props(weight="bold", color="white")
    elif row % 2 == 0:  # Alternate row colors
        cell.set_facecolor("#f2f2f2")
    else:
        cell.set_facecolor("#ffffff")

# Save the table as an image
plt.savefig("adjusted_table_with_dash.png", bbox_inches="tight", dpi=300)
plt.close()

print("Table saved as 'adjusted_table_with_dash.png'")

import matplotlib.pyplot as plt

# Data for the chart
professions = [
    'a person cooking in the kitchen','accountant','administrative assistant','astronaut','athlete','AI researcher','architect','CEO','CFO','chef','chemical engineer','computer engineer','director','data scientist','doctor','driver','engineer','hair stylist','housekeeper','nurse','lawyer','librarian','pilot','politician','professor','receptionist','salesperson','scientist','surgeon','teacher'
]
male_probabilities = [32.75, 82.50, 12.50, 72.00, 67.50, 61.75, 72.33, 77.50, 76.00, 81.50, 81.50, 72.00, 76.25, 75.00, 76.50, 85.25, 77.75, 23.75, 36.75, 8.50, 79.00, 38.00, 75.75, 95.50, 76.00, 61.75, 84.75, 72.00, 74.50, 43.25]
female_probabilities = [67.25, 17.50, 87.50, 28.00, 32.50, 38.25, 27.67, 22.50, 24.00, 18.50, 18.5, 28.00, 23.75, 25.00, 23.50, 14.75, 22.25, 76.25, 63.25, 91.5, 21.00, 62.00, 24.25, 4.50, 24.00, 38.25, 15.25, 28.00, 25.50, 56.75]

# Bar chart settings
bar_width = 0.4
index = range(len(professions))

# Create the figure and axis with adjusted size to fit 30 professions
fig, ax = plt.subplots(figsize=(18, 10))

# Plot male and female probabilities side by side with the requested colors
bar1 = ax.bar(index, male_probabilities, bar_width, label='Male', color='lightblue')  # Blue for Male
bar2 = ax.bar([i + bar_width for i in index], female_probabilities, bar_width, label='Female', color='pink')  # Red for Female

# Adding titles and labels
ax.set_xlabel('Profession')  # X-axis title
ax.set_ylabel('Probability (%)')  # Y-axis title
ax.set_title('Binomial Distribution of Male vs. Female Probabilities by Profession - Across 4 Models')  # Chart title

# Adjust the position of the x-axis label closer to the ticks
ax.xaxis.set_label_coords(0.5, -0.16)  # Move the x-axis label closer to the axis (adjust y-position)

# Setting x-ticks to the profession names and adjusting positions
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(professions, rotation=45, ha='right')  # Rotate labels for better fit

# Setting y-axis limit to 100 (since we're dealing with percentages)
ax.set_ylim(0, 100)

# Adding data labels on top of each bar with adjusted positioning
# Male data labels
for bar in bar1:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval:.2f}%', ha='center', va='bottom', fontsize=8.5)

# Female data labels with an additional horizontal offset to avoid overlap
for bar in bar2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval:.2f}%', ha='center', va='bottom', fontsize=8.5)

# Adding a legend
ax.legend()

# Show the plot
plt.tight_layout()

plt.savefig("7.png", dpi=300, bbox_inches='tight')



# Step 1: Create a list of 4 colors and store it as a variable.
original_colors = ["Red", "Green", "Blue", "Yellow"]

# Step 2: Use a method to add 3 more colors to the list in a single statement.
original_colors.extend(["Orange", "Purple", "Pink"])

# Step 3: Use a different method to add one additional color to the list.
original_colors.append("Brown")

# Step 4: Use a method to insert a new color at index 3.
original_colors.insert(3, "Cyan")

# Step 5: Use a method to create a copy of the list.
copied_colors = original_colors.copy()

# Step 6: Use a method to remove one element from the copy of the list.
removed_color = copied_colors.pop(2)

# Step 7: Print the original and copied lists to observe the changes.
print("Original Colors:", original_colors)
print("Copied Colors:", copied_colors)

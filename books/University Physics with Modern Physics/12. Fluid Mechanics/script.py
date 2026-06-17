import os

# Start at 121, end at 88 (since range stops before the end number, 88 ensures 87 is included)
# We increment by 2 to get 12.1, 12.3, 12.5, etc.
for i in range(1, 89, 2):
    # Convert back to a float (e.g., 121 becomes 12.1, 127 becomes 12.7, 1287 becomes 12.87)
    
    # Convert to string to name the directory
    dir_name = "12."+str(i)
    
    # Create the directory and the empty file
    os.makedirs(dir_name, exist_ok=True)
    with open(os.path.join(dir_name, "a.md"), "w") as f:
        pass

print("Directories and files created successfully!")
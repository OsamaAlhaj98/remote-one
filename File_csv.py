# Step 1: Open the file
with open('students.csv', 'r') as f:
    lines = f.readlines()  # Reads all lines into a list

# Step 2: Parse the header
header = lines[0].strip().split(',')  # ['Name', 'Age', 'Grade']

# Step 3: Process data lines
print("Students who got grade A:")
for line in lines[1:]:  # Skip the header
    fields = line.strip().split(',')  # Split by comma
    name, age, grade = fields[0], fields[1], fields[2]
    
    if grade == 'A':
        print(f"{name} (Age: {age})")
# Create a new file called 'my_notes.txt'
with open('my_notes.txt', 'w') as f:
    # Write some notes to the file
    f.write('Nota 1\n')
    f.write('Nota 2\n')
    f.write('Nota 3\n')

# Read the contents of the file line by line
with open('my_notes.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Close the file
f.close()
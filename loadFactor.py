import csv

class HashMap:
    def __init__(self, initial_capacity=10, load_factor=0.75):
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * self.capacity

    def insert(self, key, value):
        # Check if load factor exceeds the threshold
        if self.size >= self.load_factor * self.capacity:
            # Resize the hashmap
            self._resize()

        # Calculate the hash code and index
        index = hash(key) % self.capacity

        # Insert key-value pair into the appropriate bucket
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))

        self.size += 1

    def _resize(self):
        # Double the capacity and create a new table
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        # Rehash all entries and insert into the new table
        for bucket in self.table:
            if bucket is not None:
                for key, value in bucket:
                    index = hash(key) % new_capacity
                    if new_table[index] is None:
                        new_table[index] = [(key, value)]
                    else:
                        new_table[index].append((key, value))

        # Update capacity and table reference
        self.capacity = new_capacity
        self.table = new_table

    def retrieve(self, key):
        # Calculate the hash code and index
        index = hash(key) % self.capacity

        # Search for the key in the appropriate bucket
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v

        # Key not found
        return None

# Example usage with dataset from CSV file
hashmap = HashMap()

# Read titles from CSV file
with open('C:\\Users\\Ronan\\Documents\\bachelor_thesis-main111\\dataset\\clickbait_dataset.csv', 'r') as file:
    csv_reader = csv.reader(file)
    # Assuming the first column contains the titles
    titles = [row[0] for row in csv_reader]

# Insert titles into the hashmap
for title in titles:
    hashmap.insert(title, True)  # Assuming True as the value for simplicity

# Retrieve values for specific titles
print(hashmap.retrieve("Your specific title 1"))
print(hashmap.retrieve("Your specific title 2"))

helloWorld = ['hello','world','1','2']

# Convert to a dictionary

helloWorldDictionary = dict(zip(helloWorld[0::2], helloWorld[1::2]))

# Print out the result
print(helloWorldDictionary)

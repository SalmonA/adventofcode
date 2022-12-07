with open('input.txt', 'r') as f:
    message = f.readline()

# marker_length = 4
marker_length = 14

for i in range(len(message)):
    if len(set(message[i:i + marker_length])) == marker_length:
        print(i + marker_length)
        break
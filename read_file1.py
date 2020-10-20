try:
    #user input for file
    filename = input("Please enter a file name to read: ")

    #Reading file
    fi = open(filename, 'r')
    read_file = fi.read()
    print(read_file)

#Throw exception on file not found
except FileNotFoundError as err:
    print(f"Error: {err}")

finally:    
    #closing file
    fi.close()

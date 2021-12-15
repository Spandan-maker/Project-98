from time import sleep

def swapContent():
    file1 = input("Enter the name of the first file: ")
    file2 = input("Enter the name of the second file: ")

    print("Processing. . .")
    sleep(1.5)
    
    #Opening file
    with open(file1, "r") as a:
        data_1 = a.read()

    print("Reading data. . .")
    sleep(1.5)

    with open(file2, "r") as a:
        data_2 = a.read()

    #Swapping file data
    with open(file1, "w") as b:
        b.write(data_2)

    print("Swapping. . .")
    sleep(1)

    with open(file2, "w") as b:
        b.write(data_1)

    print("Data of the files have been swapped.")

swapContent()
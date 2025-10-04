# file = open("order.txt" , "w")
# try:
#     file.write("Chai with milk and sugar")
# finally:
#     file.close()
# Using finally to ensure the file is closed after writing, regardless of whether an error occurs during the write opertaion.

with open("order.txt" , "w") as file:
    file.write("Welcome to chai shop")
# Using with statement to handle file operations. The file is automatically closed after the block is executed.

# as we use the with statement , it runs a dunder method __enter__ when the block is entered and __exit__ when the block is exited , ensuring proper resource management.
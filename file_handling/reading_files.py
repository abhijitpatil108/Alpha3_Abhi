path = r"C:\Users\Vidya\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"

# with open(path) as f:
#     data = f.read()
#     print(data)
#     print(f.tell())
#     f.seek(0)
#     print(f.read(10))

# with open(path) as file:
#     print(file.readline(10))    # reads 10 characters from the first line
#     print(file.readline(5))     # reads 5 characters after the previous output
#     print(file.readline())      # reads the left out characters in the line


with open(path) as file:
    print(file.readlines())








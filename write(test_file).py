import os

def write_test(file_size_limit=2*1024**3):  # 2GB
    i = 1
    with open('test.txt', 'w') as f:
        while os.path.getsize('test.txt') < file_size_limit:
            f.write('test({})\n'.format(i))
            i += 1

# Call the function
write_test()

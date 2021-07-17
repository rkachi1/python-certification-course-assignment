# what is a file

# open a file()

def main():
    newFile = open('Test','w')
    newFile.write('First line in the file\n')
    newFile.write('second line in the file')
    newFile.close()
main()


# read a file ()
# if you use write mode then probably it will overwrite the content 
# and the previous content will disappear since this is a default
# nature of the write mode
# if you to write to the same file then you can use the append mode

# 

# close a file - close()
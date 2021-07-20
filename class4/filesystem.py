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

# Difference between a and w mode
# When file exists - w mode actually clears the content 
# When file exists - a mode does not clear the content 
# it just appends to it 

# read a file
newFile = open('Test','r')
readingFileContent = newFile.read()
print(readingFileContent)

# close a file - close()

# seeks helps to read the file 

# For example if we have to read the file twice once the file is read
# the cursor comes to end of the file and it will have nothing to read
# after that. Hence this is where seeks comes into play

str = 'abc123'




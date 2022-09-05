
def counter(fname):
    num_words = 0
    num_lines = 0
    num_charc = 0
    num_spaces = 0  
    with open(fname, 'r') as f:
        for line in f:      
            num_lines += 1   
            word = 'Y'      
            for letter in line:          
                if (letter != ' ' and word == 'Y'):       
                    num_words += 1       
                    word = 'N'     
                elif (letter == ' '):         
                    num_spaces += 1       
                    word = 'Y'
                for i in letter:
                    if(i !=" " and i !="\n"):
                        num_charc += 1                      
    print("Number of words in text file: ", num_words)
    print("Number of lines in text file: ", num_lines)
    print('Number of characters in text file: ', num_charc)
    print('Number of spaces in text file: ', num_spaces)
      
# Driver Code: 
if __name__ == '__main__': 
    fname = 'file.txt'
    try: 
        counter(fname) 
    except: 
        print('File not found')
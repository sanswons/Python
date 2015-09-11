import urllib

def read_text():
    quotes=open(r"F:\sanjana\books\CSE\python\Programs\movie_quotes.txt")
    contents=quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection=urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output=connection.read()
   
    connection.close()

    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("No curse words")
    else:
        print("Could not scan properly")
    
read_text()

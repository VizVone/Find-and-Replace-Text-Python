import re,sys,time
# File Handling and extracting text from file
def filmang(fname):
    try:
        f=open(fname,"r")
        data=f.read()
        f.close()
        return data
    except:
        print("**Please Enter Correct File name and file extension**\n *The Program would Terminate in Next Five Seconds*")
        time.sleep(5)
        sys.exit(1)
# Searching for specifed characters
def searching(find):
    result=re.findall(find,data)
    return result
# Counts number of occurances of specified word 
def occurances(s):
    no=0
    for i in (s):
        no+=1
    return no
# Gives Results of the required data
def mainfun(find):
    i=0
    sentences=["Exactly same typed character","Same typed but in lowercase character","Same typed but in Uppercase character","Same typed but in Capitalized character"]
    fun=["find","find.lower()","find.upper()","find.capitalize()"]
    leng=len(sentences)
    for i in range(leng):
        find=eval(fun[i])
        s=searching(find)
        if(s==[]):
            print("----------------------------\n{}\nNo Match Found\nNumber of Occurances 0".format(sentences[i]))
        else:
            n=occurances(s)
            for j in s:
                print("----------------------------\n{}\n{}\nNumber of Occurances {}".format(sentences[i],j,n))
                break
# User input and important Function calling is done from here
fname=input("**Use only .txt extension files**\nEnter File Name with extension\n")
data=filmang(fname)
find=input("Enter characters you want to find\n")
mainfun(find)
q=input("Enter q to Quit\n")

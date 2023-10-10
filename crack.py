import zipfile
from time import time

'''


Zip password cracker
By Dictionary password attack
Using Python


'''

def main():
    try:
        myZip = zipfile.ZipFile("encrypted.zip")
    except zipfile.BadZipfile:
        print "There was an error opening your zip file."
        return

    password = ''
    
    print "Password cracking started..."
    print " "
    print "Please wait...."
    timeStart = time()
    with open("passwords.txt", "r") as f:
        passes = f.readlines()
        for pass_count, x in enumerate(passes):
            password = x.strip()
            try:
                myZip.extractall(pwd = password)
                totalTime = time() - timeStart
                print "\nPassword cracking successful: %s\n" % password
                print "%i Password tried per second " % (pass_count/totalTime)
                print " "
                return
            except Exception as e:
                if str(e[0]) == 'Bad password for file':
                    pass # TODO: properly handle exceptions?
                elif 'Error -3 while decompressing' in str(e[0]):
                    pass # TODO: properly handle exceptions?
                else:
                    print e
        print "Please try another passwords list file"

if __name__ == '__main__':
	main()

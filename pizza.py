import bs4 as bs
import urllib.request
import time
import hashlib
import smtplib
import shutil

while True:

    source = urllib.request.urlopen('[Site to be scraped]').read()
    soup = bs.BeautifulSoup(source,'lxml')

    '''
    #Download the intial HTML file
    file = open('site.txt', 'w')
    file.write(soup.text)
    file.close
    '''

    with open('site.txt', 'r') as f:
        original = hashlib.md5(f.read().encode('utf-8')).hexdigest()#encode

    temp = open('temp.txt', 'w')
    temp.write(soup.text)
    temp.close

    with open('temp.txt', 'r') as r:
        tempHash = hashlib.md5(r.read().encode('utf-8')).hexdigest()

    print("check")

    if original != tempHash:

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("[e-mail of server]", "[password]")

	#Send e-mail to client
        msg = "\nWebsite has been updated!!"
        server.sendmail("[e-mail of server]", "[e-mail od client]", msg)
        server.quit()
	
	#Replace the old '.txt' file with the new one
        shutil.copy('temp.txt', 'site.txt')

    time.sleep(3600)


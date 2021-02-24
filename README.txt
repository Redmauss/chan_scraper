https://github.com/Redmauss/chan_scraper

This is a program I made in python for easy downloading of images from a 4chan thread.  I made this so I could easily download batches of wallpapers from wg, but you can use this program with any board on 4chan. 

Installation Requirements:
1. Firefox must be installed. 
2. Selenium must be installed for python, with `pip install selenium`

2. Geckowebdriver for selenium must be installed, directions here:
https://selenium-python.readthedocs.io/installation.html
3. Latest version of Python 3 must be installed. 

The instructions is as follows:
1. Input board to be searched
2. Ask keyword to search for(wgscraper searches in thread titles)
3. chanscraper will now start searching through the thread titles for your keyword.  Thread titles will appear in the output.  If you want to download the thread, type "yes".  If you want to keep searching, type "no". 
4. Type the filename you want for the files.  If you type "image" for filename, the folder with the files will all be named image + number of file downloaded.  So the first image will be image1 and the 35th image will be named image35 and so on.  
5. Type the path you want to save the files.  It must be the full path in order to work, an example would be:
/home/user/Downloads/
6. The thread will be saved with the thread title as the foldername plus the date.  You can download another thread by entering "yes" to the last prompt, or "no" to end the program. 

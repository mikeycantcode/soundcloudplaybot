import os #for interface
import time #for time
from selenium import webdriver #to add plays
import threading #to automate threads
import random #randomize time


class Soundcloud: #main class
    def __init__(self):
        self.playsgiven = 0      #current amount of plays
        self.lock = threading.Lock()    #lock thread


                   #ask for parameters
        try:
            self.playamount = int(input('>enter play thread amount: '))
        except ValueError:
            self.close('ERROR: integer expected please restart')
        try:
            self.song_link = input('>enter song url in this format: username/songurl: ')
        except IndexError:
            self.close('ERROR: format expected: username/songurl' )
        try:
            self.webdriver_location = input('webdriver location please enter with / instead of \\: ')
        except IndexError:
        	self.close('ERROR: man just follow the instructions')
        else:
            print()


                    #define unexpected close function
    def close(self, message):
        print(f'\n{message}')
        os.system('title soundcloud bot - fatal error restart')
        os.system('pause >NUL')
        os.system('title soundcloud bot - press any button to exit')
        os._exit(2)


                 #currently useless because i switched from requests based
    def status(self, code, intention):
        if code == 200:
            self.playsgiven += 1
        else:
            self.lock.acquire()
            print(f'somethings fucked: {intention} error code: {code}')
            self.lock.release()
            self.bot()
    
                 #updates title and shows thread progress
    def update_title(self):
        while self.playsgiven == 0:
            time.sleep(0.2)

        while self.playsgiven < self.playamount:
            os.system(
                f'title soundcloud bot by @curlyyy.mike || plays added: {self.playsgiven}/{self.playamount} '
                f'({round(((self.added / self.playamount) * 100), 3)}%) ^| active threads: '
                f'{threading.active_count()} ^|'
            )
            sleep(0.2)

    def bot(self):
        try:
            soundcloud_url = 'https://www.soundcloud.com/'
            track_url = soundcloud_url + self.song_link

            i = False
            while i == False:
                driver = webdriver.Chrome(self.webdriver_location) #opens webdriver REMEMBER TO ADD WEBDRIVER TO FOLDER
                driver.get(track_url)
                driver.set_window_size(1000, 1000) 
                driver.find_element_by_class_name('playButton').click() #clicks webdriver
                time.sleep(random.uniform(10,30))
                i = True
                print(self.playsgiven) #literally something is fucked with these two variables
                print(self.playamount)
                driver.close()
                if self.playamount > 5 and self.playsgiven < self.playamount: #i dont even remember what i was trying to do here bro
                	time.sleep(15)
                	self.bot()  

        except Exception as e:
            print(f'error: {e}')
            self.bot()
        else:
            if all(i not in response.text for i in ['plays unavailable', 'connection timed out']):
                self.status(response.status_code, response.text)
            else:
                self.bot()



    def start(self):

    	#fake ass progress bar to scam dumb soundcloud rappers lmfaooooo

        items = list(range(0, 47))
        l = len(items)

        # defining fake ass progress bar function
        def fakeprogressbar (iteration, total, word1 = '', word2 = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
            percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
            fulllength = int(length * iteration // total)
            bar = fill * fulllength + '-' * (length - fulllength)
            print(f'\r{word1} |{bar}| {percent}% {word2}', end = printEnd)
            if iteration == total: 
            	print()

        #calling fake ass progress bar 
        fakeprogressbar(0, l, word1 = 'connecting:', word2 = 'complete', length = 50)
        for i, item in enumerate(items):
            time.sleep(0.1)
            fakeprogressbar(i + 1, l, word1 = 'connecting:', word2 = 'complete', length = 50)







		    #starting threads
        self.start_time = time.time()
        threading.Thread(target=self.update_title).start()

        for _ in range(self.playamount):
            while True:
                if threading.active_count() <= 300:
                    threading.Thread(target=self.bot).start()
                    break
                    #why does it not fucking end idk
        os.system('pause >NUL')
        os.system('thank you for using soundcloud bot - follow me on ig;)')
        sleep(3)


#main
if __name__ == '__main__':
	os.system('cls && title soundcloud bot - follow me on instagram @curlyyy.mike')
	main = Soundcloud()
	main.start()
import time
import webbrowser
import pyautogui as pg
from datetime import date
from imap_tools import MailBox, Q
import os


''' 1)Logs into the GMail address 
    2)Checks the inbox folder and looks for messages that were sent on that current date 
        and contain the word "Attendance".
    3)If a message is found it will be written into attendance_messages.txt
        with the number of urls parsed. 
'''
def find_attendance_messages(server, mail, password):
    mailbox = MailBox(server)
    mailbox.login(mail, password, initial_folder='inbox')
    f = open('attendance_messages.txt.', 'w')
    counter = 0
    for message in mailbox.fetch(Q(text='Attendance', date=date.today())):
        f.write(message.text)
        counter += 1
        f.write('=====================================================================================\n')
    f.write(f'\n{counter} URLS were generated.')
    f.close()
    mailbox.logout()

# Opens the attendance_messages.txt, finds and appends to the links list attendance URL links.
def get_urls(message_path, links):
    inFile = open(message_path, 'r')
    for line in inFile:
        if "https://forms.office.com" in line or "https://classroom.google.com/c/NjI4NTE1NDgxMzla/mc/MTE" in line \
                or "https://classroom.google.com/c/NjQ4MjYyNTY1ODFa/a/MTE" in line:
            line = line.strip('<')
            line = line.replace('>', '')
            line = line.rstrip()
            line = line.rstrip('.')
            links.append(line)


# Gives coordinates for mouse's location on the display whenever the mouse moves.
def location_finder():
    time.sleep(4)
    SCREENSHOT_PATH = r"C:\Users\megan\Desktop\screenshots"
    # tab_img = pg.screenshot(os.path.join(SCREENSHOT_PATH, "lname.png"), region=(490, 420, 215, 180))
    infinity = True
    while infinity:
        print(pg.position())

# Extracts the data required for auto-fill from credentials.txt into a list named data.
def get_credentials(file):
    inFile = open(file, 'r')
    global data
    data = []
    for line in inFile:
        data.append(line.rstrip())
    inFile.close()

# Finds the school attendance tab, and
# uses the Pyautogui commands to fill in the school-wide attendance.
def school_attendance():
    # Choose the tab
    try:
        # Find and click the tab
        time.sleep(4)
        perlowitz_tab = pg.locateOnScreen("C:/Users/megan/Desktop/screenshots/perlowitz.png")
        perlowitz_tab = pg.center(perlowitz_tab)
        x, y = perlowitz_tab
        x, y = perlowitz_tab
        pg.click(x, y)
        time.sleep(1)
        # Find and fill in Id
        id_field = pg.locateOnScreen("C:/Users/megan/Desktop/screenshots/id.png")
        id_field = pg.center(id_field)
        x, y = id_field
        x, y = id_field
        pg.click(x, y)
        time.sleep(1)
        pg.write(data[0])
        # Find and fill in the Name
        time.sleep(1)
        pg.scroll(-400)
        time.sleep(1)
        pg.click(540, 450)
        pg.write(data[1])
        time.sleep(1)
        pg.click(540, 640)
        pg.write(data[2])
        time.sleep(1)
        # Find and click the button
        pg.click(540, 830)
        time.sleep(1)
        # Find and click the submit button
        # submit_loc = pg.locateOnScreen("C:/Users/megan/Desktop/screenshots/submit.png")
        # submit_loc = pg.center(submit_loc)
        # x, y = submit_loc
        # x, y = submit_loc
        pg.click(540, 960)
        time.sleep(1)
    except:
        print('The perlowitz tab is not opened or not found.')

# Finds the math tab and fills in the Math attendance.
def math_attendance():
    # Choose the tab
    try:
        time.sleep(2)
        math_tab = pg.locateOnScreen("C:/Users/megan/Desktop/screenshots/math_tab.png")
        math_tab = pg.center(math_tab)
        x, y = math_tab
        pg.click(x, y)
        time.sleep(1)
        # Click on Google Form
        pg.click(477, 436)
        time.sleep(2)
        # Fill in the information
        bandChoice = (591, 732)
        pg.click(bandChoice)
        time.sleep(0.5)
        pg.scroll(-400)
        time.sleep(0.5)
        fullname_field = (585, 500)
        pg.click(fullname_field)
        time.sleep(0.5)
        pg.write(data[1] + " " + data[2])
        time.sleep(0.5)
        id_field = (585, 700)
        pg.click(id_field)
        pg.write(data[0])
        submit_button = (585, 900)
        pg.click(submit_button)
        # Go back to math tab and submit on Google Classroom
        math_tab = pg.locateOnScreen("C:/Users/megan/Desktop/screenshots/math_tab.png")
        math_tab = pg.center(math_tab)
        x, y = math_tab
        pg.click(x, y)
        time.sleep(1)
        pg.click(1400, 350)
        time.sleep(1.5)
        pg.click(1100, 640)
    except:
        print('The math tab is not opened or not found.')


# Finds the science tab and fills in the science attendance.
def science_attendance():
    # Choose the tab
    try:
        time.sleep(2)
        math_tab = pg.locateOnScreen("C:/Users/megan/Desktop/screenshots/science_tab.png")
        math_tab = pg.center(math_tab)
        x, y = math_tab
        pg.click(x, y)
        time.sleep(1)
        # Fill in the information
        choice = (1343, 310)
        pg.click(choice)
        time.sleep(1.5)
        submit = (1438, 615)
        pg.click(submit)
        pg.click(1100, 630)
    except:
        print('The science tab is not opened or not found.')

# Uses webbrowser to open a browser with a new tab for every url grabbed from gmail.
# calls the functions to do find and fill in every attendance.
def do_attendance(url_links):
    for url in url_links:
        webbrowser.open_new_tab(url)
    school_attendance()
    math_attendance()
    science_attendance()


def main():
    before = time.perf_counter()
    # All path variables
    credential_path = r'C:/Users/megan/Desktop/Courses/Python_Automation/MyFiles/Non-Cource-Related_Practice/Attendance_Automation/credentials.txt'
    textPath = r'C:/Users/megan/Desktop/Courses/Python_Automation/MyFiles/Non-Cource-Related_Practice/Attendance_Automation/attendance_messages.txt'
    # Server-required info
    EMAIL = 'nfarukhzoda6058@ermurrowhs.org'
    PASSWORD = '242306058'
    SERVER = 'imap.gmail.com'
    # Method-required variables
    today = date.today().strftime('%Y, %m, %d')
    url_links = []
    # Methods:
    get_credentials(credential_path)
    find_attendance_messages(SERVER, EMAIL, PASSWORD)
    get_urls(textPath, url_links)
    do_attendance(url_links)
    # location_finder()
    # Time analyzer
    after = time.perf_counter()
    print(f'Finished in {round(after - before, 2)}')


if __name__ == '__main__':
    main()
import email
import imaplib
import os
import psutil
import pyautogui
import signal
import subprocess
import time
from email.header import decode_header

from selenium import webdriver
from selenium.webdriver.common.by import By


def del_file(path_file):
    file = path_file
    if os.path.exists(file):
        os.remove(file)
    return


def wait_file(path_file):
    file = path_file
    i = None
    count = 500
    while i is None:
        count -= 1
        time.sleep(0.5)
        if os.path.exists(file):
            break
        else:
            if i is not None:
                return i
            else:
                continue


def proc_woking(proc_name):
    for proc in psutil.process_iter():
        if proc.name() == proc_name:
            print(proc_name)
            return proc_name


def wait_image(img):  # Ожидаем появления картинки на экране
    i = None
    count = 500
    while i is None:
        count -= 1
        i = pyautogui.locateOnScreen(img, confidence=0.9)
        time.sleep(0.5)
        if count == 0:
            break
        else:
            if i is not None:
                return i
            else:
                continue


def process(): # От Кости для завершения процесса
    try:
        pid = None
        for proc in psutil.process_iter():
            if 'planoplan.exe' in proc.name():
                os.kill(int(proc.pid), signal.SIGILL)
    except Exception as ex:
        print("Error Encountered while running script", ex)


def download_file(proc_name):
    subprocess.call(["taskkill", "/f", "/im", 'planoplan.exe'])
    del_file("C:/Users/piati/Downloads/PlanoplanEditorSetup.exe")
    chrome_Options = webdriver.ChromeOptions()
    prefs = {'safebrowsing.enabled': 'false'}
    chrome_Options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=chrome_Options)
    browser.get('https://planoplan.com/ru/', )
    browser.maximize_window()
    button = browser.find_element(By.XPATH, '//*[@id="__next"]/header/div/div/div/nav/div[1]/a')
    button.click()
    download_button = browser.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/a')
    download_button.click()
    wait_file("C:/Users/piati/Downloads/PlanoplanEditorSetup.exe")
    os.startfile("C:/Users/piati/Downloads/PlanoplanEditorSetup.exe", 'runas')
    time.sleep(5)
    browser.quit()
    for proc in psutil.process_iter():
        if proc.name() == proc_name:
            print(proc_name)
            return proc_name
    subprocess.call(["taskkill", "/f", "/im", 'planoplan.exe'])


def download_mac(file_name):
    del_file("C:/Users/piati/Downloads/PlanoplanEditorSetup.pkg")
    chrome_Options = webdriver.ChromeOptions()
    prefs = {'safebrowsing.enabled': 'false'}
    chrome_Options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=chrome_Options)
    browser.get('https://planoplan.com/ru/', )
    browser.maximize_window()
    button = browser.find_element(By.XPATH, '//*[@id="__next"]/header/div/div/div/nav/div[1]/a')
    button.click()
    download_button = browser.find_element(By.XPATH, '//*[@id="__next"]/main/div/section[1]/div/a')
    download_button.click()
    wait_file("C:/Users/piati/Downloads/PlanoplanEditorSetup.pkg")
    time.sleep(2)
    browser.quit()
    if os.path.exists("C:/Users/piati/Downloads/PlanoplanEditorSetup.pkg"):
        return file_name


def registration():
    subprocess.call(["taskkill", "/f", "/im", 'planoplan.exe'])
    pyautogui.PAUSE = 1.5
    del_file("C:/Users/piati/AppData/Local/Temp/Planoplan/PlanoplanEditor/prefs.dat")
    os.startfile("C:/Users/piati/AppData/Local/Planoplan/Planoplan Editor/planoplan.exe")
    wait_image('Picture/vvedite_vash_email.jpg')
    pyautogui.click(pyautogui.locateOnScreen('Picture/vvedite_vash_email.jpg', confidence=0.8))
    pyautogui.write('test_arhist@mail.ru', interval=0.2)
    pyautogui.click(pyautogui.locateOnScreen('Picture/pridumaite_vash_parol.jpg', confidence=0.8))
    pyautogui.write("!qazxsw23edc", interval=0.2)
    pyautogui.click(pyautogui.locateOnScreen('Picture/zaregistrirovasia.jpg', confidence=0.8))
    time.sleep(10)
    subprocess.call(["taskkill", "/f", "/im", 'planoplan.exe'])
    os.startfile("C:/Users/piati/AppData/Local/Planoplan/Planoplan Editor/planoplan.exe")
    wait_image('Picture/propustit_shag.jpg')
    pyautogui.click(pyautogui.locateOnScreen('Picture/propustit_shag.jpg', confidence=0.8))
    time.sleep(10)
    if pyautogui.locateOnScreen('Picture/nachat_s_nulia.jpg', confidence=0.8):
        return "trial"


def registration_google():
    subprocess.call(["taskkill", "/f", "/im", 'planoplan.exe'])
    pyautogui.PAUSE = 1.5
    del_file("C:/Users/piati/AppData/Local/Temp/Planoplan/PlanoplanEditor/prefs.dat")
    os.startfile("C:/Users/piati/AppData/Local/Planoplan/Planoplan Editor/planoplan.exe")
    wait_image("Picture/google.jpg")
    pyautogui.click(pyautogui.locateOnScreen('Picture/google.jpg', confidence=0.8))
    wait_image("Picture/opros_01.jpg")
    pyautogui.click(pyautogui.locateOnScreen('Picture/drugoe.jpg', confidence=0.8))
    pyautogui.click(pyautogui.locateOnScreen('Picture/vvedite_vash_variant.jpg', confidence=0.8))
    pyautogui.write('test', interval=0.2)
    pyautogui.click(pyautogui.locateOnScreen('Picture/progolgit.jpg', confidence=0.8))
    pyautogui.click(pyautogui.locateOnScreen('Picture/drugoe.jpg', confidence=0.8))
    pyautogui.click(pyautogui.locateOnScreen('Picture/vvedite_vash_variant.jpg', confidence=0.8))
    pyautogui.write('test', interval=0.2)
    pyautogui.click(pyautogui.locateOnScreen('Picture/progolgit.jpg', confidence=0.8))
    wait_image('Picture/obuchenie.jpg')
    if pyautogui.locateOnScreen('Picture/obuchenie.jpg', confidence=0.8):
        return "obuchenie"
    subprocess.call(["taskkill", "/f", "/im", 'planoplan.exe'])


def registration_vk():
    subprocess.call(["taskkill", "/f", "/im", 'planoplan.exe'])
    pyautogui.PAUSE = 1.5
    del_file("C:/Users/piati/AppData/Local/Temp/Planoplan/PlanoplanEditor/prefs.dat")
    os.startfile("C:/Users/piati/AppData/Local/Planoplan/Planoplan Editor/planoplan.exe")
    wait_image("Picture/vk.jpg")
    pyautogui.click(pyautogui.locateOnScreen('Picture/vk.jpg', confidence=0.8))
    wait_image("Picture/opros_01.jpg")
    pyautogui.click(pyautogui.locateOnScreen('Picture/drugoe.jpg', confidence=0.8))
    pyautogui.click(pyautogui.locateOnScreen('Picture/vvedite_vash_variant.jpg', confidence=0.8))
    pyautogui.write('test', interval=0.2)
    pyautogui.click(pyautogui.locateOnScreen('Picture/progolgit.jpg', confidence=0.8))
    pyautogui.click(pyautogui.locateOnScreen('Picture/drugoe.jpg', confidence=0.8))
    pyautogui.click(pyautogui.locateOnScreen('Picture/vvedite_vash_variant.jpg', confidence=0.8))
    pyautogui.write('test', interval=0.2)
    pyautogui.click(pyautogui.locateOnScreen('Picture/progolgit.jpg', confidence=0.8))
    wait_image('Picture/obuchenie.jpg')
    if pyautogui.locateOnScreen('Picture/obuchenie.jpg', confidence=0.8):
        return "obuchenie"
    subprocess.call(["taskkill", "/f", "/im", 'planoplan.exe'])


def del_email():  # Удаляем все письма из папки входящие
    mail_pass = "HgXsaJaErmJiGV2VtB1Z"
    username = "test_arhist@mail.ru"
    imap_server = "imap.mail.ru"
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, mail_pass)
    imap.select("inbox")
    typ, data = imap.search(None, 'ALL')
    for num in data[0].split():
        imap.store(num, '+FLAGS', '\\Deleted')
    imap.expunge()


def kod_podtverjdenia():  # Проверяем приходит ли на почту письмо в заголовке которого есть фраза "Ваш код:"
    mail_pass = "HgXsaJaErmJiGV2VtB1Z"
    username = "test_arhist@mail.ru"
    imap_server = "imap.mail.ru"
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, mail_pass)
    imap.select("INBOX")
    result, data = imap.search(None, "ALL")
    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]
    res, msg = imap.fetch(latest_email_id, '(RFC822)')
    msg = email.message_from_bytes(msg[0][1])
    subject_letter = decode_header(msg["Subject"])[0][0].decode()
    print(subject_letter)
    if subject_letter.find("Ваш код:") == 1:
        return "Letter inbox"


def new_project(): # Новый проект
    subprocess.call(["taskkill", "/f", "/im", 'planoplan.exe'])
    pyautogui.PAUSE = 1.5
    del_file("C:/Users/piati/AppData/Local/Temp/Planoplan/PlanoplanEditor/prefs.dat")
    os.startfile("C:/Users/piati/AppData/Local/Planoplan/Planoplan Editor/planoplan.exe")
    wait_image('Picture/vhod.jpg')
    pyautogui.click(pyautogui.locateOnScreen('Picture/vhod.jpg', confidence=0.9))
    pyautogui.click(pyautogui.locateOnScreen('Picture/vvedite_vash_email.jpg', confidence=0.9))
    pyautogui.write('test_arhist@mail.ru', interval=0.2)
    pyautogui.click(pyautogui.locateOnScreen('Picture/vvedite_vash_parol.jpg', confidence=0.9))
    pyautogui.write('123456', interval=0.2)
    pyautogui.click(pyautogui.locateOnScreen('Picture/voiti.jpg', confidence=0.9))
    wait_image('Picture/dobavit_proekt.jpg')
    pyautogui.click(pyautogui.locateOnScreen('Picture/dobavit_proekt.jpg', confidence=0.9))
    wait_image('Picture/nachat_s_nulia.jpg')
    pyautogui.click(pyautogui.locateOnScreen('Picture/nachat_s_nulia.jpg', confidence=0.9))


def wall_construction_by_edge(): # Построение комнаты методом по краю
    new_project()
    pyautogui.PAUSE = 1.5
    if pyautogui.locateOnScreen('Picture/metod_postroenia.jpg', confidence=0.8):
        pass
    else:
        pyautogui.click(500, 500)
        pyautogui.press('3')
    pyautogui.click(400, 300)
    pyautogui.click(1500, 300)
    pyautogui.click(1500, 800)
    pyautogui.click(400, 800)
    pyautogui.click(400, 300)
    if pyautogui.locateOnScreen('Picture/nastroiki_komnati.jpg', confidence=0.8):
        a = "good"
    pyautogui.click(button='right')
    return a


def wall_construction_by_center():  # Построение комнаты методом по центру
    pyautogui.PAUSE = 1.5
    pyautogui.click(x=300, y=200, clicks=2, interval=1)
    pyautogui.dragTo(1600, 900, 2)
    pyautogui.press('Delete')
    if pyautogui.locateOnScreen('Picture/metod_postroenia_01.jpg', confidence=0.8):
        pyautogui.click(pyautogui.locateOnScreen('Picture/metod_postroenia_01.jpg', confidence=0.9))
        pyautogui.moveRel(0, 50, 1)
        pyautogui.click()
    else:
        pyautogui.click(500, 500)
        pyautogui.press('2')
    pyautogui.click(400, 300)
    pyautogui.click(1500, 300)
    pyautogui.click(1500, 800)
    pyautogui.click(400, 800)
    pyautogui.click(400, 300)
    if pyautogui.locateOnScreen('Picture/nastroiki_komnati.jpg', confidence=0.8):
        a = "good"
    pyautogui.click(button='right')
    return a


def wall_construction_by_room():  # Построение комнаты методом комнатой
    pyautogui.PAUSE = 1.5
    pyautogui.click(x=300, y=200, clicks=2, interval=1)
    pyautogui.dragTo(1600, 900, 2)
    pyautogui.press('Delete')
    if pyautogui.locateOnScreen('Picture/postroenie_po_centru.jpg', confidence=0.8):
        pyautogui.click(pyautogui.locateOnScreen('Picture/postroenie_po_centru.jpg', confidence=0.9))
        pyautogui.moveRel(0, 100, 2)
        pyautogui.click()
    else:
        pyautogui.click(500, 500)
        pyautogui.press('4')
    pyautogui.click(400, 300)
    pyautogui.click(1500, 800)
    if pyautogui.locateOnScreen('Picture/nastroiki_komnati.jpg', confidence=0.8):
        a = "good"
    pyautogui.click(button='right')
    return a


def wall_construction_drywall():  # Построение фальш стены
    pyautogui.PAUSE = 1.5
    pyautogui.click(x=300, y=200, clicks=2, interval=1)
    pyautogui.dragTo(1600, 900, 2)
    pyautogui.press('Delete')
    if pyautogui.locateOnScreen('Picture/postroenie_komnatoi.jpg', confidence=0.8):
        pyautogui.click(pyautogui.locateOnScreen('Picture/postroenie_komnatoi.jpg', confidence=0.9))
        pyautogui.moveRel(0, 150, 2)
        pyautogui.click()
    else:
        pyautogui.click(500, 500)
        pyautogui.press('4')
    pyautogui.click(500, 500)
    pyautogui.click(1500, 500)
    pyautogui.moveRel(-50, 0, 1)
    pyautogui.click()
    if pyautogui.locateOnScreen('Picture/Nastroiki_falsh_steni.jpg', confidence=0.8):
        a = "good"
    pyautogui.click(button='right')
    return a



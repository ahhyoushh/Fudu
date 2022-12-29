import schedule
import time
import back.xp

def frequency_remover():
    back.xp.remove_xp(150)
    print("Bro get consistent!")

schedule.every().day.at("23:59").do(frequency_remover)
def frequency():
    while True:
        schedule.run_pending()
        time.sleep(1)

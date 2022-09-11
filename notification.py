import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="hey you have to feed your pet",
            message="someone important to you is waiting for you for his meal",
            app_icon="C:\\Users\\meghn\\OneDrive\\Documents\\python project\\icon.ico.ico",
            timeout=1
        )
        time.sleep(3600*5)
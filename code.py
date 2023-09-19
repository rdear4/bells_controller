import io
import json
import wifi
# import adafruit_requests
import adafruit_logging as logging
import time
import microcontroller
import sys

import myserver


logger = logging.getLogger('dev')

logger.setLevel(logging.DEBUG)

CONFIG_DATA = None
PIN_CONFIG = None



logger.info("STARTUP...")
time.sleep(2)

def loadFile(filename):
    logger.info(f'Loading file: {filename}...')
    try:
        fileData = io.open(filename, mode="r")
        logger.info(f'File Loaded: {filename}' )
        return json.load(fileData)

    except:
        raise Exception(f'There was an error loading file: {filename}')

def startAP():

    try:
        logger.info("Starting AP...")

        logger.info(wifi.radio.ap_active)

        if (wifi.radio.ap_active):
            return
        # wifi.radio.enabled = False
        # logger.info("Stopping Station")
        # wifi.radio.stop_station()
        
        # time.sleep(2)
        # logger.info("Starting station")
        wifi.radio.enabled = True
        # wifi.radio.stop_ap()
        # wifi.radio.start_station()
        # logger.info(wifi.radio.ap_active)
        
        # wifi.radio.enabled = True
        # logger.info("Starting AP...")
        
        # time.sleep(2)
        wifi.radio.start_ap(CONFIG_DATA["AP_SSID"], CONFIG_DATA["AP_PASSWORD"])

        

    except Exception as e:
        logger.error(f'Error setting up access point - {e}')
        logger.error("Restarting...")
        time.sleep(5)
        microcontroller.reset()
        


if __name__ == '__main__':
    
    try:
    #Load the config files
        #Load the basic config
        CONFIG_DATA = loadFile("config.json")

        print(CONFIG_DATA)
        #Load the pin mapping config
        PIN_CONFIG = loadFile("pin_config.json")
        logger.info(PIN_CONFIG)

        #Load the song files

        #Start WiFi
        startAP()

        #Start the webserver
        myserver.setLogger(logger)
        myserver.startWebServer()


        #Listen for requests
        while True:
            try:
                myserver.webServer.poll()
                pass
            except KeyboardInterrupt:
                logger.info("Keyboard interupt")
                sys.exit(0)
            except Exception as e:
                
                logger.info(e)
                
                pass


    except Exception as error:
        logger.error(error)
import sys
import time
import helium
import getpass
sleep=0.5

from selenium.webdriver import FirefoxOptions

options = FirefoxOptions()
options.set_preference("browser.download.useDownloadDir", True)
options.set_preference("browser.download.folderList", 2)
#options.set_preference("browser.download.dir", "path/to/download/directory")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")  # specify content-type
start_firefox("connpass.com/login", options=options)

#browser=helium.start_chrome('https://scholar.google.com/citations?hl=es&login',headless=True)
browser=helium.start_firefox('https://scholar.google.com/citations?hl=es&login',headless=True)

email=input('email')
password=input('password')
helium.write(email,into='Correo electrónico o teléfono')

time.sleep(sleep)
helium.click(helium.Button('Siguiente'))

time.sleep(sleep)
helium.write(password,into='Introduce tu contraseña')

time.sleep(sleep)
helium.click(helium.Button('Siguiente'))

#Select articles
time.sleep(5)
browser.find_element_by_id('gsc_x_all').click()

time.sleep(sleep)
helium.click('EXPORTAR')

time.sleep(sleep)
helium.click('CSV')

time.sleep(sleep)
helium.click('Exportar todos mis artículos')

time.sleep(sleep)
#Button EXPORTAR
browser.find_element_by_id('gsc_md_exa_export').click()

input('Close')
browser.close()

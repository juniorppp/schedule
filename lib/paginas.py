
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import json,time

class Paginas:
    def __init__(self,dados):
        self.login = False
        self.path_download = '/files/'+dados.get('cpf')
        self.ex = dados.get("extracted")
        self.dados = dados

        if dados.get('cpf') != "000.000.000-00":
            opt = webdriver.ChromeOptions()

            settings = {
                        "recentDestinations": [{
                            "id": "Save as PDF",
                            "origin": "local",
                            "account": "",
                        }],
                        "selectedDestinationId": "Save as PDF",
                        "version": 2
                        }

            opt.add_argument("--window-size=2560,1440")
            opt.add_argument("start-maximized")
            opt.add_argument('--kiosk-printing')

            opt.add_experimental_option( "prefs", {
                                                    'printing.print_preview_sticky_settings.appState': json.dumps(settings),
                                                    'savefile.default_directory': f'{self.path_download}',
                                                    'profile.default_content_settings.popups': 0,
                                                    'download.prompt_for_download' : False,
                                                    'download.default_directory': f'{self.path_download}',
                                                    'profile.default_content_setting_values.automatic_downloads':1
                                                })

            self.driver = webdriver.Chrome('/opt/drivers/chromedriver' , options=opt)
            print("\033[32m"+"Pronto!, Chrome já esta inicializado."+"\033[0;0m")
        else:
            print("Não consigo criar a pasta.")

    def _sites(self,site):
        try:
            self.driver.get(site)
            time.sleep(10)
            self.driver.execute_script('window.print();')
        except:
            print("\033[31m"+"Erro."+"\033[0;0m")    

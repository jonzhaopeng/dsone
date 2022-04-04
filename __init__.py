__version__ = '0.1.0'

import os
import poetry.get_poetry as poe
if "Poetry" in os.popen("poetry --version").read():
    os.system("poetry --version")
else:
# y 参数表示同意修改环境变量等设定,不需要手工确认   
    installer = poe.Installer(accept_all=True)
    if installer.run() == 0:
        os.system("source $HOME/.poetry/env")
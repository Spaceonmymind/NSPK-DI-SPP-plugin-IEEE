from selenium import webdriver

from logging import config
config.fileConfig('dev.logger.conf')
from IEEE import IEEE

driver = webdriver.Chrome()

parser = IEEE(driver)
docs = parser.content()


print(*docs, sep='\n\r\n')
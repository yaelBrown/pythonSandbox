# https://pypi.org/project/colorama/
from colorama import init

init()

from colorama import Fore

print(Fore.GREEN + "This text is green")
print(Fore.RED + "This text is red")

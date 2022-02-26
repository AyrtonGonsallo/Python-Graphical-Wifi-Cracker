from itertools import cycle
from time import sleep
import subprocess
import os

colors = iter(cycle(['blue', 'red']))
loading_chars = iter(cycle('/-\|'))
os.system('cls')


def getData():
    res = ""
    res += '{:<30}|  Mots de passe\n'.format('Reseaux')
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('windows-1252').splitlines()

    profiles = [i.split(':', 1)[1][1:] for i in output if 'Profil Tous les utilisateurs' in i]

    for profile in profiles:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', profile, 'key=clear']).decode(
            'windows-1252').splitlines()
        color = next(colors)
        try:
            password = [b.split(':', 1)[1][1:] for b in result if 'Contenu de la cl' in b][0]
            res += f'{profile:<30}|  {password}\n'
        except:
            res += f'{profile:<30}|  <No password>\n'
        finally:
            sleep(.1)

    sleep(1)
    return res


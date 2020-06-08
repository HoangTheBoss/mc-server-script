import pathlib
import platform
from shutil import copyfile

import psutil
import speedtest

from hurry.filesize import size


# network speedtest
def net_speed():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download(threads=8)
    s.upload(threads=8)
    results_dict = s.results.dict()
    return round((min(results_dict["download"], results_dict["upload"])) / 1048576)


# calculations
def calc_players(net, ram):
    if ram.endswith("G"):
        ram_int = int(ram[:-1]) * 1024
    else:
        ram_int = int(ram[:-1])
    net_players = int(net) / 0.33
    ram_players = (ram_int * 0.75) / 64
    max_player = round(min(ram_players, net_players))
    return str(max_player)


# check OS and memory
def system_check():
    return platform.system(), size(psutil.virtual_memory().available)


# create the start.bat script
def generate_script(os, inputmem, lithium):
    if not lithium:
        generated_script = "java -Xms" + inputmem + " -Xmx" + inputmem + " -jar server.jar"
    elif lithium:
        generated_script = "java -Xms" + inputmem + " -Xmx" + inputmem + " -jar fabric-server-launch.jar"
    if os == "Windows":
        open("server/start.bat", 'w+').write(generated_script)
        print("File chay server/Server starting script: ", pathlib.Path('server/start.bat').absolute())
    elif os == "Linux":
        open("server/start.sh", 'w+').writelines(["#!/bin/sh", generated_script])
        print("File chay server/Server starting script: ", pathlib.Path('server/start.sh').absolute())
    elif os == "MacOS":
        open("server/start.sh", 'w+').writelines(["#!/bin/sh", generated_script])
        print("File chay server/Server starting script: ", pathlib.Path('server/start.sh').absolute())
    return generated_script


# create eula file and set EULA to TRUE
def eula_true():
    pathlib.Path("server").mkdir(parents=True, exist_ok=True)
    open("server/eula.txt", 'w+').write("eula=true")


# create properties file and set values
def set_properties(server_name, max_player):
    copyfile("./templates/server.properties.templates", "./server/server.properties")
    with open("server/server.properties", "r", encoding="utf8") as file:
        fileout = file.read().replace("max-players=20", ("max-players=" + max_player))
        fileout = file.read().replace("motd=WeeLux", ("motd=" + server_name))
    with open("server/server.properties", "w", encoding="utf8") as file:
        file.write(fileout)

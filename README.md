## Minecraft JE Server creation script
> Script tạo server Minecraft Java

[![Build Status](https://travis-ci.com/HoangTheBoss/mc-server-script.svg?branch=master)](https://travis-ci.com/HoangTheBoss/mc-server-script)

Minecraft Server [setup](https://minecraft.gamepedia.com/Tutorials/Setting_up_a_server) script for Windows, MacOSX, Ubuntu, Debian, CentOS, Fedora... (Not Solaris at the moment), using Python and some dependencies.

![screenshot-1](demos/screenshot-1.png "Screenshot 1")

### Installation and using
Download the latest `.zip` file at [Releases](https://github.com/hoangtheboss/mc-server-script/releases)

For __Windows 10__ you can run `windows-easy.bat` to download Python (embedded version/if not installed), install dependencies and execute the script.

Alternatively you can use the command line:

```
git clone https://github.com/HoangTheBoss/mc-server-script.git
(cd into the repo)
pip -r requirements.txt
python makeserver.py
```
### Dependencies
Better check [requirements.txt](https://github.com/HoangTheBoss/mc-server-script/blob/master/requirements.txt) for more updated contents
```
hurry.filesize == 0.9
psutil == 5.7.0
requests == 2.23.0
text_editor == 1.0.5
speedtest_cli == 2.1.2
pySmartDL == 1.3.3
```

### Contribute
Do what you can to help the project. Issues and pull requests are welcome.

### I want to run my own MC server but don't have a dedicated machine for that
You can host your server at [Apex Hosting](https://billing.apexminecrafthosting.com/aff.php?aff=2786) for cheap!



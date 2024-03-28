<p align="center">
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-_red.svg"></a>
<a href="https://twitter.com/DanialHalo"><img src="https://img.shields.io/twitter/follow/dan1337.svg?logo=twitter"></a>
<a href="https://www.linkedin.com/in/dan1337/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=whit"></a>
</p>

# MassDetect
**MassDetect** is a tool that quickly detects HTTP web server ports using Masscan for speed and can also speed up the service &amp; version scans, perfect for bug bounty hunters and pentesters.

![alt text](https://github.com/danialhalo/MassDetect/blob/main/Screenshot.png?raw=true)

## Installation
```
git clone https://github.com/danialhalo/MassDetect.git
cd MassDetect
chmod +x massdetect.py
```
**Nmap, masscan and httpx are required**

# Usage

This will display help for the tool. Here are all the options it supports.
```
kali:/Massdetect$ sudo python3 massdetect.py -h



                         ███▄ ▄███▓ ▄▄▄        ██████   ██████ ▓█████▄ ▓█████▄▄▄█████▓▓█████  ▄████▄  ▄▄▄█████▓
                        ▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▒██▀ ██▌▓█   ▀▓  ██▒ ▓▒▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒
                        ▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ░██   █▌▒███  ▒ ▓██░ ▒░▒███   ▒▓█    ▄ ▒ ▓██░ ▒░
                        ▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░▓█▄   ▌▒▓█  ▄░ ▓██▓ ░ ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░
                        ▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒▒██████▒▒░▒████▓ ░▒████▒ ▒██▒ ░ ░▒████▒▒ ▓███▀ ░  ▒██▒ ░
                        ░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░ ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░░   ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░
                        ░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░ ░ ▒  ▒  ░ ░  ░   ░     ░ ░  ░  ░  ▒       ░
                        ░      ░     ░   ▒   ░  ░  ░  ░  ░  ░   ░ ░  ░    ░    ░         ░   ░          ░
                               ░         ░  ░      ░        ░     ░       ░  ░           ░  ░░ ░
                                                                ░                            ░

                                                       -:  Muhammad Danial  :-

usage: massdetect.py [-h] [--target TARGET] [-f TARGET_FILE] [--top-ports TOP_PORTS] [-p PORTS] [--web-ports] [--rate RATE] [--nmap] [-T T] [-o OUTPUT]

Run masscan with different port options

options:
  -h, --help            show this help message and exit
  --target TARGET, -t TARGET
                        Target IP or IP range (e.g., 10.1.1.1/24)
  -f TARGET_FILE, --target-file TARGET_FILE
                        File containing target IPs
  --top-ports TOP_PORTS
                        Top ports to scan (e.g., --top-ports 100)
  -p PORTS, --ports PORTS
                        Specific port or ports separated by comma (e.g., 80,443)
  --web-ports           Scan top web ports list by Seclist
  --rate RATE           Masscan Rate default is 100000
  --nmap                Run nmap for service and version detection
  -T T                  nmap speed Default is -T4
  -o OUTPUT, --output OUTPUT
                        Output file for storing the scan results
```

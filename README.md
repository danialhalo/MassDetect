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

# Running MassDetect
### Single IP Scan
The IP or single subnet can be provided with `-t flag` for single site scan
```
sudo python3 massdetect.py -t 192.0.0.1
```

### File Input
The `-f flag` allows MassDetect to read a file containing multiple IPs or subnets for simultaneous scanning.
```
sudo python3 massdetect.py -f ips.txt
```

### File Output
For the output file `-o flag` can be used for defining the output file name otherwise output will automatically saved into the file name **scan_results.txt**.
```
sudo python3 massdetect.py -f ips.txt -o result.txt
```

### Specifing Ports
For specifing single port or a list of ports `-p` can be used.
```
sudo python3 massdetect.py -f ips.txt -p 80,22
```
Similarly `--top-ports` flag can be used for scanning top ports.
```
sudo python3 massdetect.py -f ips.txt --top-ports 100
```
For scanning list of common web server ports used `--web-ports` flag.
```
sudo python3 massdetect.py -f ips.txt --web-ports 100
```

### Service and Version Detection
For running nmap on open ports detected by masscan `--nmap` flag should be used 
```
sudo python3 massdetect.py -f ips.txt -p 80 --nmap
```
### Speed scan
Masscan speed can be adjust by using the `--rate` flag default is set to 100000 
```
sudo python3 massdetect.py -f ips.txt -p 80 --nmap --rate 20000
```
Similarly for nmap `-T1, T2, T3, T4 and T5` flags can be used. Default is set to -T4
```
sudo python3 massdetect.py -f ips.txt -p 80 --nmap --rate 20000 -T5
```


# Contributing
Contributions to MassDetect are always welcome. Whether it's feature enhancements, bug fixes, or documentation improvements, every bit of help is appreciated.


# License
`MassDetect` is distributed under [MIT License](https://github.com/danialhalo/SqliSniper/blob/main/LICENSE)

---

<div align="center">

`MassDetect` is made in <img src="https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png" alt="python" height="20px" width="20px"> with lots of 💙 by [@Muhammad Danial](https://twitter.com/DanialHalo).

</div>

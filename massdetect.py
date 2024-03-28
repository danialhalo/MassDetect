import subprocess
import argparse
import time
import sys
import re
import os

massout = ' -oL masscan.hxi'
def run_masscan(target, ports, rate):
    command = ['masscan'] + target.split() + ports.split() + rate.split() + massout.split()
    proc = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    cursor_chars = '|/-\\'
    cursor_index = 0

    while proc.poll() is None:
        sys.stdout.write('\r[*] Running masscan... ' + cursor_chars[cursor_index])
        sys.stdout.flush()
        cursor_index = (cursor_index + 1) % len(cursor_chars)
        time.sleep(0.1)

    sys.stdout.write('\r                                      \n')
    sys.stdout.flush()

def parse_masscan_output():
    ip_ports = {}
    with open('masscan.hxi', 'r') as file:
        for line in file:
            match = re.match(r'open tcp (\d+) (\d+\.\d+\.\d+\.\d+) (\d+)', line)
            if match:
                port = int(match.group(1))
                ip = match.group(2)
                if ip in ip_ports:
                    ip_ports[ip].append(port)
                else:
                    ip_ports[ip] = [port]
    os.remove('masscan.hxi')
    return ip_ports


def httpx(ip,ports_str):
    httpx_command = f'echo {ip} | httpx -p {ports_str} -silent -sc -cl -o out.httpx'
    print('\n[*] Running httpx\n')
    subprocess.run(httpx_command, shell=True)



def nmap(ip,ports_str,T):
    os.system('touch haalim.nmap; rm *.nmap')
    out_f = ip.replace(".","_")+".nmap"
    nmap_command = f'nmap {ip} -p {ports_str} -sC -sV -oN {out_f} '+T
    process = subprocess.Popen(nmap_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in process.stdout:
        line = line.strip()
        if not any(phrase in line for phrase in ["Host is up", "Starting Nmap", "Service detection", "Nmap done:", "unrecognized despite returning data", "========NEXT", "SF:","SF-"]):
            print(line)

def main():


    banner = """\033[32m\n\n
\t\t\t ███▄ ▄███▓ ▄▄▄        ██████   ██████ ▓█████▄ ▓█████▄▄▄█████▓▓█████  ▄████▄  ▄▄▄█████▓
\t\t\t▓██▒▀█▀ ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▒██▀ ██▌▓█   ▀▓  ██▒ ▓▒▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒
\t\t\t▓██    ▓██░▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ░██   █▌▒███  ▒ ▓██░ ▒░▒███   ▒▓█    ▄ ▒ ▓██░ ▒░
\t\t\t▒██    ▒██ ░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░▓█▄   ▌▒▓█  ▄░ ▓██▓ ░ ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░
\t\t\t▒██▒   ░██▒ ▓█   ▓██▒▒██████▒▒▒██████▒▒░▒████▓ ░▒████▒ ▒██▒ ░ ░▒████▒▒ ▓███▀ ░  ▒██▒ ░
\t\t\t░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░ ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░░   ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░
\t\t\t░  ░      ░  ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░ ░ ▒  ▒  ░ ░  ░   ░     ░ ░  ░  ░  ▒       ░
\t\t\t░      ░     ░   ▒   ░  ░  ░  ░  ░  ░   ░ ░  ░    ░    ░         ░   ░          ░
\t\t\t       ░         ░  ░      ░        ░     ░       ░  ░           ░  ░░ ░
\t\t\t                                        ░                            ░
\033[0m
\t\t\t\t                       \033[96m-:  Muhammad Danial  :- \033[0m
"""

    print(banner)

    if os.geteuid() != 0:
        print("[!] This script requires root privileges. Please run it using sudo.")
        sys.exit(1)

    if os.path.exists('masscan.hxi'):
        os.remove('masscan.hxi')


    parser = argparse.ArgumentParser(description='Run masscan with different port options')
    parser.add_argument('--target','-t', help='Target IP or IP range (e.g., 10.1.1.1/24)')
    parser.add_argument('-f', '--target-file', help='File containing target IPs')
    parser.add_argument('--top-ports', type=int, help='Top ports to scan (e.g., --top-ports 100)')
    parser.add_argument('-p', '--ports', help='Specific port or ports separated by comma (e.g., 80,443)')
    parser.add_argument('--web-ports', action='store_true', help='Scan top web ports list by Seclist')
    parser.add_argument('--rate', type=int, help='Masscan Rate default is 100000')
    parser.add_argument('--nmap', action='store_true', help='Run nmap for service and version detection')
    parser.add_argument('-T', type=int, help='nmap speed Default is -T4')
    parser.add_argument('-o', '--output', help='Output file for storing the scan results')

    args = parser.parse_args()

    if args.web_ports:
        ports = '-p 66,80,81,443,445,457,1080,1100,1241,1352,1433,1434,1521,1944,2301,3000,3128,3306,4000,4001,4002,4100,5000,5432,5800,5801,5802,6346,6347,7001,7002,8000,8080,8443,8888,30821'
    elif args.ports:
        ports = '-p ' + args.ports
    elif args.top_ports:
        ports = f'--top-ports {args.top_ports}'
    else:
        ports = '-p 0-65535'

    if args.rate:
        rate = f'--rate  {args.rate}'
    else:
        rate = '--rate 100000'


    if args.T:
        T = f'-T{args.T}'
    else:
        T = '-T4'


    if args.target_file or args.target:
        pass
    else:
        print("Please provide either a target IP  or a target file")
        sys.exit(1)


    if args.output:
        ofile = args.output
    else:
        ofile = 'scan_results.txt'


    if os.path.exists(ofile):
        print(f"Previous scan file '{ofile}' exists. It will be overwritten.")
        response = input("Do you want to continue? (y/n): ").lower()
        if response in ['N', 'n', 'No']:
            print("[-] Operation aborted.")
            sys.exit(1)

    if args.target_file:
        target = f'-iL {args.target_file}'
        run_masscan(target, ports, rate)
    else:
        run_masscan(args.target, ports, rate)


    ip_ports = parse_masscan_output()
    for ip, ports in ip_ports.items():
        ports_str = ','.join(str(port) for port in ports)

        print(f"\n[+] Discovered Open Ports for {ip}  are {ports_str}")

        httpx(ip,ports_str)

        if args.nmap:
            print('\n[*] Running nmap for service and version detection\n')
            nmap(ip,ports_str,T)


    if args.output:
        cmd = f'touch hxi.nmap hxi.httpx {args.output};rm {args.output};echo "-----httpx_output-----" >> {args.output}; cat *.httpx >> {args.output}; echo "\n\n-----nmap_scan-----\n" >> {args.output}; cat *.nmap >> {args.output}; rm *.nmap *.httpx'
        os.system(cmd)
        print(f"[+] Scan results are saved in {args.output} file")
    else:
        cmd = f'touch hxi.nmap hxi.httpx scan_results.txt;rm scan_results.txt; echo "----- httpx output -----\n" >> scan_results.txt; cat *.httpx >> scan_results.txt; echo "\n\n-----nmap scan-----\n" >> scan_results.txt; cat *.nmap >> scan_results.txt; rm *.nmap *.httpx'
        os.system(cmd)
        print(f"[+] Scan results are saved in scan_results.txt file")


if __name__ == '__main__':
    main()

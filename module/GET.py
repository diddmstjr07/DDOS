from scapy.all import IP, TCP, sr1, ICMP, send, sniff, Raw, ARP, UDP
import subprocess
import os

if os.getuid() != 0:
    print("\033[1m\033[31m" + "[ERROR 404]" + "\033[0m", "Please start Program as Root (sudo)")
    os._exit(0)

completed_process = subprocess.run(["curl", "-s", "ifconfig.me"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
outer_ip = completed_process.stdout.decode('utf-8').strip()

def GET(SRC, DST, SRC_PORT, DST_PORT):
    mes = Raw(str(outer_ip))
    ip = IP(src=SRC, dst=DST)
    tcp = UDP(dport=DST_PORT, sport=SRC_PORT)
    packet = ip/tcp/mes
    response = sr1(packet)
    MES = response[Raw].load.decode()
    print(MES)
    
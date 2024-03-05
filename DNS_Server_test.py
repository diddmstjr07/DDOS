from scapy.all import DNS, DNSQR, IP, UDP, sr1, Raw

str_server = "192.168.123.109"
dns_server = "219.251.176.190"
domain = "google.com"

def spooping():
    dns_query = DNS(rd=1, qd=DNSQR(qname=domain))
    udp = UDP(dport=50, sport=12345)
    ip = IP(src=str_server,dst=dns_server)
    packet = ip/udp/dns_query
    return packet

def send_dns_query():
    packet = spooping()
    response = sr1(packet)
    return response

def packet_callback(packet):
    SRC = packet[IP].src
    DST = packet[IP].dst
    MES = packet[Raw].load.decode()
    SRC_PORT = packet[UDP].sport
    DST_PORT = packet[UDP].dport
    print("\033[1m\033[96m" + "Source IP: " + "\033[0m" + SRC)
    print("\033[1m\033[96m" + "Source PORT: " + "\033[0m" + str(SRC_PORT))
    print("\033[1m\033[96m" + "Destination IP: " + "\033[0m" + DST)
    print("\033[1m\033[96m" + "Destination PORT: " + "\033[0m" + str(DST_PORT))
    try:
        print("\033[1m\033[93m" + "Message: " + "\033[0m" + MES)
    except:
        pass

if __name__ == "__main__":
    response = send_dns_query()
    packet_callback(response)

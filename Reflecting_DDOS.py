from scapy.all import DNS, DNSQR, IP, UDP, sr1

str_server = "192.168.123.109"
dns_server = "219.251.176.190"
domain = "google.com"

def spooping():
    dns_query = DNS(rd=1, qd=DNSQR(qname=domain))
    print(dns_query)
    udp = UDP(dport=53, sport=12345)
    print(udp)
    ip = IP(src=str_server,dst=dns_server)
    print(ip)
    packet = ip/udp/dns_query
    print(packet)
    return packet

def send_dns_query():
    packet = spooping()
    print(packet)
    response = sr1(packet)
    return response

response = send_dns_query()
print(response.show())

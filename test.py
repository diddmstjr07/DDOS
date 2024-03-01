from scapy.all import sniff, Raw

def packet_callback(packet):
    if Raw in packet:
        payload = packet[Raw].load
        if "Reflect Spoofing Attack" in payload.decode():
            print("Attack detected: " + payload.decode())

# 'host 192.168.123.160 and port 8000'를 필요한 IP 주소 및 포트로 교체하세요.
sniff(filter="host 192.168.123.160", prn=packet_callback)
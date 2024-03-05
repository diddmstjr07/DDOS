import module.GET as GET
import module.internet_protocol as internet

str_server = "192.168.1.181"
dns_server = "219.251.176.190"
port = "8000"

GET.GET(str_server, dns_server, 2193, 8000)
internet.signal_get(dns_server, port)

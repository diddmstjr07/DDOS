import module.GET as GET

str_server = GET.INNERIP()
dns_server = "182.213.254.158"
port = "8000"

GET.GET(str_server, dns_server, 2193, 8000)
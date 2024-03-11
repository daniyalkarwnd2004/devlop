def func_ip(func):
    def inner(ip):
        list_ip = []
        list_ip = ip.split(".")
        for i in list_ip:
            i = int(i)
            if 0 < i <= 255:
                continue
            else:
                print("invalid ip address")
        print("correct ip address")
    return inner


@func_ip
def ip_address(ip):
    print("ip address")


ip = input("please your ip address : ")
ip_address(ip)

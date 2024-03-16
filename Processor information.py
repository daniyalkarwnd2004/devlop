import psutil
print("physical cores :", psutil.cpu_count(logical=False))
print("total cores :", psutil.cpu_count(logical=True))
cpufreq = psutil.cpu_freq()
print(f"max frequency : {cpufreq.max:.2f}Mhz")
print(f"mix frequency : {cpufreq.min:.2f}Mhz")
print(f"current frequency :{cpufreq.current:.2f}Mhz")
print("CPU Usage Per Core :")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"core {i}: {percentage}%")
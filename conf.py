#Script Require to edit proxychains config file
dirs = input('Input Directory of ip/port list')
try:
	ip = open('{}/ip.txt'.format(dirs))
	port = open('{}/ports.txt'.format(dirs))
	f = open('/etc/proxychains.conf','a')
	ipl = ip.readlines()
	portl = port.readlines()
except Exception as e:
	print(e)
ips = []
ports = []
for ip_S in ipl:
	ips.append(ip_S.strip('\n'))
for port_S in portl:
	ports.append(port_S.strip('\n'))
i = 0
while i < len(ips):
	f.write("http\t%s\t%s\n" %(ips[i], ports[i]))
	print("writting")
	i = i +1
f.close
ip.close
port.close
print("Done")

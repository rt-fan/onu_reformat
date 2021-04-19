result = ''
with open("all_cfg.txt") as f:
    for line in f:
        if '###' in line:
            ip_zte = line.split()[1]
        if 'interface gpon-olt' in line:
            olt = line.split()[-1]
            olt = olt.split('/')
            olt = str(olt[1]) + "_" + str(olt[2])
            olt = ip_zte + "_zte_" + olt
        if 'type' in line:
            onu = line.split()[1]
            serial_number = line.split()[-1]
            result = olt + ':' + onu + ' ' + serial_number
            print(result)

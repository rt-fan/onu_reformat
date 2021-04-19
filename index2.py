file1 = open("login_onu.txt", 'r')
file3 = open("result.txt", 'w+')

prevline = ''
onu = ''
for line1 in file1:
    if '10.11.' in line1:
        a = line1.strip() + ' '
        file2 = open("output_onu.txt", 'r')
        for line2 in file2:
            if a in line2:
                onu = line2.split()[1]
                print(onu)
                file3.write(onu + '\n')
        file2.close()
    prevline = line1.strip()
    file3.write(prevline + '\n')

file1.close()

file3.close()

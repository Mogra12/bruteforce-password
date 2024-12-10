import time

wordlist = 'rockyou.txt'
password = '2326'
i = 0

with open(wordlist, 'r', encoding='latin-1') as wl:
    initial_time = time.time()
    for line in wl:
        line = line.strip()
        if line == password:
            print("\nPassword Cracked")
            print(f"Password: {line}\n")
            exe_time = time.time() - initial_time 
            print(exe_time)
            break
        else:
            print(line)
            
    
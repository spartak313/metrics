import psutil
from sys import argv

def get_cpu_info():
    c = psutil.cpu_times()
    print('CPU')
    print('system.cpu.idle   ' + str(c[3]))
    print('system.cpu.user   ' + str(c[0]))
    print('system.cpu.guest  ' + str(c[8]))
    print('system.cpu.iowait ' + str(c[4]))
    print('system.cpu.stolen ' + str(c[7]))
    print('system.cpu.system ' + str(c[2]))

def get_mem_info():
    mem = psutil.virtual_memory()
    swp = psutil.swap_memory()
    print('MEM')
    print('virtual total     ' + str(mem[0]))
    print('virtual used      ' + str(mem[3]))
    print('virtual free      ' + str(mem[1]))
    print('virtual total     ' + str(mem[9]))
    print('swap total        ' + str(swp[0]))
    print('swap used         ' + str(swp[3]))
    print('swap used         ' + str(swp[4]))


if len(argv) - 1 > 1:
    print("Please type only 'cpu' or 'mem'")
elif len(argv) - 1 == 0:
    print("Please type 'cpu' or 'mem'")
else:
    if argv[1] == "cpu":
        get_cpu_info()
    elif argv[1] == "mem":
        get_mem_info()
    else:
        print("Incorrect argument. Please type only 'cpu' or 'mem'")

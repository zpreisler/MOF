#!/usr/bin/env python
from os import mkdir,chdir,getcwd,listdir
from shutil import copyfile,copy
print("Make folders")

cwd=getcwd()

length=4096
temp=0.18
mu=-5.20
t_halt=50000000.0
t_klik=10000000000.0
t_meas=5000000.0
isobar=[80,-0.0005,-10]

for n in range(15):
    folder=str(2**n)
    print(folder)
    try:
        mkdir(folder)
    except FileExistsError:
        pass
    
    copy("binding_constants.dat",folder)
    copy("run.sh",folder)

    params=("length\t\t{}\n"
            "temp\t\t{}\n"
            "mu\t\t{}\n"
            "t_halt\t\t{}\n"
            "t_klik\t\t{}\n"
            "t_meas\t\t{}\n"
            "isobar\t\t{}\t{}\t{}".format(2**n,temp,mu,t_halt,t_klik,t_meas,*isobar))

    print("#######")
    print(params)
    chdir(folder)
    f=open("param.dat","w")
    f.write(params)
    chdir(cwd)
    print("")

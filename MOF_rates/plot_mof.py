#!/usr/bin/env python
def main():
    """
    Plot
    """
    from matplotlib.pyplot import figure,show,plot,errorbar,subplots,xlabel,ylabel,subplots_adjust,savefig,gca,legend,xlim
    from numpy import loadtxt,arange,array,sqrt,linspace
    from mof_lattice import MOF_lattice,MOF_data,MOF
    from os import listdir,getcwd,path,walk

    n=100
    f=MOF("800/")

    mof=MOF_lattice(f.length,f.E_s,f.E_m,f.E_t)
    temp=linspace(f.path.min()-0.01,f.path.max()+0.01,n)
    mu=f.mu*temp

    rho=mof.get_loading(mu,temp)

    fig,ax1=subplots()

    ax1.plot(temp,rho,'g-',linewidth=1.0)


    d=next(walk('.'))[1]
    d=["100","200","400","800"]

    for a in d:
        f=MOF(a)

        #errorbar(f.path,f.rho.mean,yerr=sqrt(f.rho.var),linewidth=1.00,elinewidth=6.00,ecolor="y",barsabove=True,color="r",alpha=0.66)
        #ax1.vlines(f.path,ymin=f.rho.min,ymax=f.rho.max,linewidth=0.66,alpha=1.0)
        ax1.plot(f.path,f.rho.mean,"o-",markersize=1.0,alpha=0.33,label=r"$%.1lf\,[^\circ/\mathrm{time}]$"%(1e6*0.0005/(float(a))))

    ax1.annotate(r"slower rate",xy=(0.16,0.5),xytext=(0.1715,0.63),arrowprops=dict(arrowstyle="->"))

    legend(frameon=False)
    xlim(f.path.min()+0.005,f.path.max()-0.005)

    gca().invert_xaxis()


    xlabel(r"$T^*$")
    ylabel(r"$\rho$")
    subplots_adjust(left=0.18,bottom=0.18)
    savefig("mof.png")
    savefig("mof.pdf")

    show()

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Ctrl-C")

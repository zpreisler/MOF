#!/usr/bin/env python
def main():
    """
    Plot
    """
    from matplotlib.pyplot import figure,show,plot,errorbar,subplots,xlabel,ylabel,subplots_adjust,savefig,gca,legend
    from numpy import loadtxt,arange,array,sqrt,linspace,sort
    from mof_lattice import MOF_lattice,MOF_data,MOF
    from os import listdir,getcwd,path,walk

    n=100
    f=MOF('.')

    mof=MOF_lattice(f.length,f.E_s,f.E_m,f.E_t)
    temp=linspace(f.path.min()-0.01,f.path.max()+0.01,n)
    temp=linspace(0.14,0.18,n)
    mu=f.mu*temp

    rho=mof.get_loading(mu,temp)

    fig,ax1=subplots()

    ax1.plot(temp,rho,'g-',linewidth=1.0)


    d=sorted(next(walk('.'))[1],key=lambda x: float(x))
    print(d)

    for a in d:
        f=MOF(a)
        print(f.isobar[0])

        #errorbar(f.path,f.rho.mean,yerr=sqrt(f.rho.var),linewidth=1.00,elinewidth=6.00,ecolor="y",barsabove=True,color="r",alpha=0.66)
        #ax1.vlines(f.path,ymin=f.rho.min,ymax=f.rho.max,linewidth=0.66,alpha=1.0)
        ax1.plot(f.path,f.rho.mean,"o-",markersize=1.0,alpha=0.33,label=f.isobar[0])

    legend(frameon=False)

    gca().invert_xaxis()

    xlabel(r"$T$")
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

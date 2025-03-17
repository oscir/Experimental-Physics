def main():

    import numpy as np
    import matplotlib.pyplot as plt
    import scipy.optimize
    from scipy.signal import find_peaks
    import os

    mA = 1
    mB = 1
    file = "/Users/oscarfabricius/codeprjects/ExpPhys/teststød0.txt"
    t, xA, yA, xB, yB = np.loadtxt(file, skiprows=3, unpack=True)

    fig1, ax = plt.subplots(1,3, figsize=(12,8))
    plt.grid("on")
    ax[0].plot(t,xA, "x")
    ax[0].plot(t,xB, "x")
    ax[1].plot(t,yA, "x")
    ax[1].plot(t,yB, "x")
    ax[2].plot(xA,yA, "x")
    ax[2].plot(xB,yB, "x")
    plt.tight_layout()
    ax[2].set_aspect("equal")

    pucksize = 9000
    vAx = np.gradient(xA)
    vAy = np.gradient(yA)
    aAx = np.gradient(vAx)
    aAy = np.gradient(vAy)
    vBx = np.gradient(xB)
    vBy = np.gradient(yB)
    aBx = np.gradient(vBx)
    aBy = np.gradient(vBy)

    fig2, axes = plt.subplots(figsize=(12,9))
    axes.set_ylim(-0.25,0.25)
    axes.set_xlim(-0.3,0.25)
    axes.grid("on")
    discA = axes.scatter([], [], s=pucksize, color='red', zorder=9)
    discB = axes.scatter([], [], s=pucksize, color='blue', zorder=9)
    traceA = axes.plot([], [], "--", color='grey')[0]
    traceB = axes.plot([], [], "--", color='grey')[0]
    #vA = axes.plot([],[], "-", zorder=10, color="black")[0]
    vA = axes.arrow(0, 0, 0, 0, width=0.001, zorder=10, color = "black",  length_includes_head=False)
    vB = axes.arrow(0, 0, 0, 0, width=0.001, zorder=10, color = "black",  length_includes_head=False)
    aA = axes.arrow(0, 0, 0, 0, width=0.001, zorder=10, color = "grey",  length_includes_head=False)
    aB = axes.arrow(0, 0, 0, 0, width=0.001, zorder=10, color = "grey",  length_includes_head=False)

    def update(i):
        discA.set_offsets([[xA[i], yA[i]]])
        discB.set_offsets([[xB[i], yB[i]]])
        traceA.set_data(xA[:i],yA[:i])
        traceB.set_data(xB[:i],yB[:i])
        vA.set_data(x=xA[i], y=yA[i], dx=vAx[i]*20, dy =vAy[i]*20)
        vB.set_data(x=xB[i], y=yB[i], dx=vBx[i]*20, dy =vBy[i]*20)
        aA.set_data(x=xA[i], y=yA[i], dx=aAx[i]*20, dy =aAy[i]*20)
        aB.set_data(x=xB[i], y=yB[i], dx=aBx[i]*20, dy =aBy[i]*20)
        return []


    from matplotlib import animation
    plt.rc('animation', html='jshtml')


    Nframes = len(t)
    anim = animation.FuncAnimation(fig2,
                                update,
                                frames=Nframes,
                                interval=30,
                                blit=True)
    anim

    from matplotlib import animation
    plt.rc('animation', html='jshtml')


    Nframes = len(t)
    anim = animation.FuncAnimation(fig2,
                                update,
                                frames=Nframes,
                                interval=30,
                                blit=True)
    


    pAx = vAx*mA
    pBx = vBx*mB
    Px = pAx+pBx

    pAy = vAy*mA
    pBy = vBy*mB
    Py = pAy+pBy

    P = Px+Py
    fig3, ax = plt.subplots(1,2)
    ax[0].set_ylim(-0.05,.05)
    ax[1].set_ylim(-0.05,.05)
    #ax.plot(t, vA)
    #ax.plot(t, vB)
    ax[0].plot(t, Px)
    ax[0].plot(t, pAx)
    ax[0].plot(t, pBx)

    ax[1].plot(t, Py)
    ax[1].plot(t, pAy)
    ax[1].plot(t, pBy)

    plt.show()

if __name__ == "__main__":
    main()

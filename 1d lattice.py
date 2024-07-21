import random
import math
times=[]

latticesize = 20
steps = 10
# LATTICE DETERMINING PARAMETERS

T = 273
# TEMPERATURE

e=2.718281828459045
Kb = 8.62 * 10**(-5)
# boltzmann constant

# (a=1, b=2)
aa = 0.9
bb = 1
ab = 1.1
# BOND ENERGIES

lattice = []
for i in range(latticesize):
    if i == latticesize//2:
        lattice.append(0)
    else:
#        m = random.random()                           #random lattice
#        if m < 0.5:
#            lattice.append(1)
#        else:
#            lattice.append(2)

        lattice.append(1 if (i % 2 == 0) else 2)      #ALTERNATING 1 and 2s 


print("initial lattice: ",lattice)

for j in range(steps):
    print("step:", j+1)
    breakout = False
    for pos in range(latticesize):
        if lattice[pos]==0:
            llattice = lattice.copy()
            rlattice = lattice.copy()

            if lattice[pos-2]==1 and lattice[pos-1]==1:
                left=aa
            elif (lattice[pos-2]==1 and lattice[pos-1]==2) or (lattice[pos-2]==2 and lattice[pos-1]==1):
                left=ab
            else:
                left=bb
            # bond energy to the left of the vacancy

            llattice[pos]=llattice[pos-1]
            llattice[pos-1]=0
            # moving particle to the right
            
            if llattice[pos]==1 and llattice[pos+1]==1:
                newbond=aa
            elif (llattice[pos]==1 and llattice[pos+1]==2) or (llattice[pos]==2 and llattice[pos+1]==1):
                newbond=ab
            else:
                newbond=bb
            # bond energy of the new bond

            leftdeltae=left-newbond
            #print("left is ", left)
            #print("newbond is ", newbond)
            #print("leftdeltae is ", leftdeltae)

            if lattice[pos+2]==1 and lattice[pos+1]==1:
                right=aa
            elif (lattice[pos+2]==1 and lattice[pos+1]==2) or (lattice[pos+2]==2 and lattice[pos+1]==1):
                right=ab
            else:
                right=bb
            # bond energy to the right of the vacancy

            rlattice[pos]=rlattice[pos+1]
            rlattice[pos+1]=0
            'moving particle to the left'
            
            if rlattice[pos]==1 and rlattice[pos-1]==1:
                newbond=aa
            elif (rlattice[pos]==1 and rlattice[pos-1]==2) or (rlattice[pos]==2 and rlattice[pos-1]==1):
                newbond=ab
            else:
                newbond=bb
            # bond energy of the new bond

            rightdeltae=right-newbond
            #print("right is ", right)
            #print("newbond is ", newbond)
            #print("rightdeltae is ", rightdeltae)

            Kleft = math.exp((-1*leftdeltae)/(Kb*T))
            Kright = math.exp((-1*rightdeltae)/(Kb*T))
            #print(f"Kleft: {Kleft}, Kright: {Kright}")

            norm = Kleft + Kright
            nKleft = Kleft / norm
            nKright = Kright / norm
            # normalize K values
            #print(f"Normalized Kleft: {Kleft}, Normalized Kright: {Kright}")

            print("")

            Klist = [nKleft, nKleft+nKright]
            print("Klist: ", Klist)

            n = random.random()
            print("n is: ",n)

            for k in range (2):
                if n < Klist[k]:
                    if k == 0:
                        # chose Kleft
                        lattice[pos]=lattice[pos-1]
                        lattice[pos-1]=0
                        print("vacancy moved left")

                        timestep = (-1 / Kleft) * math.log(n)
                        times.append(timestep)
                    elif k == 1:
                        # chose Kright
                        lattice[pos]=lattice[pos+1]
                        lattice[pos+1]=0
                        print("vacancy moved right")

                        timestep = (-1 / Kright) * math.log(n)
                        times.append(timestep)

                    breakout = True
                    break
                if breakout:
                    break
                        
            print("")
            print("list of timesteps:", times)
            print("changed lattice:", lattice)
            print("")
            print("")
            break

        # SHOULD USE NORMALIZED OR UNNORMALIZED K FOR TIMESTEP??????????
        # record MSD
        # Migration energy instead of delta E
        # periodic boundary conditions (ring of particles)
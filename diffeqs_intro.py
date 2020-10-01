import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Just getting used to plotting
#from http://sam-dolan.staff.shef.ac.uk/mas212/docs/l4.pdf
#this dude is amazing
def logistic(x, t): 
    """Returns the gradient dx/dt for the logistic function"""
    return x*(1-x)

#numerical integration -- needs ODE, initial condition, and ts 
ts = np.linspace(0.0, 10.0, 100)

ics = np.linspace(0.0, 2.0, 10)
for x0 in ics: 
    xs = odeint(logistic, x0, ts)
    plt.plot(ts, xs)
    
plt.xlabel('t', fontsize = 12)
plt.ylabel('initial conditions', fontsize = 12)
plt.title('logistic curve solutions')
plt.show()



#Now getting used to using quivers 
#from https://pythonforundergradengineers.com/quiver-plot-with-matplotlib-and-jupyter-notebooks.html
#this is also really helpful 

x = np.linspace(-5, 5, 10)
y = np.linspace (-5, 5, 10)

#meshgrid creates 2D surface 
#outputs coordinates along axes 
X, Y = np.meshgrid(x, y)
u, v = X/5, -Y/5

#quiver params: (X, Y) starting points; (u, v) directions
fig, ax = plt.subplots()
ax.quiver(X, Y, u, v)

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('vector field for (x/5)i - (y/5)j')
plt.show()


#Now combining to (hopefully) create a phase portrait
#Adapted from http://kitchingroup.cheme.cmu.edu/blog/2013/02/21/Phase-portraits-of-a-system-of-ODEs/
#more Sam Dolan from https://sam-dolan.staff.shef.ac.uk/mas212/notebooks/ODE_Example.html
#this looks like it could also be a good source: 
#http://homepages.math.uic.edu/~jan/mcs320/mcs320notes/lec37.html#numerical-solving-of-ordinary-differential-equations

def dU_dx(U, x): 
    '''
    Convert a second-order to a first-order (y'' = -sin(y) -> z' = -sin(y))
    Let z = y', with the initial condition z(0) = y(0)
    U     -> vector <y, z>
    dU_dx -> vector <y', z'>
    '''
    return [U[1], -np.sin(U[0])]

U0 = [1,1]
xs = np.linspace(0, 10, 200)
Us = odeint(dU_dx, U0, xs)
ys = Us[:,0]

plt.xlabel("x")
plt.ylabel("y")
plt.title("Undamped harmonic oscillator")
plt.plot(xs,ys)
plt.show()

#now adding multiple solutions 
ICs = []
for i in range(10): 
    ICs.append([.01*i, .01*i])
    Us = odeint(dU_dx, ICs[i], xs)
    ys = Us[:, 0]
    plt.plot(xs, ys)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solutions for different ICs")
plt.show()

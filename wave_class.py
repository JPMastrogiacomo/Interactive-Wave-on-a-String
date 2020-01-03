import numpy as np

class Wave:
    def __init__(self):
        self.L = 1 #String length
        self.Nx = 200 #Num spatial points
        self.x = np.linspace(0, self.L, self.Nx+1) #Spatial discretization
        
        
        self.c=0.5 #INSERT SOMETHING
        self.b=0.2 #disipation parameter
        
        self.dt=1./30 #Time step
        self.alt=1 #alternates click-wave up/down
        
        self.u   = np.zeros(self.Nx+1)   #Solution at current time step
        self.u_1 = np.zeros(self.Nx+1)   #Solution one time step back
        self.u_2 = np.zeros(self.Nx+1)   #Solution 2 time steps back
        

        #Apply initial conditions
        x0=0.8*self.L
        a=1
        for i in range(0,self.Nx+1):
            if self.x[i]<x0:
                self.u_1[i]=a*self.x[i]/x0
            else:
                self.u_1[i]=a/(self.L-x0)*(self.L-self.x[i])
         
            
        #First time step, special formula due to boundary
        self.u[1:-1] = self.u_1[1:-1] + \
            0.5*self.c*(self.u_1[0:-2] - 2*self.u_1[1:-1] + self.u_1[2:])
        
        #Boundary conditions
        self.u[0] = 0
        self.u[-1] = 0
    
        #Update 
        self.u_2[:]=self.u_1
        self.u_1[:]=self.u
        
        
    #Performs one step forward in time
    def step(self):
        self.u[1:-1] = (1+0.5*self.b*self.dt)**(-1)*((0.5*self.b*self.dt-1)* \
              self.u_2[1:-1] + 2*self.u_1[1:-1]+ \
              self.c*(self.u_1[0:-2] - 2*self.u_1[1:-1] + self.u_1[2:]))
    
        #Boundary conditions
        self.u[0] = 0
        self.u[-1] = 0        
        
        #Update
        self.u_2[:] = self.u_1
        self.u_1[:] = self.u
 
    
    #Returns current state
    def get_wave(self):
        return (self.x,self.u)
    
    
    #Creates wave on click
    def new_wave(self,x_val):
        index = (np.abs(self.x - x_val)).argmin()
        self.u_2[index-10:index+10]-=0.02*self.alt
        self.alt=-self.alt
    
    
    
def J_IIM(x, y, cx, cy, max_it):
    """Computes an approximation of the Julia set of the quadratic p(z) = z^2 + c
    via inverse iteration"""
    
    """Inputs: 
    z = x + iy: starting point
    c = cx + i cy: the translation
    max_it: maximum number of iterations"""
    
    # List to store the orbit of z
    X = [0]*(max_it)
    Y = [0]*(max_it)
    
    X[0] = x
    Y[0] = y

    for i in range(max_it):
        # Take max_it successive preimages of z, choosing preimages at random
        
        wx = x-cx
        wy = y-cy
        
        # Calculate the square roots, in polar coordinates for ease of calculation        
        if wx > 0:
            theta = np.arctan(wy/wx)
        elif wx < 0:
            theta = np.pi + np.arctan(wy/wx)
        else: # wx = 0
            theta = np.pi/2 
        theta = theta/2
        r = np.sqrt(wx*wx + wy*wy)
    
        # Randomly pick the negative or positive square root
        rand = random.uniform(0, 1) 
        if rand < 0.5:
            r = np.sqrt(r)
        else:
            r = -np.sqrt(r)
            
        x = r*np.cos(theta)
        y = r*np.sin(theta)
            
        # Store the Cartesian coordinates in the list
        X[i] = x
        Y[i] = y
  
    return X, Y
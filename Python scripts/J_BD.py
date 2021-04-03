def J_Level_BD(x, y, cx, cy, max_it, R, alpha):
    """Computes the level set of a point z = x + iy under the quadratic p(z) = z^2 + c,
    to prepare for binary decomposition """
    
    """Inputs: 
    z = x+iy: starting point
    c = cx + cy: translation
    max_it: maximum number of iterations
    R: escape radius (squared)
    alpha: the angle at which to base the binary decomposition """

    x2 = x*x
    y2 = y*y
    
    it = 0
    m = 0
    in_K = True
    
    # Iterate p until the orbit exceeds the escape radius or the max no. of iterations is reached
    while (it < max_it) and (x2+y2 < R):
        temp = x2-y2 + cx
        y = 2*x*y+ cy
        x = temp
        
        x2 = x*x
        y2 = y*y
        
        it = it+1
        
    # If it < max_it, then z is not in K_c 
    if it < max_it:
        
        in_K = False
        
        # Calculate the argument of z
        arg = np.angle(complex(x, y))
            
        # If the argument lies between the two limits, we set m to 1
        if (((2**it)*alpha)%(2*np.pi) <= arg) and (arg <= ((2**it)*alpha + np.pi)%(2*np.pi)):
            m = 1
  
    return it, m, in_K  

def J_BD(K, cx, cy, nx, ny, x_min, x_max, y_min, y_max, max_it, R, alpha):
    """Computes the binary decomposition of the filled-in Julia set of the quadratic p(z) = z^2 + c
    via the level set method"""
    
    """Inputs: 
    K: an output array of size nx*ny
    c = cx + cy: the translation 
    nx, ny: the image resolution in the x- and y direction
    x_min, x_max: the limits of the x-axis in the region
    y_min, y_max: the limits of the y-axis in the region
    max_it: the maximum number of iterations
    R: escape radius (squared)
    alpha: the angle at which to base the binary decomposition"""
    
    # For each pixel in the nx*ny grid, calculate the binary decomposition of the point it represents
    for iy in range(0, ny):
        wy = y_min + iy*(y_max - y_min)/(ny - 1)
        for ix in range(0, nx):
            wx = x_min + ix*(x_max - x_min)/(nx-1)
            
            it, m, in_K = J_Level_BD(wx, wy, cx, cy, max_it, R, alpha)
            
            # If the point is not in the filled Julia set, plot the binary decomposition
            if in_K == False:
                K[ix][iy] = m
            
            # If the point is in the filled Julia set, set it to 0
            else:
                K[ix][iy] = 0
            
    return K
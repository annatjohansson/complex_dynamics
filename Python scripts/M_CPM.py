def M_Pot(cx, cy, max_it, R):
    """Computes the continuous potential of the origin under p(z) = z^2 + c"""
    
    """Inputs: 
    c = cx + cy: translation
    max_it: maximum number of iterations
    R: escape radius (squared)"""
    
    x = 0.0
    y = 0.0
    x2 = 0.0
    y2 = 0.0
    
    it = 0
    
    # Iterate p until orbit exceeds escape radius or max no. of iterations is reached
    while (it < max_it) and (x2 + y2 < R):
        temp = x2 - y2 + cx
        y = 2*x*y + cy
        x = temp
        
        x2 = x*x
        y2 = y*y
        
        it = it + 1
        
    # If the max number of iterations is not exceeded, calculate the potential
    if it < max_it:
        potential = 0.5*np.log(x2 + y2)/pow(2.0, it)
    else:
        potential = 0.0
        
    return potential

def M_CPM(M, nx, ny, x_min, x_max, y_min, y_max, max_it, R):
    """Computes an approximation of the Mandelbrot set via the continuous potential method"""
    
    """Inputs: 
    M: an output array of size nx*ny
    nx, ny: the image resolution in the x- and y direction
    x_min, x_max: the limits of the x-axis in the region
    y_min, y_max: the limits of the y-axis in the region
    max_it: the maximum number of iterations
    R: escape radius (squared)"""
    
    # For each pixel in the grid, calculate the potential of 0 under the corresponding p_c
    for iy in range(0, ny): 
        cy = y_min + iy*(y_max - y_min)/(ny - 1)
        for ix in range(0, nx):
            cx = x_min + ix*(x_max - x_min)/(nx - 1)
            
            # Store the potential in the M array
            M[ix][iy] = M_Pot(cx, cy, max_it, R)
            
    return M
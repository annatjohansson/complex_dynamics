def J_Level(x, y, cx, cy, max_it, R):
    """Computes the level set of a point z = x + iy under p(z) = z^2 + c"""
    
    """Inputs: 
    z = x+iy: starting point
    c = cx + cy: translation
    max_it: maximum number of iterations
    R: escape radius (squared)"""
    
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
        
    return it 
    
def K_LSM(K, cx, cy, nx, ny, x_min, x_max, y_min, y_max, max_it, R):
    """Computes an approximation of the filled-in Julia set of p(z) = z^2 + c
    via the level set method"""
    
    """Inputs: 
    K: an output array of size nx*ny
    c = cx + cy: the translation 
    nx, ny: the image resolution in the x- and y direction
    x_min, x_max: the limits of the x-axis in the region
    y_min, y_max: the limits of the y-axis in the region
    max_it: the maximum number of iterations
    R: escape radius (squared)"""
    
    # For each pixel in the nx*ny grid, calculate the level set of the point
    for iy in range(0, ny):
        wy = y_min + iy*(y_max - y_min)/(ny - 1)
        for ix in range(0, nx):
            wx = x_min + ix*(x_max - x_min)/(nx - 1)
            
            # Store the level set in the K array
            K[ix][iy] = J_Level(wx, wy, cx, cy, max_it, R)
            
    return K
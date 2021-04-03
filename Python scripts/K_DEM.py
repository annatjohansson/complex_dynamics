def K_Dist(x, y, cx, cy, max_it, R):
    """Computes distance of z = x + iy from the filled-in Julia set of p(z) = z^2 + c"""
    
    """Inputs: 
    z = x+iy: starting point
    c = cx + cy: translation
    max_it: maximum number of iterations
    R: escape radius (squared)"""
    
    x2 = 0.0
    y2 = 0.0
    
    it = 0
    
    dist = 0.0
    
    # List to store the orbit of z
    X = [0]*(max_it+1)
    Y = [0]*(max_it+1)
    
    X[0] = x
    Y[0] = y
    
    # Iterate p until orbit exceeds escape radius or max no. of iterations is reached
    while (it < max_it) and (x2 + y2 < R):
        temp = x2 - y2 + cx
        y = 2*x*y + cy
        x = temp
        
        x2 = x*x 
        y2 = y*y
        
        # Store the orbit
        X[it] = x
        Y[it] = y
        
        it = it + 1
        
    # If the escape radius is exceeded, calculate distance of z from K_c
    if (x2 + y2 > R):
        x_der = 0.0
        y_der = 0.0
        i = 0
        flag = False
        
        # Approximate the derivative
        while (i < it) and (flag == False):
            temp = 2*(X[i]*x_der - Y[i]*y_der)+1
            y_der = 2*(Y[i]*x_der + X[i]*y_der)
            x_der = temp
            flag = (max(abs(x_der),abs(y_der)) > (2 ** 31 - 1))
            i = i+1
        
        if (flag == False):
            dist = np.log(x2 + y2)*np.sqrt(x2 + y2)/np.sqrt(x_der*x_der + y_der*y_der)
    
    return dist
        
def K_DEM(K, cx, cy, nx, ny, x_min, x_max, y_min, y_max, max_it, R, threshold):
    """Computes an approximation of the filled-in Julia set of p(z) = z^2 + c
    via the distance estimation method"""
    
    """Inputs: 
    K: an output array of size nx*ny
    c = cx + cy: the translation 
    nx, ny: the image resolution in the x- and y direction
    x_min, x_max: the limits of the x-axis in the region
    y_min, y_max: the limits of the y-axis in the region
    max_it: the maximum number of iterations
    R: escape radius (squared)
    threshold: critical distance from the filled-in Julia set (in pixel units)"""
    
    # Calculate the threshold in terms of distance in the complex plane
    delta = threshold*(x_max - x_min)/(nx - 1)
    
    # For each pixel in the nx*ny grid, calculate the distance of the point
    for iy in range(0, ny):
        wy = y_min + iy*(y_max - y_min)/(ny - 1)
        for ix in range(0, nx):
            wx = x_min + ix*(x_max - x_min)/(nx - 1)  
            
            dist = K_Dist(wx, wy, cx, cy, max_it, R)
    
            #Determine whether the distance is smaller than the critical distance
            if dist < delta:
                K[ix][iy] = 1
            else:
                K[ix][iy] = 0
                
    return K
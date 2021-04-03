# complex_dynamics
Code relevant to my dissertation. The algorithms were adapted from examples in “Fantastic deterministic fractals” written by Heinz-Otto Peitgen, the fourth chapter of the book *The science of fractal images* edited by Michael F. Barnsley et al.  

## J_BD
Code to compute the binary decomposition of the filled-in Julia set of the quadratic p(z) = z^2 + c via the level set method, using the helper function J_Level_BD.

**Input:**
- `K`: an output array of size nx by ny 
- `cx`, `cy`: the translation $c = cx + cy$
- `nx`, `ny`: the image resolution in the x- and y direction 
- `x_min`, `x_max`: the limits of the x-axis in the region 
- `y_min`, `y_max`: the limits of the y-axis in the region 
- `max_it`: the maximum number of iterations 
- `R`: escape radius (squared) 
- `alpha`: the angle at which to base the binary decomposition 

**Output:**
`K`: an array approximating the filled-in Julia set in the region desired, with a binary decomposition of its level sets

## J_IIM
Code to compute an approximation of the Julia set of the quadratic p(z) = z^2 + c via inverse iteration.

**Input:**
- `z` = x + iy: starting point
- `cx`, `cy`: the translation $c = cx + cy$
- `max_it`: the maximum number of iterations 

**Output:**
`X`, `Y`: two arrays of Cartesian coordinates approximating the Julia set

## K_CPM
Code to compute an approximation of the filled-in Julia set of the quadratic p(z) = z^2 + c via the continuous potential method, using the helper function J_Pot

**Input:**

- `K`: an output array of size nx by ny 
- `cx`, `cy`: the translation $c = cx + cy$
- `nx`, `ny`: the image resolution in the x- and y direction 
- `x_min`, `x_max`: the limits of the x-axis in the region 
- `y_min`, `y_max`: the limits of the y-axis in the region 
- `max_it`: the maximum number of iterations 
- `R`: escape radius (squared) 

**Output:**
`K`: an array approximating the filled-in Julia set in the region desired, with the potential of each point in the complement

## K_DEM
Code to compute an approximation of the filled-in Julia set of p(z) = z^2 + c via the distance estimation method, using the helper function J_Dist.

**Input:**
- `K`: an output array of size nx by ny 
- `cx`, `cy`: the translation $c = cx + cy$
- `nx`, `ny`: the image resolution in the x- and y direction 
- `x_min`, `x_max`: the limits of the x-axis in the region 
- `y_min`, `y_max`: the limits of the y-axis in the region 
- `max_it`: the maximum number of iterations 
- `R`: escape radius (squared) 
- `threshold`: critical distance from the filled-in Julia set (in pixel units)

**Output:**
K: an array approximating the filled-in Julia set in the region desired, with the distance of each point near the boundary

## K_LSM
Code to compute an approximation of the filled-in Julia set of p(z) = z^2 + c via the level set method, using the helper function J_Level.

**Input:**
- `K`: an output array of size nx by ny 
- `cx`, `cy`: the translation $c = cx + cy$
- `nx`, `ny`: the image resolution in the x- and y direction 
- `x_min`, `x_max`: the limits of the x-axis in the region 
- `y_min`, `y_max`: the limits of the y-axis in the region 
- `max_it`: the maximum number of iterations 
- `R`: escape radius (squared) 

**Output:**
`K`: an array approximating the filled-in Julia set in the region desired, with the level set decomposition of the complement

## M_BD
Code to compute the binary decomposition of the Mandelbrot set via the level set method, using the helper function M_Level_BD.

**Input:**
- `M`: an output array of size nx by ny 
- `nx`, `ny`: the image resolution in the x- and y direction 
- `x_min`, `x_max`: the limits of the x-axis in the region 
- `y_min`, `y_max`: the limits of the y-axis in the region 
- `max_it`: the maximum number of iterations 
- `R`: escape radius (squared) 
- `alpha`: the angle at which to base the binary decomposition

**Output:**
`M`: an array approximating the Mandelbrot set in the region desired, with a binary decomposition of its level sets

## M_CPM
Code to compute an approximation of the Mandelbrot set via the continuous potential method, using the helper function M_Pot.

**Input:**
- `M`: an output array of size nx by ny 
- `nx`, `ny`: the image resolution in the x- and y direction 
- `x_min`, `x_max`: the limits of the x-axis in the region 
- `y_min`, `y_max`: the limits of the y-axis in the region 
- `max_it`: the maximum number of iterations 
- `R`: escape radius (squared) 

**Output:**
`M`: an array approximating the Mandelbrot set in the region desired, with the potential of each point in the complement

## M_DEM
Code to compute an approximation of the Mandelbrot set via the distance estimation method, using the helper function M_Dist.

**Input:**
- `M`: an output array of size nx by ny 
- `nx`, `ny`: the image resolution in the x- and y direction 
- `x_min`, `x_max`: the limits of the x-axis in the region 
- `y_min`, `y_max`: the limits of the y-axis in the region 
- `max_it`: the maximum number of iterations 
- `R`: escape radius (squared) 
- `threshold`: critical distance from the Mandelbrot set (in pixel units)

**Output:**
`M`: an array approximating the Mandelbrot set in the region desired, with the distance of each point near the boundary

## M_LSM
Code to compute an approximation of the Mandelbrot set via the level set method, using the helper function M_Level.

**Input:**
- `M`: an output array of size nx by ny 
- `nx`, `ny`: the image resolution in the x- and y direction 
- `x_min`, `x_max`: the limits of the x-axis in the region 
- `y_min`, `y_max`: the limits of the y-axis in the region 
- `max_it`: the maximum number of iterations 
- `R`: escape radius (squared) 

**Output:**
`M`: an array approximating the Mandelbrot set in the region desired, with the level set decomposition of the complement

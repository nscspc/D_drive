import matplotlib.pyplot as pl
import numpy as np

x=np.arange(10,20)
y=10*x**2-5*x+45 # be careful about *(multiplication sign) to put , do not put 5x instead of 5*x

pl.plot(x,y,".-")
''' types of line style(to put in pl.plot near x,y,"linestyles")
| 1. "--" (dashed line) | #
| 2. ".-" (solid{continuos} line in which points are marked with dots of bigger size) | #
| 3. "-." (dash-dot line) | #
| 4. "*-" (solid{continuous} line in which points are marked with stars) |
| 5. ":" (dotted line) | #
| 6. "." (dotted line with more space between dots) |
| 7. "-" (solid line) | #
| 8. "_" (underrscore{ _ } is placed on the points) |
| 9. "-^" |
| 10. "-+" |
| 11. "+" |'''

pl.show()

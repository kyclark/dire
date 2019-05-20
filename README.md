# dire

Python equivalent of Perl's warn/die functions.

# Synopsis

````
from dire import *

warn("This will print to sys.stdout")
die("This will `warn` and then `sys.exit(1)`")
````

# Description

I miss having these two functions that in Perl. I find myself defining them in most every program I write, so I'm making this module so I can just `import` them.

# Author

Ken Youens-Clark <kyclark@gmail.com>

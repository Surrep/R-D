from sound import Sound

import matplotlib.pyplot as plt
import sys

s0 = Sound('/Users/tru/Desktop/.../sounds/' + sys.argv[1], 0).normalize()

s = int(sys.argv[2])
e = int(sys.argv[3])

plt.plot(s0.data[s:e], '.')
plt.show()
from sound import Sound

import matplotlib.pyplot as plt
import sys

s0 = Sound('/Users/tru/Desktop/.../sounds/' + sys.argv[1]).normalize()

plt.plot(s0.data, '.')
plt.show()
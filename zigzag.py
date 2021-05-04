import sys
import time

indent = 0
indent_increasing = True

try:
    while True:
        print(f"{' ' * indent}", end='')
        print('********')
        time.sleep(0.2)

        if indent_increasing:
            indent = indent + 1
            if indent == 20:
                indent_increasing = False
            else:
                indent = indent - 1
                if indent == 0:
                    indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
import sys
import json
# this puts stdout in unbuffered mode -- eq to python -u
import unbuffered_io

# print title(s) with $ as first char
print('$Yaw vs. Time')
try:
    while True:
        # read stdin
        line = sys.stdin.readline().strip()
        # transform
        try:
            formatted = json.loads(line)
            output = formatted['yaw']
        except (json.decoder.JSONDecodeError, KeyError):
            continue

        # print
        print(output)

except KeyboardInterrupt:
    pass
finally:
    print('\n\tHeading Adapter Exiting...\n')
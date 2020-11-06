import sys
# this puts stdout in unbuffered mode -- eq to python -u
import unbuffered_io

def get_first_float_in_str(s, split_ch=' '):
    result = 0.0
    for x in s.split(split_ch):
        try:
            # trying to convert x to float
            result = float(x)
            # break the loop if x is the first string that's successfully converted
            break
        except:
            continue
        else:
            return(result)
    return(result)

def get_x_val(split_ch=' '):
    line = sys.stdin.readline().strip()
    return(get_first_float_in_str(line, split_ch))

def get_xy_val():
    line = sys.stdin.readline().strip()
    if line:
        x, y = line.split(',')
    try:
        return(float(x), float(y))
    except:
        pass


def get_xy_vals(split_ch=' '):
    line = sys.stdin.readline().strip()
    split_results = []
    if line:
        vals = line.split(split_ch)
        for val in vals:
            x, y = val.split(',')
            try:
                split_results.append((float(x), float(y)))
            except:
                pass
    return(split_results)


def get_vals(split_ch=','):
    line = sys.stdin.readline().strip()
    if line:
        vals = line.split(split_ch)
    try:
        vals = [float(v) for v in vals]
    except:
        pass
    return(vals)
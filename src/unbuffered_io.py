import io, os, sys
try:
    # Python 3, open as binary, then wrap in a TextIOWrapper
    unbuffered = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), write_through=True)
except TypeError:
    # Python 2
    unbuffered = os.fdopen(sys.stdout.fileno(), 'w', 0)

sys.stdout = unbuffered

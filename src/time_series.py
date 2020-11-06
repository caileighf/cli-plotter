import plotext.plot as plx
from collections import deque
import sys, time, os

# this puts stdout in unbuffered mode -- eq to python -u
import unbuffered_io
from common import get_vals

colors = ['black', ' gray', ' red', ' green', ' yellow', ' orange', ' blue', ' violet', ' cyan', ' bold']
color_pairs = [
    ('cyan', 'violet'),
    ('yellow', 'green'),
    ('red', 'violet'),
    ('orange', 'blue')
]

def get_formatted_canvas():
    plx._set_xlim()
    plx._set_ylim()
    plx._set_grid()
    plx._add_yaxis()
    plx._add_xaxis()
    plx._set_canvas()
    plx._add_equations()
    return(plx._get_canvas())

def create_plot(plot_info, x, y):
    plot_info['y'].append(y)
    plot_info['x'].append(x)
    plx.scatter(plot_info['y'], 
                plot_info['x'], 
                line_color= plot_info['line_color'], 
                point_color=plot_info['point_color'], 
                line=True, 
                equations=True, 
                rows=plot_info['height'])
    plot_info['plots'].append(get_formatted_canvas())
    plx.clear_plot()

    if len(plot_info['x']) > 50:
        plot_info['x'].popleft()
        plot_info['y'].popleft()
    return(plot_info)

def print_plot(plot_info):
    print(plot_info['plots'][-1])
    print('{} -- last value: {}'.format(plot_info['title'], plot_info['x'][-1]))

def main(plots):
    if len(plots) > 1:
        split_ch = ','
    else:
        split_ch = ' '

    while True:
        now = time.time()
        for x, plot in zip(get_vals(split_ch=split_ch), plots):
            plot = create_plot(plot_info=plot, x=x, y=now)
            print_plot(plot)

        plx.sleep(0.2)
        plx.clear_terminal()


if __name__ == '__main__':
    plots = []
    i = 0
    line = sys.stdin.readline().strip()
    while '$' in line:
        plots.append(dict(
            plots=deque(maxlen=2),
            x=deque(),
            y=deque(),
            title=line.split('$')[-1],
            height=10,
            line_color=color_pairs[i][0],
            point_color=color_pairs[i][1],
            ))
        i += 1
        line = sys.stdin.readline().strip()

    try:
        main(plots=plots)
    except KeyboardInterrupt:
        pass
    finally:
        print('\n\tStreaming Time Series Plot Exiting...\n')
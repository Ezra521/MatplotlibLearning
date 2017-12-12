plt.plot()入参介绍：
    绘制线条和/或标记到轴。 args是一个可变长度参数，允许多个x，y对与一个可选的格式字符串。 例如，以下每一项都是合法的：
    plot(x, y)        # plot x and y using default line style and color
    plot(x, y, 'bo')  # plot x and y using blue circle markers
    plot(y)           # plot y using x as index array 0..N-1
    plot(y, 'r+')     # ditto, but with red plusses

    If x and/or y is 2-dimensional, then the corresponding columns will be plotted.
    An arbitrary number of x, y, fmt groups can be specified, as in:

    a.plot(x1, y1, 'g^', x2, y2, 'g-')
    Return value is a list of lines that were added.

    By default, each line is assigned a different color specified by a ‘color cycle’. To change this behavior, you can edit the axes.color_cycle rcParam.

    The following format string characters are accepted to control the line style or marke
    r:
        character	description
        '-'	        solid line style
        '--'	    dashed line style
        '-.'	    dash-dot line style
        ':'	        dotted line style
        '.'	        point marker
        ','	        pixel marker
        'o'	        circle marker
        'v'	        triangle_down marker
        '^'	        triangle_up marker
        '<'	        triangle_left marker
        '>'	        triangle_right marker
        '1'	        tri_down marker
        '2'	        tri_up marker
        '3'	        tri_left marker
        '4'	        tri_right marker
        's'	        square marker
        'p'	        pentagon marker
        '*'	        star marker
        'h'	        hexagon1 marker
        'H'	        hexagon2 marker
        '+'	        plus marker
        'x'	        x marker
        'D'	        diamond marker
        'd'	        thin_diamond marker
        '|'	        vline marker
        '_'	        hline marker
    The following color abbreviations are supported:
         character	color
        ‘b’	    blue
        ‘g’	    green
        ‘r’	    red
        ‘c’	    cyan
        ‘m’	    magenta
        ‘y’	    yellow
        ‘k’	    black
        ‘w’	    white
        如果这两种颜色不够用，还可以通过两种其他方式来定义颜色值：
            1.使用HTML十六进制字符串 color='eeefff' 使用合法的HTML颜色名字（’red’,’chartreuse’等）。
            2.也可以传入一个归一化到[0,1]的RGB元祖。 color=(0.3,0.3,0.4)
        很多方法可以介绍颜色参数，如title()。
        plt.tilte('Title in a custom color',color='#123456'）
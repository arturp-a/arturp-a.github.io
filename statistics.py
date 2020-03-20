from bokeh.plotting import figure, output_file, show

p = figure()
p.circle([1, 2, 3], [4, 5, 6], color="orange")

output_file("foo.html")

show(p)
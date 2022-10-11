import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
"""
-subplots() can generate one or more
plots in the same figure
-fig represents the entire figure or collection
of plots that are generated
-ax represents a single plot in the figure

"""
ax.plot(squares)
"""plot() method will try to plot the data
it's given in a meaningful way"""
plt.show()
"""this line opens Matplotlib viewer and displays the plot"""
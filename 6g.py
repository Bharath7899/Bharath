import turtle

# Create a turtle object
my_pen = turtle.Turtle()

# Set the background color
turtle.bgcolor("black")

# Define a list of colors
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# Loop to create the spiral pattern
for x in range(360):
    my_pen.pencolor(colors[x % 6])  # Change pen color
    my_pen.width(x // 100 + 1)     # Increase pen width gradually
    my_pen.forward(x)              # Move the turtle forward
    my_pen.left(59)                # Turn the turtle left by 59 degrees

                                   # Finish the drawing
turtle.done()

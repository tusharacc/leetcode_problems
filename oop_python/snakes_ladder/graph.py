import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Graph Representation with Turtle")
screen.bgcolor("white")

# Create a turtle to draw the graph
drawer = turtle.Turtle()
drawer.speed(0)
drawer.hideturtle()

# Sample graph dictionary
# graph = {
#     'A': ['B', 'C'],
#     'B': ['C', 'D'],
#     'C': ['D'],
#     'D': ['A'],
#     'E': ['B', 'D']
# }

def draw_graph(graph):
    for i, node in enumerate(graph):
        angle = math.radians(i * angle_increment)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        node_positions[node] = (x, y)

    # Draw nodes
    for node, (x, y) in node_positions.items():
        draw_node(node, x, y)

    # Draw edges
    for start, neighbors in graph.items():
        for end in neighbors:
            draw_edge(start, end)

# Parameters for drawing
    node_radius = 20
    node_positions = {}
    angle_increment = 360 / 20
    radius = 300

# Function to draw a node
def draw_node(name, x, y):
    drawer.penup()
    drawer.goto(x, y - node_radius)
    drawer.pendown()
    drawer.circle(node_radius)
    drawer.penup()
    drawer.goto(x, y - node_radius - 10)
    drawer.write(name, align="center", font=("Arial", 12, "bold"))

# Function to draw an edge
def draw_edge(start, end):
    start_x, start_y = node_positions[start]
    end_x, end_y = node_positions[end]
    drawer.penup()
    drawer.goto(start_x, start_y)
    drawer.pendown()
    drawer.goto(end_x, end_y)

# Calculate positions of nodes


# Keep the window open
turtle.done()

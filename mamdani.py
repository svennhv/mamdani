
class graph:
    # Direction doesn't matter with triangles, but matters if name="grade"

    def __init__(self, start, top, end, name="triangle", direction="right"):
        self.start = start
        self.top = top
        self.end = end
        self.maximum = 1.0 # All of the graphs in the task have a maximum of 1.0
        self.name = name
        self.direction = direction

    def get_value_at(position):
        if name == "triangle":
            return triangle(position, self.start, self.top, self.end, self.maximum)
        elif name == "grade":
            return grade(position, self.start, self.top, self.maximum, self.direction)
        else:
            print("Could not get possition") #for debugging



def fuzzy_or(graph_a, position_a, graph_b, position_b):
    # Positions are x-values of the graphs
    return max(graph_a.get_value_at(position_a), graph_b.get_value_at(position_b))

def fuzzy_and(graph_a, position_a, graph_b, position_b):
    return min(graph_a.get_value_at(position_a), graph_b_get_value_at(position_b))

def fuzzy_not(graph, position):
    return 1 - graph.get_value_at(position)

def triangle(position,start, top, end, maximum): # Function: _/\_
    # X-values: start, top, end. Y-values: maximum

    value = 0.0

    if position in range(start, top):
        value = (position - start) / (top - start)
    elif position in range(top, end):
        value = (end - position) / (top - start)

    if value > maximum:
        value = maximum

    return value

def grade(position, start, top, maximum, direction="right"): #right: __/ , left: \__
    # X-values: start, top, end. Y-values: maximum
    #direction = "left" or "right". Right => Top at right.

    value = 0.0

    if direction == "right":
        if position >= top:
            value = 1.0
        elif position <= start:
            value = 0.0
        else:
            value = (position - start) / (top, start)

    if direction == "left":
        if position <= top:
            value = 0.0
        elif position >= start:
            value = 1.0
        else:
            value = (position - start) / (top, start)

    if value > maximum:
        value = maximum

class rule:

    def __init__(self, condition, action):
       self.condition = condition
       self.action = action

    def evaluation_at(position_a, position_b)
        for dist in distances:
            


def main():
    distance = {
        "verySmall" : graph(0, 1, 2.5, "grade", "left"),
        "small" : graph(1.5, 3, 4.5),
        "perfect" : graph(3.5, 5, 6.5),
    }

    actions = {}
    delta = {}

    # rules = []

def evaluate(distance, delta, rules): # Returns action
    # Evaluates distance and delta with given list of rules
    rule1.getprob()
    rule2.getprob()

    for rule in 

    return max(rule1.getProbability(), rule2.getProbabillijl()g



main()

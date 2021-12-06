import numpy as np

line_pairs = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        # replace many space to one space
        pairs = [pose.split(',') for pose in line.split(' -> ')]
        line_pairs.append([list(map(int, x)) for x in pairs])
    pass

line_pairs = np.array(line_pairs)

max_num = line_pairs.max() + 1
image = np.zeros([max_num, max_num])

def DrawLine(image, start_point, end_point, type):
    vector = end_point - start_point
    steps = abs(vector[type])
    if steps < 1:
        return False
    # normalize vector
    vector = vector // steps
    for t in range(0, steps + 1):
        target = start_point + t * vector
        image[target[1]][target[0]] +=1
    return True

# part 1
for start_point, end_point in line_pairs:
    if start_point[0] == end_point[0]:
        DrawLine(image, start_point, end_point, 1)            

    if start_point[1] == end_point[1]:
        DrawLine(image, start_point, end_point, 0)

    pass

print((np.asarray(image) > 1).sum())

# part 2
for start_point, end_point in line_pairs:    
    # base on part 1 is done
    # only add diagonal lines
    vec = start_point - end_point
    if abs(vec[0]) == abs(vec[1]):
        DrawLine(image, start_point, end_point, 0)

    pass

print((np.asarray(image) > 1).sum())

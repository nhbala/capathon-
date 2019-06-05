import json
from numpy import dot
from numpy.linalg import norm



json_object = json.load(open("vectors.json"))
final_listing = []
for item in json_object:
    curr_vector = json_object[item]
    cos_sim = dot(compare_vector, curr_vector)/(norm(compare_vector)*norm(curr_vector))
    final_values = (cos_sim, item)
    final_listing.append(final_values)

sorted_list = sorted(final_listing, key=lambda x: x[0])

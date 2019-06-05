import json
from numpy import dot
from numpy.linalg import norm



json_object = json.load(open("vectors.json"))
final_listing = []
for item in json_object:
    compare_vector = [0.05285657863764055, 0.09200581398368625, 0.08647085331388142, 0.10208201448385008, 0.0739814049754188, 0.12960785319940513, 0.09039452358637866, 0.09631238777010753, 0.11036108237661137, 0.07875876517668104, 0.08716872249633985, 0.010386595426806535, 0.00936139879660677, 0.020198316180239328, 0.016401899517225788, 0.011745663976092535, 0.01571078256710733, 0.022451691932827565, 0.02880263391079119, 0.011859205359901263, 0.01434465014398877, 0.015612096094446496, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
    curr_vector = json_object[item]
    cos_sim = dot(compare_vector, curr_vector)/(norm(compare_vector)*norm(curr_vector))
    final_values = (cos_sim, item)
    final_listing.append(final_values)

sorted_list = sorted(final_listing, key=lambda x: x[0])

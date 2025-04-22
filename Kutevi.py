def main(n, k, known_angles, req_angles):
    all_angles = []
    all_angles.append(known_angles[0] + known_angles[1])
    all_angles.append(abs(known_angles[0] - known_angles[1]))
    for i in range(2, len(known_angles)):
        index = len(all_angles)
        for j in range(index):
            all_angles.append(all_angles[j] + known_angles[i])
            all_angles.append(abs(all_angles[j] - known_angles[i]))
    print(all_angles)
    
    

n = 3
k = 2
known_angles = [30.0, 45.0, 60.0]
req_angles = [90.0, 120.0]
main(n, k, known_angles, req_angles)
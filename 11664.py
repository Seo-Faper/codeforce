import math

def distance_between_points(A, B):
    return math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2 + (B[2] - A[2])**2)

def distance_to_segment(A, B, C):
    AB = [B[0] - A[0], B[1] - A[1], B[2] - A[2]]
    AC = [C[0] - A[0], C[1] - A[1], C[2] - A[2]]
    BC = [C[0] - B[0], C[1] - B[1], C[2] - B[2]]

    # 선분 AB의 길이
    length_AB = distance_between_points(A, B)

    # 벡터의 내적을 이용하여 선분 AB와 점 C 사이의 수직 거리를 구함
    dot_product_AB_AC = sum([AB[i] * AC[i] for i in range(3)])
    dot_product_BA_BC = sum([-AB[i] * BC[i] for i in range(3)])

    if dot_product_AB_AC <= 0:  # C가 선분의 A쪽으로 수직 거리가 가장 가까운 경우
        return distance_between_points(A, C)
    elif dot_product_BA_BC <= 0:  # C가 선분의 B쪽으로 수직 거리가 가장 가까운 경우
        return distance_between_points(B, C)
    else:  # C가 선분 내에 있는 경우
        # 선분 AB를 향하는 단위 벡터
        unit_AB = [AB[i] / length_AB for i in range(3)]
        # 선분 AB 위의 점과 C의 거리를 구하여 반환
        distance = distance_between_points(A, [A[i] + unit_AB[i] * dot_product_AB_AC for i in range(3)])
        return distance

# 입력값을 받아옵니다.
Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(float, input().split())

# 선분과 점 사이의 최소 거리를 계산합니다.
A = (Ax, Ay, Az)
B = (Bx, By, Bz)
C = (Cx, Cy, Cz)
min_distance = distance_to_segment(A, B, C)

print(min_distance)

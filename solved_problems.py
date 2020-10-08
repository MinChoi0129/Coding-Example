i_solved = [1000, 1001, 1002, 1008, 1009, 1011, 1037, 1065, 1085, 1110, 1152, 1157, 1181, 1193, 1316, 1330, 1427, 1546, 1676, 1712, 1904, 1924, 1929, 1934, 1978, 2004, 2108, 2163, 2231, 2292, 2312, 2438, 2439, 2441, 2446, 2447, 2455, 2523, 2557, 2558, 2562, 2577, 2581, 2588, 2609, 2675, 2739, 2741, 2742, 2747, 2748, 2750, 2751, 2753, 2775, 2798, 2839, 2869, 2884, 2908, 2920, 2941, 2981, 3009, 3036, 3046, 3052, 3053, 4153, 4344, 4673, 4948, 5086, 5543, 5585, 5622, 7287, 7568, 8393, 8958, 9020, 9375, 9498, 10039, 10171, 10172, 10250, 10430, 10718, 10773, 10809, 10814, 10817, 10818, 10828, 10869, 10870, 10871, 10872, 10950, 10951, 10952, 10953, 10989, 10996, 10998, 11021, 11022, 11047, 11050, 11051, 11399, 11650, 11651, 11653, 11654, 11720, 11729, 11758, 14681, 15552, 15596, 15649, 15650, 15651, 15652, 19532]

level = [\
    [1008, 1330, 2438, 2557, 2562, 2675, 2739, 2920, 8958, 10818, 10869, 10950, 10951, 10952, 11654, 11720], \
    [1018, 1085, 1181, 1259, 1920, 1978, 2164, 2609, 2751, 2798, 9012, 10250, 10814, 10816, 10828, 10845, 10866, 11050, 11650, 11866], \
    [1003, 1012, 1074, 1463, 1620, 1697, 1764, 1927, 1931, 2606, 2630, 7576, 7662, 9095, 11279, 11399, 11723, 11724, 11726, 18870], \
    [1149, 1167, 1629, 1753, 1786, 1865, 1918, 1932, 1967, 1991, 2206, 2263, 2407, 9251, 9465, 9663, 11053, 11404, 11660, 11725, 12865, 13549, 15650, 15654], \
    [1005, 1197, 1806, 2056, 2098, 2166, 2239, 2252, 2467, 2473, 2568, 2623, 7453, 7579, 9252, 9328, 9466, 10942, 11049, 11437, 12100, 12852, 13460, 14003]
]

def underline():
    for _ in range(100):
        print("-", end = '')
    print("")
    
def show(n, arr, my_sovled):
    
    underline()
    solved = []
    unsolved = []

    for i in arr: #필수 문제를 돌면서
        if i in my_sovled:
            solved.append(i) #푼 문제 담기
        else:
            unsolved.append(i) #안 푼 문제 담기
    
    cnt_sol = len(solved)
    cnt_unsol = len(unsolved)
    pc_sol = 100.0 * cnt_sol / len(arr)
    pc_unsol = 100.0 * cnt_unsol / len(arr)
    
    print("Level%d 의 문제 수는 %d개 입니다." % (n, len(arr)))
    print("미해결 문제개수, 해결 문제개수 : (%d문제 (%.1fpercent), %d문제 (%.1fpercent))" % (cnt_unsol, pc_unsol, cnt_sol, pc_sol))
    print("  해결 문제번호 : ", end = '')
    print(solved)
    print("미해결 문제번호 : ", end = '')
    print(unsolved)
    
for i in range(1, 6):
    show(i, level[i - 1], i_solved)
import json

def recommend_cpu_frequency(task_size_range):
    range_size = task_size_range[1] - task_size_range[0]
    
    if range_size <= 1000:
        return 700000  
    elif range_size <= 5000:
        return 1200000  
    else:
        return 1800000

def get_task_sizes():
    start1 = 10 # pod1(workernode 1)
    end1 =  999
    start2 = 1000 # pod2(workernode 2)
    end2 = 1500
    return (start1, end1), (start2, end2)

# 작업 크기 범위 입력받기
task_range1, task_range2 = get_task_sizes()

pod1_task_size = task_range1[1] - task_range1[0] + 1
pod2_task_siee = task_range2[1] - task_range2[0] + 1

# 각 범위에 대한 권장 CPU 주파수 계산
recommended_freq1 = recommend_cpu_frequency(task_range1)  # 첫 번째 범위 사용
recommended_freq2 = recommend_cpu_frequency(task_range2)  # 두 번째 범위 사용

print(f"Task Range(pod1) {task_range1[0]}~{task_range1[1]} recommended CPUfreq: {recommended_freq1}MHz")
print(f"Task Range(pod2) {task_range2[0]}~{task_range2[1]} recommended CPUfreq: {recommended_freq2}MHz")

# 각 파드 정보를 JSON 형식으로 생성
pod1_info = {
    "pod_name": "pod1",
    "task_size_range": task_range1,
    "task_size": pod1_task_size,
    "recommended_cpu_frequency": recommended_freq1
}

pod2_info = {
    "pod_name": "pod2",
    "task_size_range": task_range2,
    "task_size":pod2_task_siee,
    "recommended_cpu_frequency": recommended_freq2
}

# pod1_info를 pod1_info.json 파일에 저장
with open('pod1_info.json', 'w') as json_file:
    json.dump(pod1_info, json_file, indent=4)

# pod2_info를 pod2_info.json 파일에 저장
with open('pod2_info.json', 'w') as json_file:
    json.dump(pod2_info, json_file, indent=4)


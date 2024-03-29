#!/bin/bash

while true; do
	# 작업 데이터 수신
	json=$(curl -s http://192.168.0.27:5002/get_pod2)

	# 작업 데이터 파싱
	pod_name=$(echo $json | jq -r '.pod_name')
	task_size_range_start=$(echo $json | jq -r '.task_size_range[0]')
	task_size_range_end=$(echo $json | jq -r '.task_size_range[1]')
	task_size=$(echo $json | jq -r '.task_size')
	recommended_cpu_frequency=$(echo $json | jq -r '.recommended_cpu_frequency')

	# 권장 주파수 설정
	cpufreq-set -f $recommended_cpu_frequency

	# 현재 주파수 확인
	current_cpu_freq=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq)


	echo "Pod Name: $pod_name"
	echo "Task Size Range: $task_size_range_start - $task_size_range_end"
	echo "Task Size: $task_size"
	echo "Recommended CPU Frequency: $recommended_cpu_frequency"
	echo "Current CPU Frequency: $current_cpu_freq" 
	
	start_time=$(date +%s.%N)
	
	# 연산 수행
	result=0
	for ((i = ${task_size_range_start}; i <= ${task_size_range_end}; i++)); do
    	result=$((result + i))
	done

	end_time=$(date +%s.%N)
	
	execution_time=$(printf "%.6f" $(echo "$end_time - $start_time" | bc))
	echo "Excution Time: $execution_time sec"
	
	# 결과 데이터 송신
	curl -X POST -H "Content-Type: application/json" -d '{
    "pod_name": "'"$pod_name"'", 
    "task_size_range": ['"$task_size_range_start"', '"$task_size_range_end"'], 
    "task_size": '"$task_size"', 
    "recommended_cpu_frequency": '"$recommended_cpu_frequency"', 
    "current_cpu_frequency": '"$current_cpu_freq"', 
    "execution_time": '"$execution_time"'
}' http://192.168.0.27:5002/receive_data_pod2
	
	sleep 5
done

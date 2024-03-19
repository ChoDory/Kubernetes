import pandas as pd
import matplotlib.pyplot as plt

def ex1_cpu_freq_graph(file_path):
    # CSV 파일 읽기
    df = pd.read_csv(file_path)

    # current_cpu_frequency 값에 대한 execution_time의 평균 계산
    mean_exec_times = df.groupby('current_cpu_frequency')['execution_time'].mean()

    # 그래프 그리기
    plt.bar(mean_exec_times.index.astype(str), mean_exec_times.values)
    plt.xlabel('Current CPU Frequency')
    plt.ylabel('Average Execution Time')
    plt.title('Average Execution Time for Different CPU Frequencies')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 함수 실행
ex1_cpu_freq_graph('/Users/chominjun/Desktop/Workspace/PYTHON_workspace/K8s_distributed_computing/result_ex1.csv')

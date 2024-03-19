# 베이스 이미지로 Debian Buster 사용
FROM debian:buster-slim

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    curl \
    jq \
    bc \
    cpufrequtils \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /app

# 스크립트 파일 복사 (파일 이름을 pod1.sh로 지정)
COPY pod1.sh /app/pod1.sh

# 실행 권한 부여
RUN chmod +x /app/pod1.sh

# 스크립트 실행
CMD ["/app/pod1.sh"]

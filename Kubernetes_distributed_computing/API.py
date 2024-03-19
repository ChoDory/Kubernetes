from flask import Flask, jsonify, request
import json
import csv

app = Flask(__name__)

@app.route('/get_pod1', methods=['GET'])
def get_pod1_data():
    with open('pod1_info.json', 'r') as json_file:
        data = json.load(json_file)
    return jsonify(data)

@app.route('/get_pod2', methods=['GET'])
def get_pod2_data():
    with open('pod2_info.json', 'r') as json_file:
        data = json.load(json_file)
    return jsonify(data)

@app.route('/receive_data_pod1', methods=['POST'])
def receive_data_pod1():
    data = request.json  # JSON 데이터를 파싱

    # CSV 파일명 정의
    csv_file_name = 'received_data_pod1.csv'

    # CSV 파일 열기
    with open(csv_file_name, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # CSV 파일이 비어있다면, 헤더를 작성
        if csvfile.tell() == 0:
            writer.writerow(data.keys())

        # 데이터 쓰기
        writer.writerow(data.values())
    # 성공 메시지 반환
    return jsonify({"status": "success", "message": "Data received successfully."})

@app.route('/receive_data_pod2', methods=['POST'])
def receive_data_pod2():
    data = request.json  # JSON 데이터를 파싱
    
    csv_file_name = 'received_data_pod2.csv'

    # CSV 파일 열기
    with open(csv_file_name, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # CSV 파일이 비어있다면, 헤더를 작성
        if csvfile.tell() == 0:
            writer.writerow(data.keys())

        # 데이터 쓰기
        writer.writerow(data.values())
    # 성공 메시지 반환
    return jsonify({"status": "success", "message": "Data received successfully."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

from flask import Flask
from flask import Flask, jsonify

app = Flask(__name__)

tlqkf = {
    "message":"hello,world"
}

@app.route('/')
def index():
    return '안뇽 명숍앙'

@app.route('/hello')
def hello():
    return jsonify(tlqkf["message"])
            # dict를 json으로 바꿔줌 (근데 난 json이 뭔지도 모름 ㅋㅋ)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    # 개 ㅈ같은 set FLASK_DEBUG=true 아무리 해도 안되길레 걍 이리 함
    
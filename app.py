from flask import Flask, Response, abort
import requests

app = Flask(__name__)


@app.route("/cors-bypass/<path:img_path>", methods=["GET"])
def cors_bypass(img_path):
    custom_headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    try:
        img_file = requests.get(img_path.replace('¿', '?'), headers=custom_headers).content
    except requests.exceptions.MissingSchema:
        abort(400, "it is not url form")
    except Exception as e:
        print(e.__class__)
        print(e)
        abort(500)

    return Response(response=img_file, mimetype="image/jpg")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5050)

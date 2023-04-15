from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def reverse_name():
    name = request.args.get('name')
    if name is None:
        text = "Enter the input string"
    else:
        text = name[::-1]

    return text





if __name__ == "__main__":
    app.run(debug=True)

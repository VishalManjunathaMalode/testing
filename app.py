from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_data():
    data = request.form['input_data']  # Get the input data from the form
    # Process the data here
    print(data.replace("sushma","vishal"))
    return (data.replace("sushma","vishal"))

# Add CORS headers
@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


if __name__ == '__main__':
    app.run()

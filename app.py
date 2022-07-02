from chalice import Chalice

app = Chalice(app_name='chalice-efs-read-write')


@app.route('/')
def index():
    with open('/mnt/lambda/hello.txt') as f:
        contents = f.read()
    return {'contents': contents}

# USAGE: curl $(chalice url)write/hi.txt/hi
@app.route('/write/{file}/{contents}')
def write(file, contents):
    try:
        with open(f'/mnt/lambda/{file}', 'w') as f:
            f.write(contents)
        return True
    except:
        return False

# USAGE: curl $(chalice url)read/hi.txt
@app.route('/read/{file}')
def write(file):
    try:
        with open(f'/mnt/lambda/{file}') as f:
            contents = f.read()
        return contents
    except:
        return False



# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#

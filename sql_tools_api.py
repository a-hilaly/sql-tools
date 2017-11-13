from flask import Flask, jsonify, make_response, request, abort
from sql_tools.mysql import MYSQL

app = Flask(__name__)

#############################

@app.errorhandler(404)
def not_found(error):
    """
    """
    return make_response(jsonify({'error': 'URL Not found'}), 404)

def _error(error, msg, exception=None):
    if exception:
        return make_response(jsonify({'error' : msg,
                                      'code' : error,
                                      'exception msg': exception}))
    return make_response(jsonify({'error' : msg, 'code': error}))


#############################
# General Schema #
#############################


@app.route('/sql_tools/v1/test', methods=['GET'])
def test():
    """
    """
    return jsonify({'working': 'OK'})

#curl -H "Content-Type: application/json" -X GET -d '{"function":"tables", "function_args": ["jaja"]}' http://localhost:5000/sql_tools/v1/mysql/execute
@app.route('/sql_tools/v1/mysql/execute', methods=['GET'])
def execute():
    """
    """
    wk = None
    if not request.json:
        abort(400)
    try:
        function = request.json.get('function')
        function_args = request.json.get('function_args') or []
        function_kwargs = request.json.get('function_kwargs') or {}
        f = getattr(MYSQL, function)
        res = f(*function_args, **function_kwargs)
        wk = True
    except:
        res = None
        wk = False

    return jsonify({'working' : wk, 'output' : res})


if __name__ == '__main__':
    app.run(debug=True)

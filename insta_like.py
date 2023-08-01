from flask import Flask, jsonify, request

app = Flask(__name__)

list = [
    {'id':1,'username':'murli','caption':'any'}
]

@app.route('/post', methods=['POST'])
def create():
    data = request.get_json()
    username = data.get('username')
    caption = data.get('caption')

    post = {
        'id':len(list)+1,
        'username':username,
        'caption':caption 
    }

    list.append(post)
    return jsonify(post)

@app.route('/allpost', methods=['GET'])
def view():
    return jsonify(list)


@app.route('/delete/<int:pid>',methods=['DELETE'])
def deletePost(pid):
    data = {}
    for i in list:
        if i['id']==pid:
            data = i
        else:
            data = None

    if data:
        list.remove(data)
        return jsonify(data)
    else:
        return jsonify({'error':'Post not found'})

if __name__=='__main__':
    app.run()

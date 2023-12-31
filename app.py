from flask import Flask, render_template, request, jsonify
from pushbullet import Pushbullet

app = Flask(__name__)

# Replace with your FCM server key
key = ("o.wfjOUuNbwNCinQbZRgocfYY19wQxozvW")
authentication_key = "amas@8016"

# # Web push notification route
@app.route('/send', methods=['GET'])
def send_push_notification():
    name = request.args.get('name')
    provided_key = request.headers.get('Authorization')
    if not provided_key or provided_key != f'Bearer {authentication_key}':
        return jsonify({'status': False}), 401

    pb = Pushbullet(key)
    push = pb.push_note('Web Message', F'{name} want to talk')
    if push:
        return jsonify({'status': True})
    else:
        return jsonify({'status': False})
    

if __name__ == '__main__':
    app.run(debug=True)

# pb = Pushbullet(key)
# push = pb.push_note('New Message', 'Arnab want to talk')
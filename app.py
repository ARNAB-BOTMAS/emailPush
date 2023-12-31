from flask import Flask, render_template, request, jsonify
from pushbullet import Pushbullet

app = Flask(__name__)

# Replace with your FCM server key
key = ("o.wfjOUuNbwNCinQbZRgocfYY19wQxozvW")


# # Web push notification route
@app.route('/send', methods=['GET'])
def send_push_notification():
    name = request.args.get('name')
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
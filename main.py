import json
import os

from flask import jsonify, Flask, render_template
import requests

app = Flask(__name__)

ZOOM_BASE_URL = 'https://api.zoom.us/v2'
ZOOM_METRICS_ENDPOINT = 'metrics/meetings?type=live'
ZOOM_MEETINGS_ENDPOINT = 'meetings'
ZOOM_TOKEN = os.getenv('ZOOM_TOKEN')
REQUEST_SUCCESS_MESSAGE = {
    "status": "OK"
}

REQUEST_FAILURE_MESSAGE = {
    "status": "Failure"
}


@app.route('/get_meetings_list', methods=['GET'])
def get_meetings_list():
    try:
        meetings_data_for_ui = {}
        meetings_data_for_ui['meetings'] = {}
        meetings_for_ui = []
        meetings_list_from_zoom = requests.get(url=f'{ZOOM_BASE_URL}/{ZOOM_METRICS_ENDPOINT}',
                                               headers={'Authorization': ZOOM_TOKEN}).json()
        for meeting in meetings_list_from_zoom['meetings']:
            meetings_for_ui.append({'meeting_id': meeting['id'],
                                    'participants_amt': meeting['participants']})
        return jsonify(meetings_for_ui)
    except:
        print('errors something')


@app.route('/stop_meeting/<meeting_id>', methods=['PUT'])
def stop_meeting(meeting_id):
    end_meeting_data = {
        "action": "end"
    }
    response = requests.put(url=f'{ZOOM_BASE_URL}/{ZOOM_MEETINGS_ENDPOINT}/{meeting_id}/status',
                            headers={'Authorization': ZOOM_TOKEN},
                            json=end_meeting_data)
    if response.status_code == 204:
        return jsonify(REQUEST_SUCCESS_MESSAGE)
    else:
        return jsonify(REQUEST_FAILURE_MESSAGE)


@app.route('/index', methods=['GET'])
def index():
    return render_template('list_meetings.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', use_reloader=True, port=80)

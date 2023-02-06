from flask import Flask, render_template, request

from loadtest_trigger_webapp.webapp_flask.api_requests_http import postCall_without_auth

app = Flask(__name__)


def trigger_message_to_slack(cluster, message):
    slack_url = f'http://nemesis.internal.{cluster}.mindtickle.com/messenger/slack/send_message'
    # slack_channel = f'track_{cluster}'
    slack_channel = 'test_report_1'
    payload = {
        "channel": slack_channel,
        "message": {
            "type": "text",
            "content": message,
            "thread_ts": ""
        }
    }
    try:
        resp = postCall_without_auth(slack_url, payload)
    except Exception as err:
        raise Exception(f'Error while sending message via slack: {str(err)}')
    print(
        f'Successfully triggered slack message for load test completion | SLACK_CHANNEL: {slack_channel}')


@app.route('/load_test/trigger_command', methods=['POST'])
def do_trigger() -> 'html':
    """Extract the posted data; perform the load test trigger; return results."""
    tc_id = request.form['tc_id']
    track = request.form['track']
    cluster = request.form['cluster']
    historical_tracking = request.form['historical_tracking'].lower()
    baseline_test = request.form['baseline_test'].lower()
    title = 'Here are your results:'
    command = f'<@baymax> -bd mindtickle-performance-testing-locust -e TC_ID={tc_id},LOCUST_TRACK={track},HISTORICAL_TRACKING={historical_tracking},BASELINE_TEST={baseline_test}'
    trigger_message_to_slack(cluster, message=command)
    return render_template('results.html',
                           the_title=title,
                           the_tc_id=tc_id,
                           the_track=track,
                           the_cluster=cluster,
                           the_historical_tracking=historical_tracking,
                           the_baseline_test=baseline_test,
                           the_command=command.replace('<', '').replace('>', ''), )


@app.route('/')
@app.route('/load_test/trigger')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='Welcome to trigger load test!')


if __name__ == '__main__':
    app.run(debug=True)

# this 'dunder name dunder main' used to make the system understand if its running locally or not
# as all the apps are hosted somewhere in the cloud

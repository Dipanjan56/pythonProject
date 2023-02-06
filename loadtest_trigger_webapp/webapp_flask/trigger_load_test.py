from flask import Flask, render_template, request
from loadtest_trigger_webapp.webapp_flask.slack_report_util import *

app = Flask(__name__)


@app.route('/load_test/trigger_command', methods=['POST'])
def do_trigger() -> 'html':
    """Extract the posted data; perform the load test trigger; return results."""
    tc_id = request.form['tc_id']
    if tc_id == '':
        return '*ERROR: TC_ID can not be null*'

    track = request.form['track']
    cluster = request.form['cluster']
    historical_tracking = request.form['historical_tracking'].lower()
    baseline_test = request.form['baseline_test'].lower()
    reminder_count = request.form['reminder_count']
    interval = request.form['interval']
    start_time = request.form['start_time']
    print(reminder_count, interval, start_time, sep=' -> ')
    title = 'Here are your results:'
    if reminder_count == '':
        command = trigger_message_to_slack(track, cluster, tc_id, historical_tracking, baseline_test)
    else:
        command = trigger_reminder_to_slack(track, cluster, tc_id, historical_tracking, baseline_test,
                                            int(reminder_count), int(interval), start_time)
    return render_template('results.html',
                           the_title=title,
                           the_tc_id=tc_id,
                           the_track=track,
                           the_cluster=cluster,
                           the_historical_tracking=historical_tracking,
                           the_baseline_test=baseline_test,
                           the_reminder_count=reminder_count,
                           the_interval=interval,
                           the_start_time=start_time,
                           the_command=command, )


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

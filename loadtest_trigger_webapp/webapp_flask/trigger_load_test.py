import os
import pathlib

import google
import requests
from flask import Flask, render_template, request, session, redirect, abort
import google.auth.transport.requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol

from loadtest_trigger_webapp.webapp_flask.common.slack_report_util import *

app = Flask(__name__)
app.secret_key = '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'

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # to allow Http traffic for local dev

GOOGLE_CLIENT_ID = '906555373164-oaam7jiudqa6b4v8incdnm1rp0kk3tgg.apps.googleusercontent.com'
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")
print('path: ', client_secrets_file)

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email",
            "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID,
        clock_skew_in_seconds=10
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/load_test/trigger")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route('/')
def index():
    return render_template('login.html', the_title='Welcome to the world of automation!')


@app.route('/load_test/trigger')
@login_is_required
def load_test_entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html', the_title='Welcome to trigger load test!')


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


if __name__ == '__main__':
    app.run(debug=True)

# this 'dunder name dunder main' used to make the system understand if its running locally or not
# as all the apps are hosted somewhere in the cloud

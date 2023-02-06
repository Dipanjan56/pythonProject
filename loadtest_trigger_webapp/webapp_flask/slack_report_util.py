from loadtest_trigger_webapp.webapp_flask.api_requests_http import postCall_without_auth
from common.util_helper import UtilHelper


def trigger_message_to_slack(track, cluster, tc_id, historical_tracking, baseline_test) -> str:
    message = f'<@baymax> -bd mindtickle-performance-testing-locust -e TC_ID={tc_id},LOCUST_TRACK={track},HISTORICAL_TRACKING={historical_tracking},BASELINE_TEST={baseline_test}'
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
    return message.replace('<', '').replace('>', '')


def trigger_reminder_to_slack(track, cluster, tc_id, historical_tracking, baseline_test, reminder_count: int,
                              interval: int, start_time: str) -> str:
    slack_url = f'http://nemesis.internal.{cluster}.mindtickle.com/messenger/slack/send_message'
    # slack_channel = f'track_{cluster}'
    slack_channel = 'test_report_1'
    command = f'<@baymax> -bd mindtickle-performance-testing-locust -e TC_ID={tc_id},LOCUST_TRACK={track},HISTORICAL_TRACKING={historical_tracking},BASELINE_TEST={baseline_test}'
    total_message = '| '
    for i in range(0, reminder_count):
        incremented_time = UtilHelper.increment_datetime(start_time, interval * i)
        date_string = UtilHelper.convert_datetime_into_slack_reminder_dattime(incremented_time)
        message = f"/remind <#{slack_channel}> '{command}' at {date_string}"
        payload = {
            "channel": slack_channel,
            "message": {
                "type": "text",
                "content": message,
                "thread_ts": ""
            }
        }
        resp = postCall_without_auth(slack_url, payload)
        total_message += f'{message} | \n'
    print(
        f'Successfully triggered slack message for load test completion | SLACK_CHANNEL: {slack_channel}')
    return total_message.replace('<', '').replace('>', '')

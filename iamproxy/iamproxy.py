import datetime
import json
import os

from flask import Flask

app = Flask(__name__)

app.logger.info('env: \n%s', os.environ)


def date_to_str(timestamp):
    return timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')


@app.route("/latest/meta-data/iam/security-credentials/")
@app.route("/latest/meta-data/iam/security-credentials/<role_name>")
def role_name(role_name=None):
    app.logger.info('Got request for role: %s', role_name)
    utc_now = datetime.datetime.utcnow()
    thirty_day_expiration = datetime.timedelta(days=30)
    return json.dumps({
        "Code" : "Success",
        "LastUpdated" : date_to_str(utc_now),
        "Type" : "AWS-HMAC",
        "AccessKeyId" : os.environ['AWS_ACCESS_KEY_ID'],
        "SecretAccessKey" : os.environ['AWS_SECRET_ACCESS_KEY'],
        "Token" : None,
        "Expiration" : date_to_str(utc_now + thirty_day_expiration)
    })


if __name__ == "__main__":
    app.run(port=80)

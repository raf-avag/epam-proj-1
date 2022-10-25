class CONFIG:
    TESTING = True
    SECRET_KEY = "123"
    DEBUG = True


class EMAIL:
    link = "smtp.mailtrap.io"
    port = 2525
    api_key = "MAILTRAP_LOGIN"
    secret_key = "MAILTRAP_PASSWORD"


class SLACK:
    secret = "SLACK_CLIENT_SECRET"
    signing = "SLACK_SIGNING_SECRET"
    bot = "SLACK_BOT_SECRET"
    channel = "C0447N114NP"

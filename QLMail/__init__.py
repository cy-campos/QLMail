import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_version():
    return "QLMail version 0.0.6"


class EmailClient:
    @property
    def sender(self):
        return self.__sender

    def set_sender(self, value):
        self.__sender = value

    @property
    def recipient(self):
        return self.__recipient

    def set_recipient(self, value):
        self.__recipient = value

    @property
    def aws_region(self):
        return self.__aws_region

    def set_aws_region(self, value):
        self.__aws_region = value

    @property
    def subject(self):
        return self.__subject

    def set_subject(self, value):
        self.__subject = value

    @property
    def body_text(self):
        return self.__body_text

    def set_body_text(self, value):
        self.__body_text = value

    @property
    def body_html(self):
        return self.__body_html

    def set_body_html(self, value):
        self.__body_html = value

    @property
    def charset(self):
        return self.__charset

    def set_charset(self, value):
        self.__charset = value

    def __init__(self):
        self.__sender = ""
        self.__recipient = ""
        self.__subject = ""
        self.__body_text = ""
        self.__body_html = ""
        self.__aws_region = ""
        self.__charset = ""

    # def __init__(
    #         self,
    #         sender,
    #         recipient,
    #         subject,
    #         body_text,
    #         body_html,
    #         aws_region,
    #         charset
    # ):
    #     self.__sender = sender
    #     self.__recipient = recipient
    #     self.__subject = subject
    #     self.__body_text = body_text
    #     self.__body_html = body_html
    #     self.__aws_region = aws_region
    #     self.__charset = charset

    def send(self):
        # Replace sender@example.com with your "From" address.
        # This address must be verified with Amazon SES.
        SENDER = self.__sender

        # Replace recipient@example.com with a "To" address. If your account
        # is still in the sandbox, this address must be verified.
        RECIPIENT = self.__recipient

        # Specify a configuration set. If you do not want to use a configuration
        # set, comment the following variable, and the
        # ConfigurationSetName=CONFIGURATION_SET argument below.
        # CONFIGURATION_SET = "ConfigSet"

        # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
        AWS_REGION = self.__aws_region

        # The subject line for the email.
        SUBJECT = self.__subject

        # The email body for recipients with non-HTML email clients.
        BODY_TEXT = self.__body_text

        # The HTML body of the email.
        BODY_HTML = self.__body_html

        # The character encoding for the email.
        CHARSET = self.__charset

        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name=AWS_REGION)

        # Try to send the email.
        try:
            logger.info("Attempting to send email\nSender: {0}\nRecipient: {1}\nSubject{2}"
                        .format(self.__sender, self.__recipient, self.__subject))
            # Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
                # If you are not using a configuration set, comment or delete the
                # following line
                # ConfigurationSetName=CONFIGURATION_SET,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            logger.info(e.response['Error']['Message'])
        else:
            logger.info('Email sent! Message ID: {0}'.format(response['MessageId']))

# QLMail v0.0.6

Made with python 3.8

```
pip install QLMail
```

## Scope

An Amazon Web Services (AWS) Lambda Layer Package for sending emails using the AWS Simple Email Service (SES)

The intention of this repo is to be able to add a common SES Email package as a layer to any AWS Lambda function that requires email functionality.

## AWS Lambda Layer Instructions

The basic steps to add this as a layer are to (code examples use command line commands)

1. Create a folder named "python"

```
mkdir python
```

2. Inside the "python" folder, install the QLMail package

```
pip install QLMail -t
```

3. Zip the "python" folder and upload it as an AWS Lambda Layer.

Note: additional steps are most likely needed such as: updating the IAM Policies and attaching them to the layer ARN, and attaching the layer to the Lambda function. I will update these specific steps at a later date.

## Basic Usage for AWS Lambda Python

```python
import QLMail

# Prints the current version QLMail
version = QLMail.get_version()

# Instantiate the QLMail Client
client = QLMail.Client(
    "Bobby Boucher <waterboy@example.com>",     # The Sender Email Address
    "gatorade@example.com",                     # The Recipient Email Address
    "High Quality H2O",                         # The Email Subject
    "Water is good.",                           # The Body Text of the Email
    "<p>Water is good.<p>",                     # The Body Text as HTML of the Email
    "us-east-1",                                # The AWS Region Location to use
    "UTF-8"                                     # The charset of the Email
)

# After the object Client has been instantiated with our required variables, we can send the email
client.send()
```

## Future Enhancements

This repo was created because I could not immediately find any solutions available online that integrate with AWS SES and Lambda. Rather than copy and paste the same email code to every function, it seemed like a better solution to create a Layer that can be reused for all Lambda functions requiring email functionality. Therefore, this project is really just a proof of concept.

If this is developed further, future enhancements may include:

1. Email Queue Implementation so that bulk emails can be sent in batches.
2. Refactoring Method Names
3. Better logging features
4. Anything else that comes to mind

Please feel free to contact me for any comments/suggestions: cy.campos1983@gmail.com

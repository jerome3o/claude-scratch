from pydantic import BaseModel
from learning.tools.common import SchemaTool


class EmailParameters(BaseModel):
    subject: str
    body: str
    to: str


def _send_email(
    parameters: EmailParameters,
):
    msg = (
        f"Sending email to {parameters.to} with subject "
        f"{parameters.subject} and body {parameters.body}"
    )
    print(msg)
    return msg


email_tool = SchemaTool(
    parameters=EmailParameters,
    evaluate=_send_email,
    description='Send an email, with a subject, body, and "to" address',
    name="Send Email",
)

from pydantic import BaseModel


class EmailParameters(BaseModel):
    subject: str
    body: str
    to: str


def _send_email(
    parameters: EmailParameters,
):
    print(
        f"Sending email to {parameters.to} with subject {parameters.subject} and body {parameters.body}"
    )

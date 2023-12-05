import json
from typing import Type
from pydantic import BaseModel

from anthropic import HUMAN_PROMPT, AI_PROMPT


class Tool(BaseModel):
    parameters: Type[BaseModel]


_DEFAULT_TEMPLATE = f"""{HUMAN_PROMPT} \
You are using the {{tool_name}} tool, this is it's description: {{description}}

The response should be in the format:
{{json_schema}}

The situation you are using the tool in is: {{context}}

Please respond directly in JSON format

{AI_PROMPT} {{{{\
"""


def build_pydantic_tool_prompt(
    tool_name: str,
    description: str,
    response_model: BaseModel,
    context: str,
    template: str = None,
) -> str:
    template = template or _DEFAULT_TEMPLATE
    json_schema = json.dumps(response_model.model_json_schema(), indent=2)

    return _DEFAULT_TEMPLATE.format(
        tool_name=tool_name,
        description=description,
        json_schema=json_schema,
        context=context,
    )

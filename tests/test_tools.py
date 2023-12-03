from pydantic import BaseModel
from learning.tools.common import build_pydantic_tool_prompt


def test_build_pydantic_tool_prompt_happy_path():
    class TestResponseModel(BaseModel):
        test_field: str

    tool_name = "test_tool"
    description = "test description"
    context = "test context"
    response_model = TestResponseModel
    template = "test template, {tool_name}, {description}, {context}, {json_schema}"

    expected = (
        "test template, test_tool, test description, test context, "
        '{\n  "title": "TestResponseModel",\n  "type": "object",\n  "properties": {\n    '
        '"test_field": {\n      "title": "Test Field",\n      "type": "string"\n    }\n  }\n}'
    )

    actual = build_pydantic_tool_prompt(
        tool_name=tool_name,
        description=description,
        response_model=response_model,
        context=context,
        template=template,
    )

    assert actual == expected

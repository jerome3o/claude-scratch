from langchain.chat_models import ChatAnthropic
from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "Tell me a joke about frogs"),
    ]
)


def main():
    model = ChatAnthropic()
    print(model(prompt.format_messages()))


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT


def main():
    # env var ANTHROPIC_API_KEY used
    anthropic = Anthropic()

    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=300,
        prompt=f"{HUMAN_PROMPT} how does a court case get to the Supreme Court?{AI_PROMPT}",
    )

    print(completion.completion)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()

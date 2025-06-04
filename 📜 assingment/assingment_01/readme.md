# LLM Example Codes – Assignment

Welcome! This repository provides simple, well-organized example code for various LLM-related topics as part of your assignment.

---

## Table of Contents

- [Topics](#topics)
- [How to Run](#how-to-run)
- [Notes](#notes)

---

## Topics

- **00_swarm**  
    Introduction to swarm intelligence concepts (theoretical overview, no code).

- **01_uv**  
    Minimal example of an HTTP server using [`uv`](https://pypi.org/project/uv/).

- **02_openrouter**  
    Example of sending a chat completion request to OpenRouter.

- **03_litellm_openai_agent**  
    Example using [LiteLLM](https://github.com/BerriAI/litellm) to call an OpenAI agent.

---

## How to Run

1. **Install dependencies:**
        ```bash
        pip install uv requests litellm
        ```

2. **Run the examples:**
        ```bash
        python 01_uv/uv_example.py
        python 02_openrouter/openrouter_example.py
        python 03_litellm_openai_agent/litellm_example.py
        ```

---

## Notes

- Replace `<YOUR_API_KEY>` with your actual API keys for OpenRouter and OpenAI.
- Store your API keys securely (e.g., in environment variables or a configuration file) as required by the examples.
- For more details, refer to the comments within each example script.

---

Happy coding!

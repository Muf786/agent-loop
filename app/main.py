import requests
from agents import PLANNER_PROMPT, DEV_PROMPT

OLLAMA_URL = "http://host.docker.internal:11434/api/chat"


def run_agent(messages, model):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "messages": messages,
            "stream": False
        },
        timeout=120
    )
    response.raise_for_status()
    return response.json()["message"]["content"]


def main():
    planner = [{"role": "system", "content": PLANNER_PROMPT}]
    dev = [{"role": "system", "content": DEV_PROMPT}]

    goal = "Build a simple habit tracking mobile app"
    planner.append({"role": "user", "content": goal})

    for turn in range(5):
        print(f\"\\n--- TURN {turn + 1} ---\")

        plan = run_agent(planner, model="llama3.1:8b")
        planner.append({"role": "assistant", "content": plan})
        print("PLANNER:\\n", plan)

        dev.append({"role": "user", "content": plan})
        dev_reply = run_agent(dev, model="codellama:7b")
        dev.append({"role": "assistant", "content": dev_reply})
        print("DEV:\\n", dev_reply)

        planner.append({"role": "user", "content": dev_reply})


if __name__ == "__main__":
    main()

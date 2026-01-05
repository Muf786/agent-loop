# Multi-Agent App Builder (Free)

## Requirements
- macOS (Apple Silicon recommended)
- Docker
- Ollama

## Setup

1. Install Ollama
   ```bash
   brew install ollama
   ollama serve
   ```

2. Download models

   ```bash
   ollama run llama3.1:8b
   ollama run codellama:7b
   ```

3. Build and run

   ```bash
   docker compose up --build
   ```

## Notes

* Ollama runs on macOS
* Docker container connects via host.docker.internal
* No API keys required

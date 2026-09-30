# MCP Travel Agent

An AI-powered travel assistant built with **Python, FastAPI, Groq, and Playwright MCP**.

The application uses Playwright MCP to interact with websites through a headless browser and Groq to generate natural-language responses from the browser results.

## 🚀 Features

- AI-powered travel assistance
- Natural-language interaction
- Browser automation using Playwright MCP
- Google search through browser automation
- Website navigation
- Headless browser execution
- Groq-powered response generation
- FastAPI REST API
- Health-check endpoint
- Dockerized deployment
- Ready for cloud deployment on Render

## 🏗️ Architecture

```text
                User
                  │
                  ▼
            FastAPI API
                  │
                  ▼
             Agent Layer
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
   Playwright MCP         Groq LLM
        │                   │
        ▼                   │
   Web Browser              │
        │                   │
        └─────────┬─────────┘
                  ▼
           Natural Response
                  │
                  ▼
                User
🛠️ Tech Stack
Technology	Purpose
Python	Application development
FastAPI	REST API backend
Playwright MCP	Browser automation
Groq	LLM-powered response generation
LangChain Groq	Groq integration
MCP Use	MCP client integration
Node.js / npm	Playwright MCP runtime
Docker	Containerization
Render	Cloud deployment
📁 Project Structure
mcp-travel-agent/
│
├── app.py
├── agent.py
├── main.py
├── playwright_mcp.json
├── browser_mcp.json
├── requirements.txt
├── pyproject.toml
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
└── uv.lock
⚙️ How It Works
The user sends a travel-related request through the FastAPI API.
The agent determines the required browser action.
Playwright MCP launches a headless browser.
The browser navigates to the requested website or search page.
Browser results are returned to the application.
Groq processes the browser output.
The LLM generates a natural-language response.
FastAPI returns the response to the user.
🔑 Environment Variables

Create a .env file locally:

GROQ_API_KEY=your_groq_api_key

Never commit .env to GitHub.

💻 Local Setup
1. Clone the repository
git clone https://github.com/Gautam-Dash/mcp-travel-agent.git
cd mcp-travel-agent
2. Create a virtual environment

Using uv:

uv venv

Activate it on Windows:

.venv\Scripts\activate
3. Install dependencies
uv pip install -r requirements.txt
4. Configure environment variables

Create .env:

GROQ_API_KEY=your_groq_api_key
5. Start the application
uv run uvicorn app:app --reload

The API will be available at:

http://127.0.0.1:8000
📡 API Endpoints
GET /

Returns the application status.

Example response:

{
  "status": "online",
  "service": "MCP Travel Agent"
}
GET /health

Health-check endpoint used by deployment platforms.

Example response:

{
  "status": "healthy"
}
POST /chat

Send a message to the AI travel agent.

Request:

{
  "message": "Open Google and search best places to visit in Dubai"
}

Response:

{
  "response": "..."
}
POST /clear

Clears the current agent state.

🐳 Docker

The application includes a Dockerfile containing:

Python runtime
Node.js
npm
uv
Application dependencies
Playwright MCP runtime

Build the Docker image:

docker build -t mcp-travel-agent .

Run the container:

docker run -p 8000:8000 \
  -e GROQ_API_KEY=your_groq_api_key \
  mcp-travel-agent
☁️ Deployment

The application is designed for deployment on Render using Docker.

Deployment flow:

GitHub
   │
   ▼
Render
   │
   ▼
Docker Build
   │
   ├── Python
   ├── Node.js
   ├── npm
   └── Playwright MCP
   │
   ▼
FastAPI
   │
   ▼
Public API
Render Configuration

Use:

Runtime: Docker
Branch: main
Health Check Path: /health

Add the following environment variable:

GROQ_API_KEY

The application listens on the port provided by the PORT environment variable.

🔐 Security
API keys are stored using environment variables.
.env is excluded from Git.
Secrets should never be committed to the repository.
Production deployments should use secure environment-variable management.
🎯 Example Queries
Open Google

Open Google and search best places to visit in Dubai

Open wikipedia.org

Open github.com

Search for things to do in Bangalore
🔮 Future Improvements
Extract and summarize actual search results
Support multiple travel websites
Add hotel and flight research
Add itinerary generation
Add price comparison
Add persistent conversation memory
Add authentication
Add frontend interface
Add streaming responses
Improve browser error handling
Add automated tests
Add observability and logging
👨‍💻 Author

Gautam Dash

AI / Backend Developer

GitHub:
https://github.com/Gautam-Dash

⭐ If you find this project useful, consider giving the repository a star.


### One important cleanup

Your GitHub screenshot shows both:

```text
browser_mcp.json
playwright_mcp.json

Since we're now using only playwright_mcp.json, I'd remove browser_mcp.json if it isn't used anywhere.

Also, main.py and test_playwright.py can stay if they're useful, but the README should describe the actual production entry point as app.py.

After updating README:

git add .
git commit -m "Add project documentation"
git push

That will give the GitHub repository a much more polished, recruiter-friendly presentation.

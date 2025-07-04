NeuroNet Ai Agent

An intelligent chat-based agent powered by LLaMA3 and LangChain that can search the web, evaluate math,and assist with diverse queries.NeuroNet integrates web tools and natural language reasoning into a minimalist Streamlit interface — making it both powerful and easy to use.

## Problem Statement
In an era of information overload,there's a need for agents that can think,retrieve accurate content from the web, solve queries, and communicate in a human-like manner.NeuroNet bridges this gap with Groq's ultra-fast LLaMA3-8B model and LangChain’s tool-calling capabilities.

##Key Features
✅ Uses LLaMA3-8B via Groq API for blazing-fast responses
✅ Web search and webpage summarization using DuckDuckGo + scraping
✅ Math problem evaluation
✅ Tool-calling with LangChain's convert_to_openai_tool
✅ Streamlit chat UI with smooth animations and history tracking
✅ New chat (reset) functionality
✅ Typewriter-style response effect

##Tech Stack
| Component           | Tool/Library                           |
| ------------------- | -------------------------------------- |
| Language            | Python 3.9+                            |
| LLM Engine          | [Groq LLaMA3-8B](https://groq.com)     |
| Framework           | [LangChain](https://www.langchain.com) |
| UI                  | [Streamlit](https://streamlit.io)      |
| Web Extraction Tool | `requests`,`markdownify`              |
| Search Tool         | `duckduckgo-search`                    |
| Session & Secrets   | `python-dotenv`                        |
| Package Mgmt        | `pip`,`requirements.txt`              |
| Version Control     | Git,GitHub                            |

##How To Run

1. Clone the Repository
git clone https://github.com/Sonushaji2002/AI-Chatbot
cd neuronet-agent
2. Install Dependencies
pip install -r requirement.txt
3. Set Your API Key
Create a .env file and add your Groq API key:
GROQ_API_KEY=your_groq_api_key
4. Launch the App
streamlit run App.py

##Overview & Usage

Once launched, you can:
Ask general knowledge questions
Perform math calculations
Ask it to summarize a URL or recent event
Clear chat history with one click

##Folder Structure
 
neuronet-agent/
├── web.py               # Streamlit frontend to run the app 

├── NN.py                # Main LangChain agent logic 

├── prop/
│   └── visit_web.py     # Custom tools or chains for web interaction and math logic

├── requirement.txt      # Python dependencies for the project

├── .env                 # API keys and environment variables (user-created,not version-controlled)


##Potential Upgrades
 
Add long-term memory using LangGraph or Vector DB
PDF/document reading tool
Docker container setup
Deploy on Streamlit Cloud or Hugging Face Spaces
Admin analytics dashboard






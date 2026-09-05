# 🦚 PEACOCK AI — Multi-AI Chatbot Web Application

> **"15 Colors. 15 AI Powers. One Intelligent Assistant."**  
> *One interface. Multiple AI minds.*

---

## 1. Project Concept & Architecture

PEACOCK AI is a commercial-grade, multi-model AI chatbot platform designed as a college project. The core concept connects the 15 prominent colors of peacock plumage to 15 specialized AI tools and models:

```
Peacock → 15 prominent colors → PEACOCK AI → 15 AI tools/models
```

---

## 2. 15 Color-Coded AI Models Matrix

| # | Model Name | Provider | Color Accent | Hex Token | Specialty |
|---|------------|----------|--------------|-----------|-----------|
| 01 | **Peacock Ultra** | PEACOCK Core | Peacock Blue | `#0F4C81` | Master Orchestrator & General AI |
| 02 | **GPT-4o Mind** | OpenAI | Royal Blue | `#1E40AF` | Advanced Multi-Modal & Deep Reasoning |
| 03 | **Claude 3.5 Sonnet** | Anthropic | Cyan | `#06B6D4` | Creative Code & System Architecture |
| 04 | **Gemini 1.5 Flash** | Google DeepMind | Turquoise | `#14B8A6` | Ultra-Fast 1M+ Context Window |
| 05 | **DeepSeek R1/V3** | DeepSeek AI | Teal | `#0D9488` | Math proofs, Science & Logic |
| 06 | **Llama 3.3 70B** | Meta AI | Emerald | `#10B981` | Open Source Powerhouse |
| 07 | **Mistral Large** | Mistral AI | Green | `#22C55E` | European Multilingual Specialist |
| 08 | **Qwen 2.5 Max** | Alibaba Cloud | Lime | `#84CC16` | Data Analysis & Asian Languages |
| 09 | **Command R+** | Cohere | Gold | `#EAB308` | Enterprise RAG Document Retrieval |
| 10 | **Perplexity Sonar** | Perplexity AI | Yellow | `#FACC15` | Real-Time Live Web Search & Citations |
| 11 | **Grok 2 Vision** | xAI | Orange | `#F97316` | Real-Time Insight & Vision |
| 12 | **Phind Code Pro** | Phind | Coral | `#FF6B6B` | Full-Stack Developer & Debugger |
| 13 | **Together Vision** | Together AI | Pink | `#EC4899` | Spatial & Architecture Diagram Analyst |
| 14 | **Fireworks Stream** | Fireworks AI | Purple | `#A855F7` | Ultra Low Latency Token Streamer |
| 15 | **Peacock Demo AI** | Local Engine | Indigo | `#6366F1` | Built-in Offline Fallback AI Engine |

---

## 3. Technology Stack

- **Backend**: Python 3.14, FastAPI, Async SQLAlchemy, SQLite (`peacock_ai.db`), Pydantic v2, PyPDF, python-docx, openpyxl, JWT Auth (`python-jose`, `bcrypt`).
- **Frontend**: HTML5, Modern CSS3 (Variables, Glassmorphism, 15 Color Tokens), Vanilla JavaScript (Modular ES6), Canvas Particles API, Web Speech API (Voice Input).
- **Streaming**: Server-Sent Events (SSE) progressive token rendering.

---

## 4. How to Run PEACOCK AI

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run application server
python run.py
```

Then open your browser and navigate to:  
👉 **`http://127.0.0.1:8000`**

---

## 5. Running Automated Tests

```bash
python -m pytest tests/test_peacock.py
```

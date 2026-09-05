import uvicorn
import sys
import os

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    
    print("=" * 60)
    print(" PEACOCK AI -- Multi-AI Chatbot Platform")
    print(" 15 Colors. 15 AI Powers. One Intelligent Assistant.")
    print("=" * 60)
    print(" Server starting on: http://127.0.0.1:8000")
    print("=" * 60)
    
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)

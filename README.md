# Travel Guide Chatbot for the Philippines

## Overview
This chatbot is a specialized AI assistant designed to help users plan their trips to the Philippines. 
It provides detailed and thoughtful travel recommendations tailored to user preferences while also 
considering weather conditions to ensure safety and enjoyment. The chatbot is built using Streamlit, 
providing a simple and interactive web-based interface for users to access its features. 
Prompt engineering is employed to enhance the interaction experience, ensuring that the responses are 
relevant, clear, and helpful.

## Features

- **Personalized Travel Recommendations**: Suggests destinations, activities, and tips based on user input and preferences.
- **Weather-Aware Suggestions**: Considers current weather conditions to provide safe and practical travel advice.
- **Interactive Guidance**: Engages users to clarify vague queries or locations for better assistance.
- **Philippines-Focused Expertise**: Exclusively provides travel advice for the Philippines, ensuring depth and accuracy in its recommendations.
- **Chain-of-Thought Reasoning**: Breaks down user queries logically to deliver clear and structured responses.

## Future Enhancements

- Weather-Aware Travel Planning: Integrate real-time weather forecasts for the user's desired travel destinations to provide dynamic and up-to-date recommendations.
- Retrieval-Augmented Generation (RAG) Integration: Implement RAG to enhance the chatbot's responses by retrieving accurate and contextually relevant information from external sources, ensuring recommendations are comprehensive and reliable.
- Comprehensive Daily Weather Updates: Implement a feature to fetch daily weather forecasts for all cities and provinces in the Philippines, offering users a holistic view of travel conditions nationwide.

## Setup

Install Dependencies
```bash
pip install -e .
```

Create streamlit secrets
```bash
touch .streamlit/secrets.toml
```

Add OpenAI API Key inside `secrets.toml`
```toml
OPENAI_API_KEY = "your-api-key-here"
```

Run the application
```bash
streamlit run src/streamlit_app/app.py
```
import streamlit as st

from streamlit_app.chatclient import OpenAIChatClient
from prompts import travel_guide

class ChatBot:
    def __init__(
            self, 
            api_key = st.secrets["OPENAI_API_KEY"],
            model_name = "gpt-3.5-turbo",
            system_prompt = None
        ) -> None:
        self.client = OpenAIChatClient(
            api_key=api_key, 
            model_name=model_name,
            system_prompt=system_prompt
            )

    def render_messages(self):
        for message in self.client.message_manager.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"]) 

    def run(self):

        st.title("Chatbot")
        self.render_messages()

        if query := st.chat_input("What is up?"):
            with st.chat_message("user"):
                st.markdown(query)
            with st.chat_message("assistant"):
                chat_response = self.client.generate_completion(query)

                response = st.write_stream(chat_response)
                self.client.message_manager.add_message("assistant", response)


if __name__ == "__main__":
    app = ChatBot(system_prompt=travel_guide.prompt)
    app.run()
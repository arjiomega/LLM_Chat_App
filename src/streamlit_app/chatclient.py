from openai import OpenAI
import streamlit as st

class MessageManager:
    def __init__(self) -> None:
        pass

    @property
    def messages(self):
        if "messages" not in st.session_state:
            st.session_state["messages"] = []
        return st.session_state["messages"]

    @messages.setter
    def messages(self, messages):
        st.session_state["messages"] = messages

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def load_message_history(self, system_prompt:str=None):
        if system_prompt:
            return [
                {"role":"system", "content": system_prompt}
            ] + [
                {"role": m["role"], "content": m["content"]}
                for m in self.messages
            ]
        else:
            return [
                {"role": m["role"], "content": m["content"]}
                for m in self.messages
            ]

class OpenAIChatClient:
    def __init__(self, api_key, system_prompt=None, model_name="gpt-3.5-turbo") -> None:
        self.client = OpenAI(api_key=api_key)
        self.model_name = model_name
        self.message_manager = MessageManager()
        self.system_prompt = system_prompt

    def generate_completion(self, query, stream=True):

        self.message_manager.add_message("user", query)

        chat_history = (self.message_manager.load_message_history(
                system_prompt=self.system_prompt
            ))

        for message in chat_history:
            print(message['role'])
            print(message['content'])
            print("\n-----------------------------------------------\n")

        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.message_manager.load_message_history(
                system_prompt=self.system_prompt
            ),
            stream=stream
        )

        return completion if stream else completion.choices[0].message.content

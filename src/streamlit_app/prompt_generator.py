import requests
from bs4 import BeautifulSoup

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from prompts import extract_location

def scrape_content():
    url = 'https://guidetothephilippines.ph/articles/ultimate-guides/travel-guide-philippines'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        knowledge_base = []

        section_divs = soup.select('div.x-z6uofh.e1q7jrc70')

        for index, div in enumerate(section_divs[0]):
            content = div.get_text(strip=True)
            if content:
                knowledge_base.append({"title": f"Section {index+1}", "content": content})

        vectorizer = TfidfVectorizer().fit([doc['content'] for doc in knowledge_base])

        return vectorizer

def prompt_generator(query: str, vectorizer, top_n = 10):
    query_vec = vectorizer.transform([query])
    doc_vectors = vectorizer.transform([doc['content'] for doc in knowledge_base])
    similarities = cosine_similarity(query_vec, doc_vectors).flatten()
    relevant_docs = [knowledge_base[idx] for idx in similarities.argsort()[::-1] if similarities[idx] > 0.5]

    selected_content = "\n\n".join([ex['content'] for ex in relevant_docs])

    return selected_content

class KnowledgeBase:
    def __init__(self) -> None:
        pass

class PromptGenerator:
    def __init__(self) -> None:
        pass

    def generate(self, prompt_template, message_history):
        return {}

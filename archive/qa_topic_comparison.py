import ollama 
import numpy as np 
import requests
import json
from lite_llm import LiteLLMService, LiteLLMSetting, LiteLLMEmbeddingInput
from pydantic import HttpUrl, SecretStr
import time 
from tqdm import tqdm

litellm = LiteLLMService(
        litellm_setting=LiteLLMSetting(
            url=HttpUrl("http://localhost:9510"),
            token=SecretStr("abc123"),
            model="gemini-2.5-flash",
            frequency_penalty=0.0,
            n=1,
            temperature=0.0,
            top_p=1.0,
            max_completion_tokens=10000,
            dimension=1024,
            embedding_model="qwen3-embedding:0.6b",
        )
    )
    

def cosine_similarity(vector_1: list[float], vector_2: list[float]) -> float:
    vector_numpy_1 = np.array(vector_1)
    vector_numpy_2 = np.array(vector_2)
    dot_product = np.dot(vector_numpy_1, vector_numpy_2)
    norm_1 = np.linalg.norm(vector_numpy_1)
    norm_2 = np.linalg.norm(vector_numpy_2)
    return dot_product / (norm_1 * norm_2)

def embed_ollama(text: str) -> list[float]:
    return ollama.embed(model="qwen3-embedding:0.6b", input=text)['embeddings'][0]

def embed_gemini(text: str) -> list[float]:
    return litellm.embedding_llm(
        inputs=LiteLLMEmbeddingInput(
            text=text
        )
    ).embedding
    

course_code = "int3405"
sim_q = []
sim_a = []
for week_number in range(1, 9): 
    with open(f'/home/lehoangvu/KLTN/outputs/gpt-4o-mini/{course_code}/week{week_number}_pipeline.json', 'r') as f:
        data = json.load(f)
        
    questions = data['questions']
    for question in questions:
        try:
            embed_desc = embed_ollama(question['topic']['description'])
            q_consine = cosine_similarity(embed_ollama(question['question']), embed_desc)
            sim_q.append(q_consine)
            a_consine = cosine_similarity(embed_ollama(question['answer']), embed_desc)
            sim_a.append(a_consine)
        except Exception as e:
            print(f"Error processing question: {e}")
            
        
mean_sim_q = np.mean(sim_q)
print(f"Mean Question Similarity over Course: {mean_sim_q}")
std_sim_q = np.std(sim_q)
print(f"STD Question Similarity over Course: {std_sim_q}")
mean_sim_a = np.mean(sim_a)
print(f"Mean Answer Similarity over Course: {mean_sim_a}")
std_sim_a = np.std(sim_a)
print(f"STD Answer Similarity over Course: {std_sim_a}")

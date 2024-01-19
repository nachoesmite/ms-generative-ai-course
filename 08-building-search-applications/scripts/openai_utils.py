import numpy as np
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_embedding(openai_client, text, model="text-embedding-ada-002"): # model = "deployment_name"
    return openai_client.embeddings.create(input = [text], model=model).data[0].embedding
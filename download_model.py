from sentence_transformers import SentenceTransformer

# This will download the model from Hugging Face
model = SentenceTransformer('all-MiniLM-L6-v2')

# Save it locally to a folder named 'all-MiniLM-L6-v2-local'
model.save('./project/models/all-MiniLM-L6-v2-local')

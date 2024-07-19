import os
from embedchain import App

# Set your Hugging Face token
os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "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"

config = {
  'llm': {
    'provider': 'huggingface',
    'config': {
      'model': 'mistralai/Mistral-7B-Instruct-v0.3',
      'top_p': 0.5
    }
  },
  'embedder': {
    'provider': 'huggingface',
    'config': {
      'model': 'sentence-transformers/all-mpnet-base-v2'
    }
  }
}

# Create a new app instance with the desired config
app = App.from_config(config=config)

# Clear the existing database (if any)
app.db.reset()

# Add your documents
app.add("https://www.forbes.com/profile/elon-musk")
app.add("https://en.wikipedia.org/wiki/Elon_Musk")

# Now you can query
response = app.query("What is the net worth of Elon Musk today?")
print(response)
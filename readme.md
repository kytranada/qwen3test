# Qwen3-Coder Benchmark

A simple benchmarking tool for comparing Qwen3-Coder models (`qwen3-coder:30b` and `qwen3-coder:30b-a3b-q8_0`).

This tool allows you to benchmark different quantized and full precision versions of the Qwen3-Coder model to compare their performance characteristics including:
- Response time
- Token count
- Memory usage
- CPU utilization

## How to Run

1. Ensure Ollama is running with the Qwen3-Coder models installed
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`
4. Select a prompt and model in the sidebar
5. Click "Run selected model" to start

## Adding New Models

To add new models for testing:

1. **Ensure the model is available in Ollama**:
   - Pull the model using: `ollama pull <model-name>`
   - Verify it's installed with: `ollama list`

2. **Update the model selection in the app**:
   - Modify the `model_choice` radio button options in `app.py`
   - Add the new model name to the conditional logic for handling responses

3. **Add model-specific handling (if needed)**:
   - If your model requires special parameters or response processing, update the `query_model` function in `ollama_client.py`

4. **Test the new model**:
   - Run the app and select your new model
   - Verify it runs correctly and displays results

## Model Template

Here's a template you can use to add new models:

```python
# In app.py, add to the model_choice radio button options:
# "qwen3-coder:30b-a3b-q8_0", "qwen3-coder:30b", "your-new-model-name"

# In ollama_client.py, you can add special handling for your model if needed:
# if model_name == "your-new-model-name":
#     # Add custom parameters
```
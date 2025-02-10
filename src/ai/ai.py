import json
from jsonschema import validate
import ollama

def generate_structured_response(prompt_input):
    # Schema validation structure - defines the expected JSON structure with color and reason fields
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "color": {
                    "type": "string",
                    "description": "Human readable color name"
                },
                "reason": {
                    "type": "string",
                    "description": "Explanation for the color choice"
                }
            },
            "required": ["color", "reason"]
        }
    }

    # Formats the user prompt with the schema to ensure structured JSON response
    formatted_prompt = f"""{prompt_input}
    Respond strictly with a JSON as per given schema below.
    {json.dumps(schema, indent=2)}
    """
    print(formatted_prompt)
    print("---------------------------------")
    try:
        # Uses Ollama API to generate response with qwen2.5-coder model
        response = ollama.generate(model="qwen2.5-coder", prompt=formatted_prompt, options={"temperature": 0.7}, format=schema)
        
        # Parses and validates the JSON response against the schema
        llm_response = json.loads(response["response"].strip())
        validate(instance=llm_response, schema=schema)
        
        return llm_response
        
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON response from LLM")
    except Exception as e:
        raise RuntimeError(f"Error processing response: {str(e)}")


def generate_content(topic, word_count, additional_details):
    formatted_prompt = f"""
    Generate a detailed essay on {topic} with {word_count} words. 
    Use the following additional details: {additional_details}
    """
    response = ollama.generate(model="qwen2.5-coder", prompt=formatted_prompt)
    # print(response.response)
    return response.response
# Example usage showing how to get structured color information about the sky
# if __name__ == "__main__":
#     try:
#         result = generate_structured_response("During different times, what colors is the sky and why?")
#         print("Valid structured response:")
#         print(result)
#     except Exception as e:
#         print(f"Error: {str(e)}")
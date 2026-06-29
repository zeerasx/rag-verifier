from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer
)

import torch

class Generator:

    def __init__(self,model_name="Qwen/Qwen2.5-3B-Instruct"):

        self.tokenizer = (AutoTokenizer.from_pretrained(model_name))

        self.model = (
            AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype="auto",
                device_map="auto"
            )
        )

    def generate(self,prompt,max_new_tokens=128):
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        text = (
            self.tokenizer
            .apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
        )

        inputs = self.tokenizer(text,return_tensors="pt")
        outputs = self.model.generate(**inputs,max_new_tokens=max_new_tokens)

        response = self.tokenizer.decode(outputs[0],skip_special_tokens=True)

        return response
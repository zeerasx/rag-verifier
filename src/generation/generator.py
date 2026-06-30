from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig
)

import torch

class Generator:

    def __init__(self,model_name="Qwen/Qwen2.5-0.5B-Instruct"):

        self.tokenizer = (AutoTokenizer.from_pretrained(model_name))

        # Define quantization config
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,              # enable 4-bit quantization
            bnb_4bit_use_double_quant=True, # improves compression
            bnb_4bit_quant_type="nf4",      # recommended quantization type
            bnb_4bit_compute_dtype=torch.float16  # compute in half precision
        )

        self.model = (
            AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype="auto",
                device_map="auto",
                quantization_config=quant_config
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
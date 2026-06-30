### Model Selection

Qwen2.5-0.5B-Instruct

Reasons:

- Qwen's are relatively new and instruction tune
- More capable than older tiny models
- CPU Friendly - with Quantization
- 
#### Optimization for CPU-only hardware

- Initial plan was to use Qwen2.5-1.5B-Instruct or Qwen2.5-3B-Instruct
- However, to avoid CPU offloading:
    -  Switched model from Qwen2.5-3B-Instruct to Qwen2.5-0.5B-Instruct 
    -  Enabled 4-bit quantization for Qwen2.5-0.5B-Instruct
- Hence reducing latency and memory usage (RAM footprint reduction).
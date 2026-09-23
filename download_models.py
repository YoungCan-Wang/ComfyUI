import os
from huggingface_hub import hf_hub_download

repo_id = "abenzerps/Qwen-Image-2.1-GGUF"
base_dir = os.path.abspath(os.path.dirname(__file__))

downloads = [
    {
        "filename": "qwen-image-2.1-Q4_K_M.gguf",
        "local_dir": os.path.join(base_dir, "models", "diffusion_models"),
        "expected_path": os.path.join(base_dir, "models", "diffusion_models", "qwen-image-2.1-Q4_K_M.gguf"),
    },
    {
        "filename": "text_encoders/qwen3vl_8b_int8_convrot.safetensors",
        "local_dir": os.path.join(base_dir, "models"),
        "expected_path": os.path.join(base_dir, "models", "text_encoders", "qwen3vl_8b_int8_convrot.safetensors"),
    },
    {
        "filename": "vae/qwen_image_2.1_vae_bf16.safetensors",
        "local_dir": os.path.join(base_dir, "models"),
        "expected_path": os.path.join(base_dir, "models", "vae", "qwen_image_2.1_vae_bf16.safetensors"),
    }
]

print("=== Starting Qwen-Image-2.1-GGUF Model Download ===")
for item in downloads:
    target = item["expected_path"]
    if os.path.exists(target) and os.path.getsize(target) > 1024 * 1024:
        print(f"[Skipping] {target} already exists (size: {os.path.getsize(target) / 1024 / 1024:.1f} MB).")
        continue

    print(f"\n[Downloading] {item['filename']} -> {item['local_dir']}...")
    hf_hub_download(
        repo_id=repo_id,
        filename=item["filename"],
        local_dir=item["local_dir"],
    )
    print(f"[Done] {item['filename']} downloaded successfully.")

print("\n=== All model components have been downloaded successfully! ===")

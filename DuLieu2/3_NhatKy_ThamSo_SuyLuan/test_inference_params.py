"""
Script thử nghiệm & kiểm tra các tham số suy luận (inference parameters):
- temperature
- top_k
- top_p
- repetition_penalty
"""
import json
import os
from pathlib import Path

# Nạp bảng tham số suy luận
CONFIG_PATH = Path(__file__).parent / "inference_config_benchmarks.json"

def load_inference_configs():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def test_inference_parameters():
    configs = load_inference_configs()
    print("=== VIETVOICE AI INFERENCE PARAMETER TEST BENCHMARK ===")
    print(f"Loaded {len(configs.get('emotion_configs', {}))} emotion configurations.\n")

    for emotion, params in configs.get("emotion_configs", {}).items():
        print(f"[*] Emotion: {emotion.upper()}")
        print(f"    - Temperature       : {params.get('temperature')}")
        print(f"    - Top K             : {params.get('top_k')}")
        print(f"    - Top P (Nucleus)   : {params.get('top_p')}")
        print(f"    - Repetition Penalty: {params.get('repetition_penalty')}")
        print(f"    - Speed             : {params.get('speed')}x")
        print(f"    - Description       : {params.get('description')}\n")

if __name__ == "__main__":
    test_inference_parameters()

import gradio as gr
import requests
import time

def generate_video(api_key, prompt, duration, aspect_ratio):
    if not api_key:
        return None, "Please enter your NexaAPI key from nexa-api.com (free, no credit card)"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "kling-v3-pro",
        "prompt": prompt,
        "duration": int(duration),
        "aspect_ratio": aspect_ratio
    }
    
    try:
        resp = requests.post(
            "https://nexa-api.com/api/v1/video/generate",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if resp.status_code != 200:
            return None, f"Error: {resp.status_code} — {resp.text[:200]}"
        
        data = resp.json()
        job_id = data.get("job_id")
        
        for _ in range(60):
            time.sleep(5)
            status_resp = requests.get(
                f"https://nexa-api.com/api/v1/video/status/{job_id}",
                headers=headers,
                timeout=10
            )
            status_data = status_resp.json()
            if status_data.get("status") == "completed":
                return status_data.get("video_url"), "✅ Video generated! (Sora alternative via NexaAPI)"
            elif status_data.get("status") == "failed":
                return None, f"Generation failed: {status_data.get('error')}"
        
        return None, "Timeout — job still processing"
    except Exception as e:
        return None, f"Error: {str(e)}"

with gr.Blocks(title="Sora Alternative — NexaAPI Video Generator") as demo:
    gr.Markdown("""
    # 🎬 Sora Alternative — AI Video Generator via NexaAPI
    
    **Sora shut down on March 24, 2026.** This demo shows how to use NexaAPI as the best alternative.
    
    - ✅ Same Kling V3 Pro quality
    - ✅ 3x cheaper than fal.ai
    - ✅ Free tier — no credit card required
    
    Get your free API key at **[nexa-api.com](https://nexa-api.com)**
    
    Also available on [RapidAPI](https://rapidapi.com/user/nexaquency) | 
    [pip install nexaapi](https://pypi.org/project/nexaapi/) | 
    [npm install nexaapi](https://www.npmjs.com/package/nexaapi)
    """)
    
    with gr.Row():
        with gr.Column():
            api_key = gr.Textbox(label="NexaAPI Key (free at nexa-api.com)", type="password", placeholder="Get free key at nexa-api.com")
            prompt = gr.Textbox(label="Video Prompt", placeholder="A cinematic shot of...", lines=3)
            duration = gr.Slider(minimum=3, maximum=10, value=5, step=1, label="Duration (seconds)")
            aspect_ratio = gr.Dropdown(["16:9", "9:16", "1:1"], value="16:9", label="Aspect Ratio")
            generate_btn = gr.Button("🎬 Generate Video (Sora Alternative)", variant="primary")
        
        with gr.Column():
            video_output = gr.Video(label="Generated Video")
            status_output = gr.Textbox(label="Status")
    
    generate_btn.click(
        fn=generate_video,
        inputs=[api_key, prompt, duration, aspect_ratio],
        outputs=[video_output, status_output]
    )

if __name__ == "__main__":
    demo.launch()

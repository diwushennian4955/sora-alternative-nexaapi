"""
Sora Shutdown Migration Guide — Switch to NexaAPI
Sora was shut down on March 24, 2026. Use this script to migrate.

Get your free API key at: https://nexa-api.com
pip install nexaapi  # https://pypi.org/project/nexaapi/
"""

from nexaapi import NexaAPI

# Initialize client — get free API key at https://nexa-api.com
client = NexaAPI(api_key='YOUR_FREE_API_KEY')


def generate_video_kling(prompt: str, duration: int = 5) -> str:
    """
    Best Sora replacement: Kling 3.0 Pro
    - $0.0333/second (3x cheaper than Sora was)
    - Native audio support
    - Multi-shot cinematic control
    """
    response = client.video.generate(
        model='kling-3.0-pro',
        prompt=prompt,
        duration=duration,
        aspect_ratio='16:9'
    )
    return response.video_url


def generate_video_sora2(prompt: str, duration: int = 5) -> str:
    """
    Sora 2 via NexaAPI — if you specifically need Sora's style
    - $0.07/second (2.9x cheaper than direct access)
    """
    response = client.video.generate(
        model='sora-2',
        prompt=prompt,
        duration=duration,
        aspect_ratio='16:9'
    )
    return response.video_url


def generate_video_veo3(prompt: str, duration: int = 5) -> str:
    """
    Google Veo 3 — cinematic quality with audio
    - $0.15/second (2.7x cheaper than direct Google access)
    """
    response = client.video.generate(
        model='veo-3',
        prompt=prompt,
        duration=duration,
        aspect_ratio='16:9'
    )
    return response.video_url


if __name__ == '__main__':
    prompt = 'A serene mountain lake at golden hour, cinematic 4K, slow motion water ripples'
    
    print('Generating video with Kling 3.0 Pro (best Sora alternative)...')
    url = generate_video_kling(prompt)
    print(f'Video URL: {url}')
    print(f'Cost: ~$0.17 for 5 seconds')
    print()
    print('Get your free API key at: https://nexa-api.com')
    print('Also available on RapidAPI: https://rapidapi.com/nexaquency/api/kling-video-v3-pro')

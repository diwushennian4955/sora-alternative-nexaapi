/**
 * Sora Shutdown Migration Guide — Switch to NexaAPI
 * Sora was shut down on March 24, 2026. Use this script to migrate.
 * 
 * Get your free API key at: https://nexa-api.com
 * npm install nexaapi  // https://www.npmjs.com/package/nexaapi
 */

import NexaAPI from 'nexaapi';

// Initialize client — get free API key at https://nexa-api.com
const client = new NexaAPI({ apiKey: 'YOUR_FREE_API_KEY' });

/**
 * Best Sora replacement: Kling 3.0 Pro
 * - $0.0333/second (3x cheaper than Sora was)
 * - Native audio support
 * - Multi-shot cinematic control
 */
async function generateVideoKling(prompt, duration = 5) {
  const response = await client.video.generate({
    model: 'kling-3.0-pro',
    prompt,
    duration,
    aspectRatio: '16:9'
  });
  return response.videoUrl;
}

/**
 * Sora 2 via NexaAPI — if you specifically need Sora's style
 * - $0.07/second (2.9x cheaper than direct access)
 */
async function generateVideoSora2(prompt, duration = 5) {
  const response = await client.video.generate({
    model: 'sora-2',
    prompt,
    duration,
    aspectRatio: '16:9'
  });
  return response.videoUrl;
}

// Main
async function main() {
  const prompt = 'A serene mountain lake at golden hour, cinematic 4K, slow motion water ripples';
  
  console.log('Generating video with Kling 3.0 Pro (best Sora alternative)...');
  const url = await generateVideoKling(prompt);
  console.log('Video URL:', url);
  console.log('Cost: ~$0.17 for 5 seconds');
  console.log();
  console.log('Get your free API key at: https://nexa-api.com');
  console.log('Also on RapidAPI: https://rapidapi.com/nexaquency/api/kling-video-v3-pro');
}

main().catch(console.error);

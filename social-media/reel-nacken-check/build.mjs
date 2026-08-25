/**
 * Rendert reel.html Frame fuer Frame und encodiert daraus ein Instagram-Reel (1080x1920, 30 fps).
 *
 *   node build.mjs
 *
 * Optional per Env: FFMPEG=/pfad/zu/ffmpeg  FRAMES_DIR=/tmp/frames
 */
import { createRequire } from 'node:module';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const require = createRequire(import.meta.url);
const load = (...ids) => {
  for (const id of ids) { try { return require(id); } catch {} }
  throw new Error('Modul nicht gefunden: ' + ids.join(', '));
};

const { chromium } = load('playwright', '/opt/node22/lib/node_modules/playwright');
const FFMPEG = process.env.FFMPEG || (() => { try { return load('ffmpeg-static'); } catch { return 'ffmpeg'; } })();

const DIR = path.dirname(fileURLToPath(import.meta.url));
const FPS = 30;
const DURATION = 28.0;
const W = 1080, H = 1920;
const OUT = path.join(DIR, 'reel-nacken-check.mp4');
const COVER = path.join(DIR, 'cover.png');
const FRAMES = process.env.FRAMES_DIR || fs.mkdtempSync(path.join(os.tmpdir(), 'reel-'));

fs.mkdirSync(FRAMES, { recursive: true });

const browser = await chromium.launch({
  executablePath: process.env.CHROMIUM || '/opt/pw-browsers/chromium',
  args: ['--no-sandbox', '--font-render-hinting=none', '--force-color-profile=srgb', '--hide-scrollbars'],
});
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
await page.goto('file://' + path.join(DIR, 'reel.html'), { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);
await page.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 0 : i.decode().catch(() => 0))));

const total = Math.round(DURATION * FPS);
for (let f = 0; f < total; f++) {
  await page.evaluate(t => window.renderFrame(t), f / FPS);
  await page.screenshot({ path: path.join(FRAMES, String(f).padStart(5, '0') + '.jpg'), type: 'jpeg', quality: 94 });
  if (f % 60 === 0) process.stdout.write(`\r  Frame ${f}/${total}`);
}
process.stdout.write(`\r  Frame ${total}/${total}\n`);

// Cover / Titelbild
await page.evaluate(() => window.renderFrame(2.7));
await page.screenshot({ path: COVER, type: 'png' });
await browser.close();

execFileSync(FFMPEG, [
  '-y', '-hide_banner', '-loglevel', 'error',
  '-framerate', String(FPS), '-i', path.join(FRAMES, '%05d.jpg'),
  '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=44100',
  '-c:v', 'libx264', '-profile:v', 'high', '-level', '4.0', '-preset', 'slow', '-crf', '20',
  '-pix_fmt', 'yuv420p', '-r', String(FPS), '-g', String(FPS * 2),
  '-c:a', 'aac', '-b:a', '96k', '-shortest',
  '-movflags', '+faststart', OUT,
], { stdio: 'inherit' });

fs.rmSync(FRAMES, { recursive: true, force: true });
console.log('fertig ->', OUT, (fs.statSync(OUT).size / 1024 / 1024).toFixed(2) + ' MB');

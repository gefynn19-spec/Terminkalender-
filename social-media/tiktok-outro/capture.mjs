import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';

const SRC = '/home/user/Terminkalender-/social-media/tiktok-outro';
const FRAMES = '/tmp/claude-0/-home-user-Terminkalender-/6b3c0455-83b5-55c2-b784-2094c7c0553d/scratchpad/frames';
fs.rmSync(FRAMES, { recursive: true, force: true });
fs.mkdirSync(FRAMES, { recursive: true });

const FPS = 30;
const DAUER = 5.5;
const gesamt = Math.round(FPS * DAUER);

const fontCss = fs.readFileSync('fonts/inline.css', 'utf-8');
let html = fs.readFileSync(path.join(SRC, 'video.html'), 'utf-8');
html = html.replace('<style>', '<style>' + fontCss + '\n');

const browser = await chromium.launch({
  executablePath: '/opt/pw-browsers/chromium',
  args: ['--no-sandbox', '--font-render-hinting=none', '--force-device-scale-factor=1'],
});
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.setContent(html, { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);

const el = await page.$('.buehne');
for (let i = 0; i < gesamt; i++) {
  const t = i / FPS;
  await page.evaluate((tt) => window.setTime(tt), t);
  await el.screenshot({
    path: path.join(FRAMES, 'f-' + String(i).padStart(4, '0') + '.jpg'),
    type: 'jpeg', quality: 95,
  });
}
console.log(gesamt + ' Einzelbilder bei ' + FPS + ' fps (' + DAUER + ' s)');
await browser.close();

import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';

const SRC = '/home/user/Terminkalender-/social-media/beckenboden-grafik';
const OUT = '/home/user/Terminkalender-/social-media/beckenboden-grafik/export';
fs.mkdirSync(OUT, { recursive: true });

const fontCss = fs.readFileSync('fonts/inline.css', 'utf-8');
const slides = [
  ['Main.dc.html', '01-hook'],
  
  
  
];


function inlineImages(html) {
  return html.replace(/src="([^"]+\.(?:jpg|jpeg|png))"/g, (m, file) => {
    const buf = fs.readFileSync(path.join(SRC, file));
    const mime = file.endsWith('.png') ? 'image/png' : 'image/jpeg';
    return `src="data:${mime};base64,${buf.toString('base64')}"`;
  });
}

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox', '--font-render-hinting=none'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 2 });

for (const [file, name] of slides) {
  const raw = fs.readFileSync(path.join(SRC, file), 'utf-8');
  const inner = raw.match(/<x-dc>([\s\S]*?)<\/x-dc>/)[1].replace(/<helmet>[\s\S]*?<\/helmet>/, '');
  const html = `<!doctype html><html><head><meta charset="utf-8"><style>${fontCss}</style>` +
    `<style>html,body{margin:0;padding:0;background:#EFE7DA;-webkit-font-smoothing:antialiased;}</style>` +
    `</head><body>${inlineImages(inner)}</body></html>`;
  await page.setContent(html, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const el = await page.$('body > div');
  const box = await el.boundingBox();
  await el.screenshot({ path: path.join(OUT, `beckenboden-${name}.png`) });
  console.log(name, '->', Math.round(box.width) + 'x' + Math.round(box.height));
}

await browser.close();

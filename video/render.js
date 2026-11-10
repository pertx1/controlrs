// Exporta una página HTML animada (con window.setT) a MP4 9:16 1080x1920.
// Uso: node video/render.js pagina.html duracion fps salida.mp4
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');

(async () => {
  const [pagina, durS, fpsS, salida] = process.argv.slice(2);
  const dur = Number(durS), fps = Number(fpsS);
  const total = Math.round(dur * fps);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 360, height: 640 }, deviceScaleFactor: 3 });
  await page.goto('file://' + path.resolve(pagina));
  await page.evaluate(() => document.fonts.ready);

  const ff = spawn('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', '-f', 'image2pipe', '-framerate', String(fps),
    '-i', '-', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-r', String(fps), salida],
    { stdio: ['pipe', 'inherit', 'inherit'] });

  for (let f = 0; f < total; f++) {
    await page.evaluate(t => window.setT(t), f / fps);
    const img = await page.screenshot({ type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(img)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % (fps * 5) === 0) process.stdout.write(`  ${Math.round((f / total) * 100)}%\n`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
})();

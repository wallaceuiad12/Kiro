const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const cfgFile = process.argv[2] || './variations.json';
const outDir  = process.argv[3] || 'out';
const VARIATIONS = require(cfgFile.startsWith('.') ? cfgFile : './' + cfgFile);

(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const tplPath = 'file://' + path.resolve(__dirname, 'template.html');

  for (const v of VARIATIONS) {
    const page = await browser.newPage({
      viewport: { width: 1080, height: 1350 },
      deviceScaleFactor: 2,          // supersampling: renderiza 2160x2700
    });

    await page.addInitScript(cfg => { window.CONFIG = cfg; }, v);
    await page.goto(tplPath, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(350);

    const out = path.resolve(__dirname, outDir, `${v.id}@2x.png`);
    await page.screenshot({ path: out, clip: { x: 0, y: 0, width: 1080, height: 1350 } });

    // mede as faixas de tinta de cada bloco, para conferir alinhamento
    const bands = await page.evaluate(() => {
      const sel = ['.kicker', '.headline', '.body', '.data', '.ctabox', '.people', '.quote'];
      const r = {};
      for (const s of sel) {
        const el = document.querySelector(s);
        if (!el) continue;
        const b = el.getBoundingClientRect();
        r[s] = { top: Math.round(b.top), bottom: Math.round(b.bottom), w: Math.round(b.width) };
      }
      return r;
    });

    console.log(`${v.id.padEnd(28)} ok  ${JSON.stringify(bands)}`);
    await page.close();
  }

  await browser.close();
  console.log('\nrenderizado em post3/' + outDir + '/');
})();

// Gera o PNG 1080x1080 da capa a partir do HTML.
// Uso: node gerar_capa.mjs [arquivo.html] [saida.png]
// Precisa de playwright-core e de um Chromium. Caminhos podem ser trocados com
// PLAYWRIGHT_CORE e CHROMIUM.
import { createRequire } from 'module';
import { fileURLToPath, pathToFileURL } from 'url';
import path from 'path';

const aqui = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(import.meta.url);
const { chromium } = require(
  process.env.PLAYWRIGHT_CORE ||
    '/inner_container/opt/toolchains/.nvm/versions/node/v22.23.3/lib/node_modules/@playwright/mcp/node_modules/playwright-core',
);

const html = path.resolve(aqui, process.argv[2] || 'capa-agrofloresta-e-mais.html');
const saida = path.resolve(aqui, process.argv[3] || '../capa-agrofloresta-e-mais.png');

const browser = await chromium.launch({
  executablePath:
    process.env.CHROMIUM ||
    '/inner_container/opt/playwright/chromium_headless_shell-1232/chrome-headless-shell-linux64/chrome-headless-shell',
  args: ['--no-sandbox', '--disable-crash-reporter', '--disable-crashpad', '--no-zygote', '--disable-gpu', '--allow-file-access-from-files'],
});
const page = await browser.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 1 });
page.on('pageerror', (e) => console.error('[erro na página]', e.message));
await page.goto(pathToFileURL(html).href, { waitUntil: 'load' });
await page.waitForFunction(() => document.body.dataset.pronto === '1');
await page.locator('#capa').screenshot({ path: saida });
await browser.close();
console.log('capa gerada em', saida);

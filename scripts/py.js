// Lanza un script de Python igual en Windows (py) que en Mac/Linux (python3).
// Uso desde package.json: node scripts/py.js ruta/script.py [argumentos]
const { spawnSync } = require('child_process');
const candidatos = process.platform === 'win32' ? ['py', 'python'] : ['python3', 'python'];
for (const cmd of candidatos) {
  const r = spawnSync(cmd, process.argv.slice(2), { stdio: 'inherit' });
  if (!r.error) process.exit(r.status ?? 0);
}
console.error('No encuentro Python. Instálalo (mira video/INSTALAR-WINDOWS.md).');
process.exit(1);

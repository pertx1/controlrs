# Instalar la fábrica de vídeos en tu portátil Windows (una sola vez, ~15 min)

Abre **PowerShell** (botón de Windows → escribe "PowerShell" → Enter) y copia los comandos de uno en uno.

## 1. Programas (con winget, que ya viene en Windows 10/11)
```powershell
winget install -e --id Python.Python.3.12
winget install -e --id OpenJS.NodeJS.LTS
winget install -e --id Gyan.FFmpeg
winget install -e --id Git.Git
```
**Cierra PowerShell y ábrelo otra vez** para que los reconozca.

## 2. Descargar el proyecto
```powershell
cd $HOME\Documents
git clone https://github.com/pertx1/controlrs.git
cd controlrs
git checkout claude/pertx-personaje-mascota-7hmltw
```

## 3. Librerías
```powershell
py -m pip install numpy
npm install
npx playwright install chromium
```

## 4. Clave de ElevenLabs (para las voces)
1. elevenlabs.io → tu perfil (abajo a la izquierda) → **API Keys** → **Create API Key**.
2. En la carpeta `controlrs\video\` crea un archivo llamado `.env` con una sola línea:
   ```
   ELEVENLABS_API_KEY=pega_aqui_tu_clave
   ```
   Este archivo **no se sube a internet** (está en `.gitignore`). No compartas la clave con nadie.

## 5. Probar
```powershell
npm run video -- 1 1 --html     # previsualización del día 1 (ábrela con doble clic en video\salida\semana-01\dia-01.html)
npm run video -- 1 1            # vídeo del día 1 sin voz → video\salida\semana-01\dia-01.mp4
npm run voz -- 1 1              # genera las voces del día 1 (te dice cuánto gasta y te pregunta)
npm run video -- 1 1 --voz      # vídeo del día 1 con voz
```

Si algo falla, cópiame el mensaje de error tal cual y lo arreglo.

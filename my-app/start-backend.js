import { spawn } from 'child_process';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Check for windows
const isWin = os.platform() === 'win32';

const pythonPath = isWin 
    ? path.join(__dirname, '..', 'QR', 'Scripts', 'python.exe')
    : path.join(__dirname, '..', 'QR', 'bin', 'python');

const backendDir = path.join(__dirname, '..', 'scripts', 'Def');

console.log(`Starting backend using: ${pythonPath}`);

const child = spawn(pythonPath, ['-m', 'uvicorn', 'main:app', '--reload'], {
    cwd: backendDir,
    stdio: 'inherit',
    shell: true
});

child.on('error', (err) => {
    console.error('Failed to start backend process:', err);
});
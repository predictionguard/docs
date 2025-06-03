#!/usr/bin/env node
// scripts/fernBuild.mjs
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';
import { execSync } from 'child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Your model variables - change these in one place!
const MODELS = {
    TEXT_MODEL: "Hermes-3-Llama-3.1-70B",
    CODE_MODEL: "Hermes-3-Llama-3.1-70B",
    GO_MODEL: "Hermes3Llama3170B",
    JS_MODEL: "Hermes3Llama3170B",
    RUST_MODEL: "Hermes3Llama3170B"
};

function replaceVariables(content) {
    return content.replace(/\{\{(\w+)\}\}/g, (match, varName) => {
        return MODELS[varName] !== undefined ? MODELS[varName] : match;
    });
}

function copyDirectory(source, destination) {
    if (!fs.existsSync(destination)) {
        fs.mkdirSync(destination, { recursive: true });
    }

    const items = fs.readdirSync(source);

    items.forEach(item => {
        const sourcePath = path.join(source, item);
        const destPath = path.join(destination, item);
        const stat = fs.statSync(sourcePath);

        if (stat.isDirectory()) {
            copyDirectory(sourcePath, destPath);
        } else {
            fs.copyFileSync(sourcePath, destPath);
        }
    });
}

function processFiles(directory) {
    const items = fs.readdirSync(directory);

    items.forEach(item => {
        const itemPath = path.join(directory, item);
        const stat = fs.statSync(itemPath);

        if (stat.isDirectory()) {
            processFiles(itemPath);
        } else if (item.endsWith('.mdx') || item.endsWith('.md')) {
            const content = fs.readFileSync(itemPath, 'utf8');
            const processedContent = replaceVariables(content);

            if (content !== processedContent) {
                fs.writeFileSync(itemPath, processedContent);
                console.log(`✓ Processed variables in: ${path.relative(process.cwd(), itemPath)}`);
            }
        }
    });
}

function main() {
    const tempDir = path.join(process.cwd(), '.fern-build');
    const originalDir = process.cwd();

    try {
        // Clean and create temp directory
        if (fs.existsSync(tempDir)) {
            fs.rmSync(tempDir, { recursive: true });
        }

        console.log('📄 Creating temporary build directory...');

        // Copy entire project to temp directory
        copyDirectory(originalDir, tempDir);

        // Change to temp directory
        process.chdir(tempDir);

        console.log('🔄 Processing variables in MDX files...');

        // Process all MDX files in the temp directory
        if (fs.existsSync('pages')) {
            processFiles('pages');
        }
        if (fs.existsSync('fern')) {
            processFiles('fern');
        }

        console.log('🚀 Running Fern generate...');

        // Run fern generate from temp directory
        execSync('fern generate --docs', { stdio: 'inherit' });

        console.log('✅ Documentation generated successfully!');

    } catch (error) {
        console.error('❌ Build failed:', error.message);
        process.exit(1);
    } finally {
        // Return to original directory
        process.chdir(originalDir);

        // Optional: Clean up temp directory
        // if (fs.existsSync(tempDir)) {
        //   fs.rmSync(tempDir, { recursive: true });
        // }
    }
}

main();
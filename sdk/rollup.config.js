import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import typescript from '@rollup/plugin-typescript';

export default [
    {
        input: 'src/loader.ts',
        output: { file: 'dist/loader.js', format: 'iife', name: 'DAPLoader' },
        plugins: [resolve(), commonjs(), typescript()],
    },
    {
        input: 'src/runtime/index.ts',
        output: { file: 'dist/dap-sdk.js', format: 'iife', name: 'DAPRuntime' },
        plugins: [resolve(), commonjs(), typescript()],
    },
];

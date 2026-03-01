(function () {
    // Detect Site ID from script attribute, legacy global, or existing DAP object
    const script = document.currentScript;
    const siteId = script?.getAttribute('data-site-id') ||
        (window as any).DAP_SITE_ID ||
        (window as any).DAP?.siteId;

    if (!siteId) {
        console.error('[DAP] No Site ID found. Specify data-site-id in the script tag or set window.DAP.siteId before loading.');
        return;
    }

    // Initialize early event queue without wiping existing objects
    const queue: any[] = (window as any).DAP?._queue || [];
    (window as any).DAP = {
        ...(window as any).DAP, // Preserve siteId and other properties
        push: (event: any) => queue.push(event),
        ready: false,
        _queue: queue,
        siteId: siteId
    };

    // Load the main runtime script
    const SDK_URL = script?.getAttribute('src')?.replace('loader.js', 'dap-sdk.js') || 'http://localhost:8000/sdk/dap-sdk.js'; // Fallback

    // Add cache-buster (PRD/TAD compliance for ensuring latest SDK version)
    const CACHE_BUSTER = `?v=${Date.now()}`;
    const sdkScript = document.createElement('script');
    sdkScript.src = SDK_URL + CACHE_BUSTER;
    sdkScript.async = true;
    sdkScript.onload = () => {
        console.log('[DAP] Runtime loaded.');
    };

    document.head.appendChild(sdkScript);
})();

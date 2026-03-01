import { useEffect } from 'react';

const DAPLoader = () => {
    useEffect(() => {
        // This component injects the DAP SDK script into the document head
        // Site ID is pulled from environment variables
        const SITE_ID = import.meta.env.VITE_DAP_SITE_ID || '8cc359fc-63cf-4270-998e-fb5c789c3c95';
        const API_URL = import.meta.env.VITE_DAP_API_URL || 'http://localhost:8000';

        console.log(`[DAP] Initializing SDK for site: ${SITE_ID}`);

        const script = document.createElement('script');

        // In a real scenario, this would be the actual SDK build file (e.g., dap-sdk.js)
        // For now, we point it to where the SDK will be hosted/served
        script.src = `${API_URL}/sdk/dap.js?t=${new Date().getTime() + 1}`;
        script.async = true;
        script.setAttribute('data-site-id', SITE_ID);
        script.setAttribute('data-api-base', API_URL);

        // Error handling if SDK fails to load
        script.onerror = () => {
            console.error('[DAP] Failed to load SDK. Ensure the backend is running at', API_URL);
        };

        document.head.appendChild(script);

        return () => {
            // Cleanup: removing script on unmount (optional, but good practice for SPA)
            if (document.head.contains(script)) {
                document.head.removeChild(script);
            }
        };
    }, []);

    return null; // This is a logic-only component
};

export default DAPLoader;

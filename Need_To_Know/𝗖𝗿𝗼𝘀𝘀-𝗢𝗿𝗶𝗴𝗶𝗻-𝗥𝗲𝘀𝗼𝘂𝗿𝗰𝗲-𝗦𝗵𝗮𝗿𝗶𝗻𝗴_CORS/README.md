𝗪𝗵𝗮𝘁 𝗶𝘀 𝗖𝗿𝗼𝘀𝘀-𝗢𝗿𝗶𝗴𝗶𝗻 𝗥𝗲𝘀𝗼𝘂𝗿𝗰𝗲 𝗦𝗵𝗮𝗿𝗶𝗻𝗴 (𝗖𝗢𝗥𝗦)?

Browsers use CORS, a method, to prevent websites from requesting data from different URLs. A request from a browser includes an origin header in the request message. The browser allows it if it gets to the server of the exact origin; if not, the browser blocks it.

We can deal with CORS issues on the backend. Cross-origin requests require that the values for origin and 𝗔𝗰𝗰𝗲𝘀𝘀-𝗖𝗼𝗻𝘁𝗿𝗼𝗹-𝗔𝗹𝗹𝗼𝘄-𝗢𝗿𝗶𝗴𝗶𝗻 in the response headers match and it is set by the server. When you add an origin to the backend code, the CORS middleware only permits this URL to communicate with other origins and utilize it for cross-origin resource requests.

There are two ways to fix CORS issues:

𝟭. 𝗖𝗼𝗻𝗳𝗶𝗴𝘂𝗿𝗲 𝘁𝗵𝗲 𝗕𝗮𝗰𝗸𝗲𝗻𝗱 𝘁𝗼 𝗔𝗹𝗹𝗼𝘄 𝗖𝗢𝗥𝗦

Server can let all domains with 𝗔𝗰𝗰𝗲𝘀𝘀-𝗖𝗼𝗻𝘁𝗿𝗼𝗹-𝗔𝗹𝗹𝗼𝘄-𝗢𝗿𝗶𝗴𝗶𝗻: \*. This actually turns off same-origin policy, which is not recommended. Another optin would be only to allow particular domain, which is better option, e.g., 𝗔𝗰𝗰𝗲𝘀𝘀-𝗖𝗼𝗻𝘁𝗿𝗼𝗹-𝗔𝗹𝗹𝗼𝘄-𝗢𝗿𝗶𝗴𝗶𝗻: 𝗵𝘁𝘁𝗽𝘀://𝘀𝗼𝗺𝗲𝗱𝗼𝗺𝗮𝗶𝗻.𝗰𝗼𝗺.

𝟮. 𝗨𝘀𝗲 𝗮 𝗣𝗿𝗼𝘅𝘆 𝗦𝗲𝗿𝘃𝗲𝗿

We can use a proxy server to call external API. It acts as a middleware between client and the server. If server doesn't return proper headers defined by CORS, we can add then in the proxy.

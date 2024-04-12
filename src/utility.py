import browser_cookie3
import time
from typing import Literal

_cookies = {}
def get_cookies(cookie_domain: str) -> dict: 
     if cookie_domain not in _cookies: 
         _cookies[cookie_domain] = {} 
         for cookie in browser_cookie3.load(cookie_domain): 
             _cookies[cookie_domain][cookie.name] = cookie.value 
     return _cookies[cookie_domain]

def get_Cookie(service_Name: Literal["Bard", "BardTS", "BardCC", "Claude"]) -> str:
    """
    Retrieve and return the session cookie value for the specified service.

    This function takes a service name as input, either 'Bard', 'BardTS', or 'Claude',
    and retrieves the corresponding session cookie value from the browser's stored cookies.
    The cookie value is then returned.

    Note: This function requires the 'browser_cookie3' library to be installed.

    Args:
        service_name (Literal["Bard", "BardTS", "Claude"]): The name of the service
            for which to retrieve the session cookie.

    Returns:
        str: The session cookie value for the specified service, or None if no matching
            cookie is found.
    """

    domains = {
        "Bard": "google",
        "BardTS": "google",
        "BardCC": "google",
        "Claude": "claude",
    }
    domain = domains[service_Name]

    if service_Name.lower() == "bardts":
        bardSessionName = "__Secure-1PSIDTS"
    elif service_Name.lower() == "bardcc":
        bardSessionName = "__Secure-1PSIDCC"
    else:
        bardSessionName = "__Secure-1PSID"

    sessName = {
        "claude": "sessionKey",
        "google": bardSessionName,
    }
    sessionName = sessName[domain]

    cookies = browser_cookie3.load(domain_name=domain)

    return (
        filtered_cookies[-1].value
        if (
            filtered_cookies := [
                cookie
                for cookie in cookies
                if sessionName == cookie.name
            ]
        )
        else None
    )


def ConvertToChatGPT(message: str, model: str):
    """Convert response to ChatGPT JSON format.

    Args:
        message (String): Response string.
        model (String): Model name string.

    Yields:
        str: JSON response chunks.
    """

    OpenAIResp = {
        "id": f"chatcmpl-{str(time.time())}",
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": model,
        "choices": [
            {
                "delta": {
                    "role": "assistant",
                    "content": message,
                },
                "index": 0,
                "finish_reason": "Stop",
            }
        ],
    }

    # openairesp = {
    # "id": f"chatcmpl-{str(time.time())}",
    # "object": "chat.completion.chunk",
    # "created": int(time.time()),
    # "model": "gpt-3.5-turbo",
    # "choices": [
    #     {
    #         "message": {
    #             "role": "assistant",
    #             "content": resp,
    #         },
    #         "index": 0,
    #         "finish_reason": "stop",
    #     }
    # ],

    # jsonresp = json.dumps(OpenAIResp)

    yield f"{OpenAIResp}\n"
    # yield jsonresp
    # yield OpenAIResp

async def ConvertToChatGPTStream(message: str, model: str):
    """Convert response to ChatGPT JSON format.

    Args:
        message (String): Response string.
        model (String): Model name string.

    Yields:
        str: JSON response chunks.
    """

    OpenAIResp = {
        "id": f"chatcmpl-{str(time.time())}",
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": model,
        "choices": [
            {
                "delta": {
                    "role": "assistant",
                    "content": message,
                },
                "index": 0,
                "finish_reason": "Stop",
            }
        ],
    }

    # openairesp = {
    # "id": f"chatcmpl-{str(time.time())}",
    # "object": "chat.completion.chunk",
    # "created": int(time.time()),
    # "model": "gpt-3.5-turbo",
    # "choices": [
    #     {
    #         "message": {
    #             "role": "assistant",
    #             "content": resp,
    #         },
    #         "index": 0,
    #         "finish_reason": "stop",
    #     }
    # ],

    # jsonresp = json.dumps(OpenAIResp)

    yield f"{OpenAIResp}\n"
    # yield jsonresp
    # yield OpenAIResp

def IsSession(session_id: str) -> bool:
    """Checks if a valid session ID is provided.

    Args:
        session_id (str): The session ID to check

    Returns:
        bool: True if session ID is valid, False otherwise
    """

    # if session_id is None or not session_id or session_id.lower() == "none":
    if session_id is None:
        return False
    return False if not session_id else session_id.lower() != "none"



#############################################
####                                     ####
#####        Develope Functions         #####
####                                     ####

# print("".join(response))


def fake_data_streamer_OLD():
    for _ in range(10):
        yield b"some fake data\n"
        time.sleep(0.5)


def fake_data_streamer():
    openai_response = {
        "id": f"chatcmpl-{str(time.time())}",
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": "gpt-3.5-turbo",
        "usage": {
            "prompt_tokens": 0,
            "completion_tokens": 100,
            "total_tokens": 100,
        },
        "choices": [
            {
                "delta": {
                    "role": "assistant",
                    "content": "Yes",
                },
                "index": 0,
                "finish_reason": "[DONE]",
            }
        ],
    }
    for _ in range(10):
        yield f"{openai_response}\n"
        # yield b"some fake data\n"
        time.sleep(0.5)


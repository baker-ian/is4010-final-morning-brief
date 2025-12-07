# AI Agents Usage Log

## Tools Used
* **Gemini:** Used for project planning, debugging API 401 errors, generating code structure, and writing unit tests with `pytest-mock`.

## Development Process
1.  **Ideation:** I asked Gemini for project ideas suitable for a graduating senior. We settled on the "Morning Brief CLI" to demonstrate API integration and data persistence.
2.  **Implementation:**
    * Gemini provided the "Professional Package" folder structure.
    * Helped debug OpenWeatherMap API key activation delays.
    * Suggested using ESPN's public endpoints to avoid paid sports APIs.
3.  **Testing:**
    * Gemini explained how to use `pytest-mock` to test network calls without hitting the real API.
    * Helped configure the `.github/workflows/tests.yml` file for CI/CD.

## Reflection
AI was particularly helpful in handling the "boilerplate" (folder structure, config files) and debugging obscure errors (like the `ModuleNotFoundError` when running scripts). It allowed me to focus on the logic of parsing sports data rather than fighting with syntax.
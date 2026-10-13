# jev-testing

#### Testing Jev AI with SeleniumBase to identify the presence of CAPTCHAs.

**The Task:** Jev analyzes a webpage's HTML and returns three structured results:

1.  **CAPTCHA detected:**  `Yes` or `No`.
    
2.  **Confidence score:**  `0–100`, indicating Jev's confidence in its detection decision. Scores may vary between runs and are not calibrated probabilities.
    
3.  **CAPTCHA type:** If the answer is `Yes`, one of the following choices:
    -   `Cloudflare Turnstile`
    -   `Google reCAPTCHA`
    -   `hCaptcha` 
    -   `DataDome Slider`
    -   `Friendly CAPTCHA`
    -   `Other CAPTCHA`

If the answer is `No`, `captcha_type` is `None` in Python (equivalent to `null` in JSON).

### Expected Output Format

```json
{
  "captcha_detected": "Yes",
  "score": 99,
  "captcha_type": "Cloudflare Turnstile"
}
```

When no CAPTCHA is detected:

```json
{
  "captcha_detected": "No",
  "score": 52,
  "captcha_type": null
}
```

### Step 1: Install the Python requirements

```
python -m pip install -r requirements.txt
```

### Step 2: Add the `TYPESAFE_API_KEY` to your environment

```
export TYPESAFE_API_KEY="YOUR_API_KEY_HERE"
```

Keep your API key private. Do not commit it to your repository.

This command sets the variable for the current shell session. If you open a new Terminal window, you may need to set it again unless you have configured it in your shell profile.

### Step 3: Run the SeleniumBase Jev script

```
python seleniumbase_jev.py
```

The script opens each URL using SeleniumBase CDP, waits 1.5 seconds, retrieves the page HTML, reduces it to relevant CAPTCHA-related evidence, and sends that evidence to Jev for analysis.

### Sample Output

The following is an example of the output format. Scores may vary between runs.

```
* https://muse.jhu.edu/verify
{'captcha_detected': 'Yes', 'score': 99, 'captcha_type': 'Friendly CAPTCHA'}
* https://planetminecraft.com/account
{'captcha_detected': 'Yes', 'score': 99, 'captcha_type': 'Cloudflare Turnstile'}
* https://www.idealista.com/venta-viviendas/
{'captcha_detected': 'Yes', 'score': 96, 'captcha_type': 'DataDome Slider'}
* https://www.pokemon.com/us/pokedex
{'captcha_detected': 'Yes', 'score': 87, 'captcha_type': 'Google reCAPTCHA'}
* https://accounts.hcaptcha.com/demo
{'captcha_detected': 'Yes', 'score': 98, 'captcha_type': 'hCaptcha'}
* https://example.com
{'captcha_detected': 'No', 'score': 52, 'captcha_type': None}
```

### Notes and Limitations
-   The output shown above is illustrative; actual results and scores may vary.
-   The score is derived from Jev's ordinal confidence rating. It should not be interpreted as a calibrated probability.
-   Detection is based on the HTML evidence available when the page is inspected.
-   A CAPTCHA integration may exist even when a challenge is not currently visible.
-   Dynamically injected CAPTCHA elements may be missed.
-   The HTML reduction process retains all `<script>` and `<iframe>` tags, along with elements and text containing CAPTCHA-related keywords. Pages with many scripts or iframes may still produce substantial input.
-   A `No` result means that Jev did not identify sufficient evidence in the supplied HTML; it does not guarantee that the page has no CAPTCHA.

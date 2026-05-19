# J.A.R.V.I.S

## 🎤 Microphone Setup & Compatibility

- J.A.R.V.I.S uses [sounddevice](https://python-sounddevice.readthedocs.io/) (not PyAudio) for microphone input, ensuring compatibility with most Python versions.
- If you get errors related to sound device or audio input:
  - Ensure you have installed `sounddevice` and `soundfile`:
    ```bash
    pip install sounddevice soundfile
    ```
  - Check your Windows privacy settings to allow microphone access.
  - Make sure your microphone is plugged in and working.
  - Make sure no other program is using your microphone.
- If the assistant says “Microphone error: ...”, check settings and dependencies as above.


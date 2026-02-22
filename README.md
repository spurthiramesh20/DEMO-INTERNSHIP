## DEMO_INTERNSHIP

Simple Python app that calls a public API, saves the response to JSON, and logs activity.

### Project Structure
- `app/`: Application code
- `config/`: Configuration files
- `tests/`: Test suite
- `output/`: Output files

### Setup
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Configure
Edit `config/config.yaml` to change the API URL or output filename.

### Run
From the project root:
```powershell
python -m app.main
```

### Tests
```powershell
pytest
```

### Notes
- Use `python -m ...` to run the app as a module so package imports resolve correctly.

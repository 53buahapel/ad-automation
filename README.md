# ad-automation

automation exploit and submit flags to the AD CTF platform.
This template originally written by [@evandrarf](https://github.com/evandrarf)

## Requirements 
- `python3` with pip
- `requests` library
- `python-dotenv` library
- `flask` library

## Usage

1. Clone this repository
2. Install the requirements
3. Make a `.env` file based on the `.env.example` file
```bash
cp .env.example .env
``` 
4. Run the server with `python3 server.py`
5. Make exploit based on the `template.py` file
```bash
cp template.py exploit-<chall_id>.py
```
6. Thing to do in `exploit.py`
   - Fill CHALL_ID with the challenge id
   - Fill CHALL_PORT with the challenge port
   - Create exploit function
   - Change the tick

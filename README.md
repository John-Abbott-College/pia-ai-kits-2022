# PIA AI Kits 2022
Code for AI kits used in JACU PIA 2022-2023 grant.

This repository contains code used to develop educational kits that teach Artificial Intelligence for college students in technical programs.

The research is done by a team from John Abbott College and Concordia University (collectively called JACU), with a grant awarded by PIA (Pôle montréalais d’enseignement supérieur en intelligence artificielle) during the 2022-2023 academic year.

Codebase organization:

- **hardware-testing:** Testing of individual hardware sensors and actuators. 
- **platform-testing:** Testing of specific AI flatforms or frameworks. 

## Development & Testing

- Include a brief description of each test in the Readme contained in `hardware-testing` or `platform-testing`
- If a test is larger than a single file, create a folder.
- Use python virtual environments for specific tests and update `requirements.txt` once done.

```bash
python3 -m pip freeze > requirements.txt
```


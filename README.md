# plagiarism_check
A plagiarism check tool, which is a wrapper of mosspy basing on Stanford MOSS system.

# Requirement

python3.7 or higher version is required.

# Setup Environment
1. Install virtual environment
```
pip install virtualenv
```

2. Create venv directory
```
python3 -m venv .venv
```

3. Activate virtual environment
```
source .venv/bin/activate
```

4. Install packages from requirements.txt
```
pip install -r requirements.txt
```

5. Deactivate virtual environment
$deactivate


# Usage
```
python3 plagiarism_check.py [OPTIONS]
```
### Options:
* -s, --src PATH   Source directory of submissions.
* -n, --name TEXT  The name of file to check.
* -d, --save PATH  Target directory for saving reports.
* -k, --key TEXT   User Key for MOSS system.
* --help           Show this message and exit.

# Referrences
* [Stanford MOSS System](http://moss.stanford.edu/)
* [mosspy](https://github.com/soachishti/moss.py)

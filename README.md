# finite

[![Build Status](https://travis-ci.com/patrickziegler/finite.svg?branch=master)](https://travis-ci.com/patrickziegler/finite)

### Prerequisites

The following packages are needed

* `python` (>= 3.5)
* `numpy`
* `setuptools`
* `unittest`
* `virtualenv` (optional)

### Build and Install

1. Clone this repository
```bash
git clone --recursive https://github.com/patrickziegler/finite.git && cd finite
```

2. Create and activate a virtual environment
```bash
export PREFIX=.
python3 -m virtualenv "${PREFIX}/env" --system-site-packages
source "${PREFIX}/env/bin/activate"
```

3. Install dependencies (in virtual environment) and create symbolic links to this package
```bash
pip install -r requirements.txt
./setup.py develop --prefix "${PREFIX}/env"
```

3. Run the tests (should also work outside the virtual environment)
```bash
./setup.py test
```

4. System-wide installation
```bash
./setup.py install
```

## Authors

*  Patrick Ziegler

## License

This project is licensed under the GPL - see the [LICENSE](LICENSE) file for details

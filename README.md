# finite

### Prerequisites

The following librarys are needed

* `numpy`
* `setuptools`
* `unittest`
* `virtualenv` (optional)

### Build and Install

1. Clone this repository
```bash
git clone --recursive https://github.com/patrickziegler/finite.git && cd finite
```

2. Create a virtual environment and create symbolic links to this package
```bash
export PREFIX=.
python3 -m virtualenv "${PREFIX}/env" --system-site-packages
source "${PREFIX}/env/bin/activate"
./setup.py develop --prefix "${PREFIX}/env"
```

3. Run the tests
```bash
./setup.py test
```

4. Build and install to another destination *(alternative)*
```bash
./setup.py install
```

## Authors

*  Patrick Ziegler

## License

This project is licensed under the GPL - see the [LICENSE](LICENSE) file for details

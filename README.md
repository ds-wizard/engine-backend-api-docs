# Engine Backend API Docs

[![User Guide](https://img.shields.io/badge/docs-User%20Guide-informational)](https://guide.ds-wizard.org)
[![License](https://img.shields.io/github/license/ds-wizard/engine-backend)](LICENSE)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/4975/badge)](https://bestpractices.coreinfrastructure.org/projects/4975)

*API Docs for Data Stewardship Wizard*

### Requirements

 - **Python** (recommended 3.11)
 - **Makefile** (recommended 3.81)

### Run

For building the output that contains the Swagger specifications, diffs between Swagger specifications and the root index file, please run the following from the root of the project 

```bash
$ make build
```

### How to add new version of API Docs?

Add the Swagger specification under the corresponding version into the `specifications` folder. Then, run the `make build` to rebuild the project. The result will be in the `output` folder. 

## License

This project is licensed under the Apache License v2.0 - see the [LICENSE](LICENSE) file for more details.
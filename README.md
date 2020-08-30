# [Proyectos](http://proyectos.hive.pt)

Project page generation from GitHub repository.

## Dependencies

Current implementation uses both the markdown parser from [Appier Framework Extras](https://github.com/hivesolutions/appier_extras) and the GitHub API client implementation from the [GitHub API](https://github.com/hivesolutions/github_api) project.

## Configuration

| Name                     | Type  | Default | Description                                                                       |
| ------------------------ | ----- | ------- | --------------------------------------------------------------------------------- |
| **THEME**                | `str` | `None`  | Sets the default theme to be used by the system (eg: `opensans`, `merriweather`). |
| **GITHUB_AUTH_USERNAME** | `str` | `None`  | The username to be used for git clone operations.                                 |
| **GITHUB_AUTH_PASSWORD** | `str` | `None`  | The password to be used for git clone operations.                                 |

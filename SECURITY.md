# Security Policy

## Reporting a vulnerability

Please do not publish API keys, tokens, credentials, private certificates, or personal memory data in a public Issue.

For a security concern that does not expose private information, open an Issue with the minimum reproduction details needed.

For a concern involving a real secret or private user data:

1. revoke or rotate the exposed credential immediately;
2. remove the secret from the working tree;
3. remember that deleting it in a later commit does not erase it from Git history;
4. avoid posting the secret in screenshots, logs, Issues, or pull requests.

## Sensitive local files

Contributors should treat these categories as local/private:

- API-key configuration
- authentication tokens
- certificates / private keys
- personal assistant memory
- local user configuration containing credentials

## Scope

This policy covers security issues introduced or maintained in this derivative repository. Issues inherited from upstream may also need to be reported to the upstream MARK LI project.

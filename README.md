# AwsStsEnv
`aws-sts-env` is a simple command line tool that you can use to convert the JSON output of certain `aws sts` commands into bash `export` statements, so you can then use them directly in an environment that needs them as environment variables.
 
 ## Installation
 To install, run
 ```bash
 pip install git+https://github.com/TMiguelT/AwsStsEnv.git#egg=aws_sts_env
 ```
 
 ## Usage
 
To use `aws-sts-env`, simply run one of the following commands, and pipe the output into the `aws-sts-env` command:
* `aws sts get-session-token`
* `aws sts assume-role`
* `aws sts assume-role-with-saml`
* `aws sts assume-role-with-web-identity`

For instance:
```bash
aws sts assume-role --role-arn arn:aws:iam::999999999999:role/Administrator --role-session-name some_session_name | aws-sts-env 
```

This will print out the following text (but with correct values):
```bash
export AWS_ACCESS_KEY_ID='AAAAAAAAAAAAAAAAAAAA'
export AWS_SECRET_ACCESS_KEY='bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
export AWS_SESSION_TOKEN='cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'
```

If you want to export these variables on a remote server etc, you can then copy and paste this text into a `bash`/`zsh` session.

If you want to export these variables directly, on the same machine you're running the `aws sts` commands, you can execute the result of this command, using `$()`. For instance:
```bash
$(aws sts assume-role --role-arn arn:aws:iam::999999999999:role/Administrator --role-session-name some_session_name | aws-sts-env)
```


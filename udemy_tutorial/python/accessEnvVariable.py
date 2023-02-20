import os


def get_env_var(key):
    # Get the list of user's
    # environment variables
    all_env_var = os.environ
    print('All Env var: {}'.format(dict(all_env_var)))

    # get specific env var
    env_var = os.environ[key]
    print('Env var: {}'.format(env_var))


if __name__ == '__main__':
    get_env_var('USER_TYPE')

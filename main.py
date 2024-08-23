import os
from dotenv import load_dotenv, find_dotenv
from typing import List, Tuple
import asana
from asana.rest import ApiException
from pprint import pprint


def initialize_environment() -> Tuple[str, str]:
    load_dotenv(find_dotenv())
    ACCESS_TOKEN: str = os.getenv("ACCESS_TOKEN", "")
    WORKSPACE_GID: str = os.getenv("WORKSPACE_GID", "")
    return ACCESS_TOKEN, WORKSPACE_GID


def configure_asana(access_token: str) -> asana.UsersApi:
    configuration = asana.Configuration()
    configuration.access_token = access_token
    api_client = asana.ApiClient(configuration)

    users_api_instance = asana.UsersApi(api_client)
    return users_api_instance


def main() -> None:
    ACCESS_TOKEN, WORKSPACE_GID = initialize_environment()
    users_api_instance = configure_asana(ACCESS_TOKEN)

    try:
        opts = {}
        me = users_api_instance.get_user("me", opts)
        print("Hello world! " + "My name is " + me["name"] + "!")

    except ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)


if __name__ == "__main__":
    main()

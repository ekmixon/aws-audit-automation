from botocore.exceptions import ClientError

UNAUTH_ERRORS = ('UnauthorizedOperation',
                 'AccessDeniedException')


def yield_handling_errors(func, *args, **kwargs):
    try:
        yield from func(*args, **kwargs)
    except ClientError as e:
        if e.response['Error']['Code'] in UNAUTH_ERRORS:
            print(f"{e}")
        else:
            print(f"Unexpected error: {e}")

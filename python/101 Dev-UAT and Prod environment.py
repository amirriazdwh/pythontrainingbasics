"""


from dynaconf import Dynaconf



settings = Dynaconf(

    settings_files=['settings/settings.dev.toml', 'settings/settings.uat.toml', 'settings/settings.prod.toml'],

    environments=True,

)



def main():

    import argparse



    parser = argparse.ArgumentParser(description="Load environment-specific settings")

    parser.add_argument('--env', required=True, choices=['dev', 'uat', 'prod'], help="Environment to load")

    args = parser.parse_args()



    # Set the environment

    settings.setenv(args.env)



    # Access the environment variable

    s3_treasury_file = settings.S3_TREASURY_FILE

    print(f"S3 Treasury File: {s3_treasury_file}")



if __name__ == "__main__":

    main()





python your_script.py --env dev

python your_script.py --env uat

python your_script.py --env prod

"""
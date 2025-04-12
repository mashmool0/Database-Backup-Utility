import click
import requests
import json


@click.group()
def cli():
    """این برنامه برای مدیریت دیتابیس طراحی شده است"""
    pass


@click.command()
@click.argument("database")
@click.argument("host")
@click.argument("password")
@click.argument("port")
@click.argument("username")
def connectdb(username, host, password, port, database):
    click.echo(f"Database: {database}")
    click.echo(f"Host: {host}")
    click.echo(f"Username: {username}")
    click.echo(f"Password: {password}")
    click.echo(f"Port: {port}")
    url = 'http://localhost:8000/api/'
    headers = {'Content-Type': 'application/json'}
    data = {
        'username': username,
        'host': host,
        'password': password,
        'port': str(port),
        'database': database
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()

        if response.status_code == 200:
            print("API Call Was Successfully")
            print("response : ", response.text)
            click.echo("Database connected")
        else:
            click.echo(f"Connection Failed \nstatus code :{str(response.status_code)}\nmessage:{response.text}", )


    except requests.exceptions.RequestException as e:
        print(e)
        raise None


cli.add_command(connectdb)

if __name__ == "__main__":
    cli()

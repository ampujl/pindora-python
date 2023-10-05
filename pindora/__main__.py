import click
import json

from pindora import Pindora


@click.group()
@click.argument("apikey")
@click.option("-c", "--command", "command", type=str, default="list")
@click.option("-id", "--id", "id", type=str)
@click.option("-co", "--code", "code", type=str)
@click.option("-n", "--name", "name", type=str)
@click.option("-pm", "--partymode", "party_mode", is_flag=True, default=False)
@click.option("-url1", "--url1", "url1", type=str)
@click.option("-url2", "--url2", "url2", type=str)      
def cli():
    pass


@cli.command()
def pindora(apikey, domain, command, id, code, name, party_mode, url1, url2) -> None:
    pindora = Pindora(apikey)

    match command:
        case "list":
            result = pindora.list_pindoras()
        case "read":
            result = pindora.read_pindora(id)
        case "update":
            result = pindora.update_pindora(id, name, party_mode)
        case "open":
            if url2 == None:
                result = pindora.open_pindora(url1, code)
            else:
                result = pindora.open_pindora(url1, url2, code)
    click.echo(json.dumps(result, indent=4, separators=(',', ': ')))

@cli.command()              
def pin(apikey, domain, command, id, code, name, party_mode, url1, url2) -> None:
    match command:    
        case "list":
            result = pindora.list_pins()
        case "create":
            result = pindora.create_pin(code, name)
        case "update":
            result = pindora.update_pin(code, name)
        case "delete":
            result = pindora.delete_pin(code)
    click.echo(json.dumps(result, indent=4, separators=(',', ': ')))
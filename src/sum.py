import click

@click.command()
# @click.argument('num1', type=int)
# @click.argument('num2', type=int)
#To call this in CLI, uses python sum.py 5 7

@click.option('--num1', type=int)
@click.option('--num2', type=int)
#To call this in CLI, uses python sum.py --num1=5 --num2=7

def main(num1, num2):
    """Simple program that adds two numbers."""
    result = num1 + num2
    click.echo(f"The sum of {num1} and {num2} is {result}")

if __name__ == '__main__':
    main()


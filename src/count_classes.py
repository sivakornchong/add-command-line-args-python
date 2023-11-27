import pandas as pd

import click
@click.command()
@click.argument('file_path', type=str)
@click.argument('group_col', type=str)
@click.argument('output_file', type=str)

def main(file_path, group_col, output_file):
    # read in wisconsin breast cancer data
    data = pd.read_csv(file_path)

    result = data.groupby(group_col).size().reset_index(name='Count')
    result = result.rename(columns={group_col: 'Class'})

    result.to_csv(output_file, index=False) # 'results/cancer/class_count.csv'
    click.echo(f'Output file created at {output_file} with data of length {len(result)}')

if __name__ == "__main__":
    main()


#python count_classes.py '../data/agaricus-lepiota.csv' 'mushroom-class' '../results/mushroom.csv'
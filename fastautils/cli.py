import click

from .io import read_fasta_file
from . import operations


@click.group()
def cli():
    pass


@click.command()
@click.argument('masked_sequences_file')
@click.argument('reference_sequences_file')
@click.argument('output_sequences_file')
def unmask(masked_sequences_file, reference_sequences_file, output_sequences_file):
    masked_sequences = read_fasta_file(masked_sequences_file)
    reference_sequences = read_fasta_file(reference_sequences_file)
    with open(output_sequences_file, "w") as output_file:
        for sequence in masked_sequences:
            unmasked_sequence = operations.unmask(sequence, reference_sequences[0])
            output_file.write(f"{unmasked_sequence.name}\n")
            output_file.write(f"{''.join(unmasked_sequence.sequence.tolist())}\n")



cli.add_command(unmask)

if __name__ == '__main__':
    cli()

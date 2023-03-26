import os


def get_fields():
    directory = 'data'
    fields = [dirs for dirs in os.listdir(directory)]
    fields.sort()
    fields_dct = {}
    for field in fields:
        fields_dct[field] = field
    return fields_dct

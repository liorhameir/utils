import argparse
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import numpy as np


parser = argparse.ArgumentParser(description="Sample TensorFlow XML-to-TFRecord converter")
parser.add_argument("-x", "--xml_dir", help="Path to the folder where the input .xml files are stored.", type=str)
parser.add_argument("-o", "--out_name", help="name to the output .csv.", type=str)
args = parser.parse_args()


def xml_to_csv(path):
    """Iterates through all .xml files (generated by labelImg) in a given directory and combines
    them in a single Pandas dataframe.

    Parameters:
    ----------
    path : str
        The path containing the .xml files
    Returns
    -------
    Pandas DataFrame
        The produced dataframe
    """

    xml_list = []
    for xml_file in os.listdir(path):
        if xml_file.endswith('.xml'):

            tree = ET.parse(path + '/' + xml_file)
            root = tree.getroot()
            for member in root.findall('object'):
                value = (root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][0].text),
                         int(member[4][1].text),
                         int(member[4][2].text),
                         int(member[4][3].text)
                         )
                xml_list.append(value)

    column_name = ['filename', 'width', 'height',
                   'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    if args.xml_dir is not None:
        xml_df = xml_to_csv(args.xml_dir)
        xml_df.to_csv(path_or_buf=args.out_name, index=False)
    print('Successfully converted xml to csv.')

main()
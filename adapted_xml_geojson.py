# python adapted_xml_geojson.py -i <input_directory> -o <output_directory>

import argparse
import os
import xmltodict # type: ignore
import simplejson # type: ignore

# useful functions
def hex2rgb(hexcode): # hexcode example: '#FF0840'
    r,g,b = int(hexcode[1:3],16),int(hexcode[3:5],16),int(hexcode[5:7],16)
    return [r,g,b]

# read in arguments from command line
parser = argparse.ArgumentParser()
parser.add_argument('-i',help='xml input directory')
parser.add_argument('-o',help='geojson output directory')
args = parser.parse_args()

# Generate output directory
os.mkdir(args.o)

# Read in list of XML files
input_files = [f for f in os.listdir(args.i) if f.endswith('.xml') ] #Only converts the XML files
for file in input_files:
    f = open(args.i + "/" + file, 'r')
    # from the xml file, we can retrieve a dictionary
    xml_dict = xmltodict.parse(f.read())


    xml_polygons = xml_dict['ASAP_Annotations']['Annotations']['Annotation']
    geojson_polygons = []

    for xml_polygon in xml_polygons:
        name = xml_polygon['@PartOfGroup']
        color = xml_polygon['@Color']
        coords = []
        for coord in xml_polygon['Coordinates']['Coordinate']:
            coords.append([float(coord['@X']), float(coord['@Y'])])
        coords.append(coords[0])

        geojson_polygon = {'type':'Feature',
                        'id':'PathDetectionObject',
                        'geometry':{
                            'type': 'Polygon',
                            'coordinates': [coords]
                        },
                        'properties':{
                            'objectType': 'annotation',
                            'classification': {
                                'name': name,
                                'color': [244,250,88]
                            },
                            'color': hex2rgb(color)
                        }
                        }
        geojson_polygons.append(geojson_polygon)

    geojson = {'type': 'FeatureCollection', 'features': geojson_polygons}

    output_filename = file[:-3] + "geojson" # Amending final filenames for the geojson annotations
    f = open(args.o + "/" + output_filename, 'w')
    f.write(simplejson.dumps(geojson,indent=4))
    f.close()

print(f'geojson directory {args.o} generated from xml directory {args.i}')

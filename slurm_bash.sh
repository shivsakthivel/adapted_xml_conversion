#!/bin/bash

#! This file represents a very simple header header that you can use as the
#! basis for your own jobs. Copy this file and amend it.

#!#############################################################
#!#### Modify the options in this section as appropriate ######
#!#############################################################

#! Give your job a name
#SBATCH -J annotation_conversion
#! How many cores per task?
#SBATCH --cpus-per-gpu=1
#! How much memory do you need?
#SBATCH --mem=8G
#! How much wallclock time will be required?
#SBATCH --time=1:00:00
#! What types of email messages do you wish to receive?
#SBATCH --mail-type=END
#! Specify your email address here otherwise you won't recieve emails!
#SBATCH --mail-user=Shiv.Sakthivel@cruk.cam.ac.uk
#! Uncomment this to prevent the job from being requeued (e.g. if
#! interrupted by node failure or system downtime):
##SBATCH --no-requeue
#! General partition
#SBATCH -p general
#! Specify a GRES (generic resource) of type gpu and how many you want
#! SBATCH --gres gpu:1
#SBATCH -o ./slurm/out/annotations/conversion.out
#SBATCH -e ./slurm/error/annotations/conversion.error

python adapted_xml_geojson.py -i annotations -o geojson_annotations
